import requests
import threading
import re
import time

# Domain validation function

def is_valid_domain(domain):
    pattern = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$'
    return re.match(pattern, domain) is not None

while True:
    domain = input('Enter the target domain (e.g., youtube.com): ').strip()
    if is_valid_domain(domain):
        break
    else:
        print("Invalid domain name. Please enter a valid domain like 'example.com'.")

with open('subdomains.txt') as file:
    subdomains = file.read().splitlines()

discivered_subdomains = []
lock = threading.Lock()

def check_subdomain(subdomain):
    url = f'http://{subdomain}.{domain}'
    try:
        requests.get(url, timeout=5)
    except (requests.ConnectionError, requests.Timeout):
        pass
    except requests.RequestException:
        pass
    else:
        print("[+] Discovered subdomain: ", url)
        with lock:
            discivered_subdomains.append(url)

threads = []

start_time = time.time()
for subdomain in subdomains:
    subdomain = subdomain.strip()
    if not subdomain or subdomain.startswith('#'):
        continue
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
end_time = time.time()

with open("discovered_subdomains.txt", 'w') as f:
    for subdomain in discivered_subdomains:
        print(subdomain, file=f)

# Print summary in green if possible
try:
    GREEN = '\033[92m'
    RESET = '\033[0m'
    print(f"{GREEN}Results saved to discovered_subdomains.txt")
    print(f"Total subdomains found: {len(discivered_subdomains)}")
    print(f"Time taken: {end_time - start_time:.2f} seconds{RESET}")
except:
    print("Results saved to discovered_subdomains.txt")
    print(f"Total subdomains found: {len(discivered_subdomains)}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                