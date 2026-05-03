import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor
import argparse

#Function to scan a given port on a specific IP address
def scan_port(ip, port):
    try:
        # Create a new socket using IPv4 and TCP protocols
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout of 1 second for the connection attempt
        s.settimeout(1)
        
        # Try connecting to the IP and port. 0 = success (Open Port)
        result = s.connect_ex((str(ip), port))
        if result == 0:
            print(f"[+] Port {port} is OPEN on {ip}")
        # Close socket
        s.close()
    except:
        # Ignore errors (like unreachable hosts) to keep the scanner running continuously
        pass

#  Function to scan all IPs and ports through the network and manage threads
def start_scanner(target_network, start_port, end_port, threads):
    print(f"[*] Scanning started on: {target_network}")
    print(f"[*] Port range: {start_port} - {end_port}")
    
    try:
        # Turn the CIDR input into a list of IPs
        network = ipaddress.ip_network(target_network, strict=False)
        
        #Use multiple threads to make scanning faster
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for ip in network.hosts():
                for port in range(start_port, end_port + 1):
                    # Submit each port scan task to the thread pool
                    executor.submit(scan_port, ip, port)
                    
    except Exception as e:
        print(f"[!] Error: {e}")

#Entry point -handles user input
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Network Discovery Tool")
    # Input for target network
    parser.add_argument("-t", "--target", help="Target CIDR (e.g. 192.168.1.0/24)", required=True)
    # Input for port range
    parser.add_argument("-p", "--ports", help="Port range (e.g. 20-100)", default="1-1024")
    #Input for number of threads
    parser.add_argument("-w", "--threads", help="Number of threads", type=int, default=100)
    
    args = parser.parse_args()
    
    try:
        #Get start and end ports from input
        start_p, end_p = map(int, args.ports.split("-"))
        #Run the scanner
        start_scanner(args.target, start_p, end_p, args.threads)
    except ValueError:
        print("[!] Port range format should be 'start-end' (e.g. 1-1000)")
