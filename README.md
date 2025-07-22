# 🔍 Subdomain Enumeration Toolkit

A multi-feature Python toolkit for **subdomain enumeration and DNS analysis**. This project supports both **command-line interface (CLI)** and a **Graphical User Interface (GUI)** for discovering subdomains from a large list and saving valid ones for reconnaissance or cybersecurity assessments.

---

## 📁 Project Structure

```
project/
├── subdomain_enum_gui.py         # GUI-based subdomain enumeration tool (Tkinter)
├── cli_subdomain_enum.py         # CLI-based threaded subdomain checker
├── dns_records_fetcher.py        # DNS records fetcher for common types (A, MX, etc.)
├── subdomains.txt                # Wordlist (~114,000 subdomains)
└── discovered_subdomains.txt     # Output file storing discovered subdomains
```
