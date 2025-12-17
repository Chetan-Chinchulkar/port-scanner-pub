# mini-nmap

A lightweight, **non-root Nmap-like TCP port scanner** written in Python.

This tool implements the parts of Nmap that **do not require elevated privileges**, making it safe and easy to run in most environments. It is intended for learning, testing, and authorized security assessments.

---

## Features

- ✅ No `sudo` / administrator permissions required  
- ✅ TCP connect port scanning (`nmap -sT` equivalent)  
- ✅ Basic service / banner detection (`nmap -sV` lite)  
- ✅ No host discovery (`nmap -Pn` behavior)  
- ✅ Multithreaded scanning for speed  
- ✅ Cross-platform (Linux, macOS, Windows)  

---

## Requirements

- Python **3.8 or newer**
- No external Python dependencies (standard library only)

---

## Project Structure

```
mini_nmap/
├── scanner.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository or copy the files locally:

```
git clone https://github.com/Chetan-Chinchulkar/port-scanner-pub.git
cd mini_nmap
```

If you are not using Git, simply place `scanner.py` and `requirements.txt` in the same directory.

### (Optional) Create a virtual environment

```
python3 -m venv venv
source venv/bin/activate      # Linux / macOS
# venv\Scripts\activate       # Windows
```

### Install requirements

```
pip install -r requirements.txt
```

> Note: This project uses only Python’s standard library, so no packages will actually be installed.

---

## Usage

### Scan common ports (default)

```
python3 scanner.py <target>
```

Example:

```
python3 scanner.py scanme.nmap.org
```

---

### Scan a specific port range

```
python3 scanner.py <target> <start_port> <end_port>
```

Example:

```
python3 scanner.py 192.168.1.1 1 1024
```

---

## Example Output

```
Starting scan against scanme.nmap.org
Scan type: TCP connect (-sT)
Host discovery: disabled (-Pn)

[+] 22/tcp OPEN
    Service: SSH-2.0-OpenSSH_8.2

[+] 80/tcp OPEN
    Service: HTTP/1.1 200 OK

Scan completed.
```

---

## How It Compares to Nmap

| Feature | mini-nmap | Nmap |
|-------|-----------|------|
| No sudo required | ✅ | ❌ |
| TCP connect scan | ✅ | ✅ |
| Service detection | ✅ (basic) | ✅ (advanced) |
| SYN scan (`-sS`) | ❌ | ✅ |
| UDP scan | ❌ | ✅ |
| OS detection | ❌ | ✅ |
| NSE scripts | ❌ | ✅ |

---

## Limitations

- Cannot perform SYN scans (`-sS`) without root privileges  
- No OS fingerprinting  
- No UDP scanning  
- Service detection is banner-based and best-effort  

These limitations are inherent to non-privileged scanning.

---

## Legal Notice

⚠️ **Use responsibly**

This tool is intended for:
- Educational purposes
- Testing systems you own
- Authorized security assessments

Scanning systems without explicit permission may be illegal in your jurisdiction.

---

## Future Improvements

Possible enhancements that still do not require elevated privileges:

- JSON / XML output formats  
- Nmap-style table output  
- Improved service fingerprint database  
- IPv6 support  
- CIDR range scanning  
- Rate limiting and timing profiles  

---

