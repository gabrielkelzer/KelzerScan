import socket
import os
clear = lambda: os.system('clear')
print ("""\033[1;31m
 _  __    _              _____                 
| |/ /   | |            / ____|                
| ' / ___| |_______ _ _| (___   ___ __ _ _ __  
|  < / _ \ |_  / _ \ '__\___ \ / __/ _` | '_ \ 
| . \  __/ |/ /  __/ |  ____  | (_| (_| | | | |
|_|\_\___|_/___\___|_| |_____/ \___\__,_|_| |_| \033[0m\033[1;34mV1\033[0m

\033[1;33mCreated By: Gabriel Kelzer\033[0m
                                               
""")

NET_BOA_RUIM = input('SUA INTERNET É BOA ? [S/N] ')


if NET_BOA_RUIM == "S":
	VAR_DEMORA = 1
elif NET_BOA_RUIM == "N":
	VAR_DEMORA = 5
else:
		print('\033[31mERA S OU N ! AGORA A DEMORA PRA VERIFICAR SE A PORTA TÁ ABERTA É 6 SEGUNDOS ;-; \033[0m')
		VAR_DEMORA = 6






site = input('DIGITE O SITE: ')
portas = [21, 23, 80, 443, 8080, 4040, 4444]

for p in portas:
	c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c.settimeout(VAR_DEMORA)
	codigo = c.connect_ex(('{}'.format(site), p))
	if codigo == 0:
		print ("A porta ({}) está aberta".format(p))
