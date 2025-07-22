import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
import requests
import re
import time

# Domain validation function

def is_valid_domain(domain):
    pattern = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$'
    return re.match(pattern, domain) is not None

discivered_subdomains = []
lock = threading.Lock()

class SubdomainEnumGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Subdomain Enumeration Tool')
        self.domain_var = tk.StringVar()
        self.file_path = None
        self.threads = []
        self.enumeration_thread = None
        self.is_enumerating = False
        self.start_time = None
        self.end_time = None

        tk.Label(root, text='Target Domain:').grid(row=0, column=0, padx=5, pady=5, sticky='e')
        tk.Entry(root, textvariable=self.domain_var, width=30).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(root, text='Select subdomains.txt', command=self.select_file).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(root, text='Start', command=self.start_enum).grid(row=0, column=3, padx=5, pady=5)

        self.output = scrolledtext.ScrolledText(root, width=80, height=25)
        self.output.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        self.output.tag_configure('summary', foreground='green')

    def select_file(self):
        self.file_path = filedialog.askopenfilename(title='Select subdomains.txt', filetypes=[('Text Files', '*.txt')])
        if self.file_path:
            self.output.insert(tk.END, f'Selected file: {self.file_path}\n')

    def start_enum(self):
        domain = self.domain_var.get().strip()
        if not is_valid_domain(domain):
            messagebox.showerror('Invalid Domain', "Please enter a valid domain like 'example.com'.")
            return
        if not self.file_path:
            messagebox.showerror('No File', 'Please select a subdomains.txt file.')
            return
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, f'Starting enumeration for {domain}\n')
        discivered_subdomains.clear()
        self.is_enumerating = True
        self.start_time = time.time()
        self.enumeration_thread = threading.Thread(target=self.enumerate_subdomains, args=(domain, self.file_path))
        self.enumeration_thread.start()
        self.root.after(100, self.check_enumeration_thread)

    def enumerate_subdomains(self, domain, file_path):
        with open(file_path) as file:
            subdomains = file.read().splitlines()
        threads = []
        def check_subdomain(subdomain):
            url = f'http://{subdomain}.{domain}'
            try:
                requests.get(url, timeout=5)
            except (requests.ConnectionError, requests.Timeout):
                pass
            except requests.RequestException:
                pass
            else:
                with lock:
                    discivered_subdomains.append(url)
                self.root.after(0, lambda: self.output_subdomain(url))
        for subdomain in subdomains:
            subdomain = subdomain.strip()
            if not subdomain or subdomain.startswith('#'):
                continue
            thread = threading.Thread(target=check_subdomain, args=(subdomain,))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        self.is_enumerating = False
        self.end_time = time.time()

    def output_subdomain(self, url):
        self.output.insert(tk.END, f'[+] Discovered subdomain: {url}\n')
        self.output.see(tk.END)

    def check_enumeration_thread(self):
        if self.is_enumerating and self.enumeration_thread.is_alive():
            self.root.after(100, self.check_enumeration_thread)
        else:
            elapsed = self.end_time - self.start_time if self.end_time and self.start_time else 0
            summary = (f'\nEnumeration complete. Saving results...\n'
                       f'Results saved to discovered_subdomains.txt\n'
                       f'Total subdomains found: {len(discivered_subdomains)}\n'
                       f'Time taken: {elapsed:.2f} seconds\n')
            with open('discovered_subdomains.txt', 'w') as f:
                for subdomain in discivered_subdomains:
                    f.write(subdomain + '\n')
            self.output.insert(tk.END, summary, 'summary')
            self.output.see(tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = SubdomainEnumGUI(root)
    root.mainloop() 