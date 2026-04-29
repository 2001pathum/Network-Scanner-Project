import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor
import argparse

# 1. Function to scan a specific port on an IP address
def scan_port(ip, port):
    try:
        # Create a new socket object using IPv4 and TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout of 1 second for the connection attempt
        s.settimeout(1)
        
        # Try connecting to the IP and port. 0 means success (Open)
        result = s.connect_ex((str(ip), port))
        if result == 0:
            print(f"[+] Port {port} is OPEN on {ip}")
        s.close()
    except:
        # Ignore errors (e.g., host unreachable) to keep the scanner running
        pass

# 2. Function to iterate through the network and manage threads
def start_scanner(target_network, start_port, end_port, threads):
    print(f"[*] Scanning started on: {target_network}")
    print(f"[*] Port range: {start_port} - {end_port}")
    
    try:
        # Parse the network CIDR block
        network = ipaddress.ip_network(target_network, strict=False)
        
        # Use Multi-threading to speed up the process
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for ip in network.hosts():
                for port in range(start_port, end_port + 1):
                    # Submit each port scan task to the thread pool
                    executor.submit(scan_port, ip, port)
                    
    except Exception as e:
        print(f"[!] Error: {e}")

# 3. Entry point - Handles Command Line Arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Discovery Tool")
    parser.add_argument("-t", "--target", help="Target CIDR (e.g. 192.168.1.0/24)", required=True)
    parser.add_argument("-p", "--ports", help="Port range (e.g. 20-100)", default="1-1024")
    parser.add_argument("-w", "--threads", help="Number of threads", type=int, default=100)
    
    args = parser.parse_args()
    
    try:
        # Split the port range string into start and end integers
        start_p, end_p = map(int, args.ports.split("-"))
        start_scanner(args.target, start_p, end_p, args.threads)
    except ValueError:
        print("[!] Port range format should be 'start-end' (e.g. 1-1000)")