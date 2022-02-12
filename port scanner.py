# made with <3
from ast import For
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
            print("                                                                           1.0")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)

            host = input(Fore.WHITE + "Enter Ip: ")
            port = int(input(Fore.WHITE + "Enter specific port to scan: "))


            def portScan(port):
                if sock.connect_ex((host, port)):
                    print(Fore.RED + "Port" + str(port) + " is Closed!")
                else:
                    print(Fore.GREEN + "Port " + str(port) + " is Open!")

            portScan(port)
            goBack()

        # Scans all ports
        def aPort():
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
            print("                                                                           1.0")    
            ip = input(Fore.WHITE + "Enter the IP address: ")

            def scan(ip, port):
                scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                scanner.settimeout(1)
                try:
                    scanner.connect((ip, port))
                    scanner.close()
                    with printLock:
                        print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " is Open!")
                except:
                    pass
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as exec:
                for port in range(1000):
                    exec.submit(scan, ip, port + 1)

            goBack()
                    

        # Asks user to choose between two modes
        def question():
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
            print("                                                                           1.0")    
            print(Fore.MAGENTA + "\ntype 1 For specific port, 2 For all ports, 3 for exit") 
            ans = input(Fore.WHITE + "Please enter: ")
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