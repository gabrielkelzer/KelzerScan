import socket
import os
clear = lambda: os.system('clear')
clear()
print ("""\033[1;31m
 _  __    _              _____                 
| |/ /   | |            / ____|                
| ' / ___| |_______ _ _| (___   ___ __ _ _ __  
|  < / _ \ |_  / _ \ '__\___ \ / __/ _` | '_ \ 
| . \  __/ |/ /  __/ |  ____  | (_| (_| | | | |
|_|\_\___|_/___\___|_| |_____/ \___\__,_|_| |_| \033[0m\033[1mV2\033[0m

\033[1;33mCreated By: Gabriel Kelzer\033[0m
                                               
""")

NET_BOA_RUIM = input('\033[35mSUA INTERNET É BOA ? [s/n]  \033[0m ')


if NET_BOA_RUIM == "s":
	VAR_DEMORA = 1
elif NET_BOA_RUIM == "n":
	VAR_DEMORA = 5
else:
		print('\033[37mO programa irá tentar por 6 segundos verificar se as portas estão abertas !!!  ;-; \033[0m')
		VAR_DEMORA = 6






site = input('\033[35mDIGITE O SITE: \n \033[0m')
portas = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 161, 194, 389, 443, 445, 514, 515, 587, 631, 636, 666, 993, 995, 1080, 1433, 1521, 2049, 3306, 3389, 5432, 5900, 6660, 8000, 8443, 9100, 9418, 9999, 10000, 1121, 27017, 28015, 3306, 3389, 5432, 5900, 6660, 8333, 8880, 9000, 9042, 9200, 9300, 9418, 11211, 27017, 33060, 50070, 54321, 5984, 6379, 6666, 8008, 8081, 8333, 8880, 9000, 9042, 9160, 10000, 11211, 27017, 28015, 33060, 50070, 54321,5601, 6379, 7077, 9042, 9160, 10000, 11211, 27017, 28015, 33060, 50070, 54321, 5672, 6379, 9042, 9160, 10250, 10255, 2375, 3198, 33060, 50070, 54321, 5672, 6379, 8080, 8123, 9042, 9160 ]

for p in portas:
	c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c.settimeout(VAR_DEMORA)
	codigo = c.connect_ex(('{}'.format(site), p))
	if codigo == 0:
		print ("=> Porta ({}) aberta ! ".format(p))
SOPRAPAUSARATELAMSM = input('\033[41mAPERTE ENTER PARA SAIR:  \033[0m ')
