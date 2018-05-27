#Juego del ahorcado
import os
import random
import platform

aos = platform.system()
idraw = ['|------------------|\n|                  |\n|                  |\n|                  |\n|                  |\n|------------------|','|------------------|\n|                  |\n|                  |\n|                  |\n|            =     |\n|------------------|','|------------------|\n|                  |\n|                  |\n|            |     |\n|            =     |\n|------------------|','|------------------|\n|                  |\n|            |     |\n|            |     |\n|            =     |\n|------------------|','|------------------|\n|            |     |\n|            |     |\n|            |     |\n|            =     |\n|------------------|','|------------------|\n|           -|     |\n|            |     |\n|            |     |\n|            =     |\n|------------------|','|------------------|\n|          --|     |\n|            |     |\n|            |     |\n|            =     |\n|------------------|','|------------------|\n|         ---|     |\n|            |     |\n|            |     |\n|            =     |\n|------------------|','|------------------|\n|        /---|     |\n|            |     |\n|            |     |\n|            =     |\n|------------------|','|------------------|\n|        /---|     |\n|        o   |     |\n|      --|-- |     |\n|       / \  =     |\n|------------------|']
lista_palabras = open('palabras.txt').read().splitlines()
mi_palabra = ''
intento = 0

def clear():
	if aos == 'Windows':
		os.system('cls')
	if aos == 'Linux':
		os.system('clear')

while True:
	palabra_correcta = random.choice(lista_palabras)
	clear()
	print("====================")
	print("|   EL AHORCADO    |")
	print("====================")
	print("|1. Partida Nueva. |")
	print("|2. Salir.         |")
	print("====================")

	while True:
		try:
			option = int(input("\n[?] Que deseas hacer? -> "))
			break
		except ValueError:
			print("[!] Usa el numero acorde a tu eleccion.")

	if option == 2:
		exit()

	if option == 1:

		while True:
			clear()
			fallas = 0
			print(idraw[intento])
			for i in palabra_correcta:
				if i in mi_palabra:
					print(i, end='')
				else:
					print("_",end='')
					fallas+=1
			if fallas == 0:
				print("\nFelicidades, has ganado.")
				intento = 0
				mi_palabra = ''
				input("Presona para volver al menu.")
				break

			if intento == 9:
				print("\nPERDISTE!!!")
				print("La palabra era: \'%s\'" % (palabra_correcta))
				input('Presiona para volver al menu.')
				intento = 0
				mi_palabra = ''
				break

			mi_letra = input("\n[*] Introduce tu letra: ")
			mi_palabra += mi_letra

			if mi_letra not in palabra_correcta:
				print("Te equivocaste.")
				intento += 1