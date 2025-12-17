#!/usr/bin/env python3
"""
scanner.py
--------------------------------
Non-root Nmap-like scanner
Features:
 - TCP connect scan (-sT equivalent)
 - Basic service/version detection (-sV lite)
 - No host discovery (-Pn behavior)
 - No sudo required
"""

import socket
import sys
import threading
from queue import Queue

# ---------------- CONFIG ----------------
DEFAULT_PORTS = [
    21, 22, 23, 25, 53, 80, 110,
    139, 143, 443, 445, 3306,
    3389, 5432, 8080
]

TIMEOUT = 2
THREADS = 100
# ----------------------------------------


def tcp_connect_scan(target, port):
    """
    TCP connect scan (similar to nmap -sT)
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        result = sock.connect_ex((target, port))

        if result == 0:
            return True
        return False
    except:
        return False
    finally:
        try:
            sock.close()
        except:
            pass


def grab_banner(target, port):
    """
    Basic service detection (nmap -sV lite)
    """
    try:
        sock = socket.socket()
        sock.settimeout(TIMEOUT)
        sock.connect((target, port))

        # HTTP needs a request
        if port in (80, 8080, 443):
            sock.sendall(b"HEAD / HTTP/1.0\r\n\r\n")

        banner = sock.recv(1024)
        sock.close()

        if banner:
            return banner.decode(errors="ignore").strip()
        return None
    except:
        return None


def worker(target, queue):
    while not queue.empty():
        port = queue.get()
        if tcp_connect_scan(target, port):
            print(f"[+] {port}/tcp OPEN")

            banner = grab_banner(target, port)
            if banner:
                first_line = banner.splitlines()[0]
                print(f"    Service: {first_line}")
            else:
                print("    Service: unknown")

        queue.task_done()


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <target> [start_port end_port]")
        sys.exit(1)

    target = sys.argv[1]

    # Port selection
    if len(sys.argv) == 4:
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
        ports = list(range(start_port, end_port + 1))
    else:
        ports = DEFAULT_PORTS

    print(f"\nStarting scan against {target}")
    print("Scan type: TCP connect (-sT)")
    print("Host discovery: disabled (-Pn)\n")

    queue = Queue()

    for port in ports:
        queue.put(port)

    for _ in range(THREADS):
        t = threading.Thread(target=worker, args=(target, queue), daemon=True)
        t.start()

    queue.join()
    print("\nScan completed.")


if __name__ == "__main__":
    main()
