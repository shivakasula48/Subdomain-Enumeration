# 🔍 Subdomain Enumeration Toolkit

A multi-feature Python toolkit for **subdomain enumeration and DNS analysis**. This project supports both **command-line interface (CLI)** and a **Graphical User Interface (GUI)** for discovering subdomains from a large list and saving valid ones for reconnaissance or cybersecurity assessments.

---

## 📁 Project Structure

```
project/
├── subdomain_enum_gui.py         # GUI-based subdomain enumeration tool (Tkinter)
├── subdomain_enum.py             # CLI-based threaded subdomain checker
├── dns_enum.py                   # DNS records fetcher for common types (A, MX, etc.)
├── subdomains.txt                # Wordlist (~114,000 subdomains)
└── discovered_subdomains.txt     # Output file storing discovered subdomains
```



---

## 🚀 Features

### ✅ Subdomain Enumerator (CLI)
- Uses multithreading for fast checking
- Validates domains using regex
- Reads from a massive `subdomains.txt` wordlist
- Saves output to `discovered_subdomains.txt`
- Provides summary statistics (count & time taken)

### 🖥️ Subdomain Enumerator (GUI)
- Built with **Tkinter**
- User-friendly interface
- File selector for subdomain list
- Real-time output with scrollable view
- Color-coded summary after completion

### 📡  dns_enum (basic)
- Supports fetching:
  - `A`, `AAAA`, `CNAME`, `MX`, `TXT`, `SOA` records
- Uses `dnspython` to resolve and display DNS information for a domain

---

## ⚙️ Requirements
---

## ⚙️ Tool & Library Requirements

### 1. `dns_enum.py`
**Required Library:**  
- `dnspython`

**Install with:**  
```bash
pip install dnspython
```

---

### 2. `subdomain_enum.py`  
**Required Library:**  
- `requests`

**Install with:**  
```bash
pip install requests
```

---

### 3. `subdomain_enum_gui.py`  
**Required Libraries:**  
- `requests`  
- `tkinter` (comes pre-installed with most Python distributions)

**Install with:**  
```bash
pip install requests
```

> 📌 _No need to install `tkinter` via pip; it's part of the standard library for most Python installations. If missing, install via your OS package manager._
