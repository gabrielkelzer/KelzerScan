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
|_|\_\___|_/___\___|_| |_____/ \___\__,_|_| |_| \033[0m\033[1;34mV1\033[0m

\033[1;33mCreated By: Gabriel Kelzer\033[0m
                                               
""")

NET_BOA_RUIM = input('\033[37mSUA INTERNET É BOA ? [s/n] \n \033[0m ')


if NET_BOA_RUIM == "s":
	VAR_DEMORA = 1
elif NET_BOA_RUIM == "n":
	VAR_DEMORA = 5
else:
		print('\033[37m \n O programa irá tentar por 6 segundos verificar se as portas estão abertas !!!  ;-; \n \033[0m')
		VAR_DEMORA = 6






site = input('\033[37mDIGITE O SITE: \n \033[0m')
portas = [21, 23, 80, 443, 8080, 4040, 4444]

for p in portas:
	c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c.settimeout(VAR_DEMORA)
	codigo = c.connect_ex(('{}'.format(site), p))
	if codigo == 0:
		print ("=> Porta ({}) aberta ! ".format(p))
