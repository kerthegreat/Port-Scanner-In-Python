# made with <3 by kerbs
import platform
import concurrent.futures
import os
import socket
import time
import threading
import colorama
from colorama import Fore
colorama.init()

def main():
        printLock = threading.Lock()
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') 
        def goBack():
            a = input(Fore.WHITE + "Please type 1 to go back, and type 2 to exit the application ")
            if a == "1":
                question()
            elif a == "2":
                exit()
            else:
                goBack()
                
        # Scans specific port
        def sPort():
            os.system('title Scan Specific Port')
            clearConsole()
            print(Fore.RED + r"""
            ██▓███   ▒█████   ██▀███  ▄▄▄█████▓  ██████  ▄████▄   ▄▄▄       ███▄    █ 
            ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ 
            ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
            ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
            ▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
            ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
            ░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
            ░░       ░ ░ ░ ▒    ░░   ░   ░      ░  ░  ░  ░          ░   ▒      ░   ░ ░ 
                        ░ ░     ░                    ░  ░ ░            ░  ░         ░ 
                                                        ░                             """)
            print("                                                                           v1.2")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)

            host = input(Fore.YELLOW + "Enter Ip: ")
            port = int(input(Fore.YELLOW + "Enter specific port to scan: "))



            def portScan(port):
                if sock.connect_ex((host, port)):
                    print(Fore.WHITE + f"Port [{port}]" + Fore.RED + " is Closed!")
                else:
                    print(Fore.WHITE + f"Port [{port}]" + Fore.GREEN + " is Open!")

            portScan(port)
            goBack()

        # Scans all ports
        def aPort():
            os.system('title Scan all Ports')
            clearConsole()
            print(Fore.RED + r"""
            ██▓███   ▒█████   ██▀███  ▄▄▄█████▓  ██████  ▄████▄   ▄▄▄       ███▄    █ 
            ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ 
            ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
            ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
            ▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
            ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
            ░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
            ░░       ░ ░ ░ ▒    ░░   ░   ░      ░  ░  ░  ░          ░   ▒      ░   ░ ░ 
                        ░ ░     ░                    ░  ░ ░            ░  ░         ░ 
                                                        ░                             """)
            print("                                                                           v1.2")    
            ip = input(Fore.YELLOW + "Enter the IP address: ")
            portRange = int(input(Fore.YELLOW + f"Please Enter the Port Range: "))

            def scan(ip, port):
                scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                scanner.settimeout(1)
                try:
                    scanner.connect((ip, port))
                    scanner.close()
                    with printLock:
                        print(Fore.WHITE + f"Port [{port}]" + Fore.GREEN + " is Open!")
                except:
                    pass
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as exec:
                for port in range(portRange):
                    exec.submit(scan, ip, port + 1)

            goBack()
                    

        # Asks user to choose between two modes
        def question():
            os.system('title Port Scanner')
            clearConsole()
            print(Fore.RED + r"""
            ██▓███   ▒█████   ██▀███  ▄▄▄█████▓  ██████  ▄████▄   ▄▄▄       ███▄    █ 
            ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █ 
            ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒
            ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒
            ▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░
            ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
            ░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░
            ░░       ░ ░ ░ ▒    ░░   ░   ░      ░  ░  ░  ░          ░   ▒      ░   ░ ░ 
                        ░ ░     ░                    ░  ░ ░            ░  ░         ░ 
                                                        ░                             """)
            print("                                                                           v1.2")    
            print(Fore.MAGENTA + "\ntype 1 For specific port, 2 For all ports, 3 for exit") 
            print(Fore.WHITE + f"┌──({platform.node()})-[~]")
            ans = input("└─$ ")
            if ans == "1":
                sPort()
            elif ans == "2":
                aPort()
            elif ans == "3":
                print("Exiting Application! Goodbye!!!")
                time.sleep(2)
                exit()
            else:
                question()

        question()

if __name__ == "__main__":
    main()