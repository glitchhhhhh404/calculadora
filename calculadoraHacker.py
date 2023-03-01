
inicio = """\033[1;31m
╔═╗╔══╗╔╗─╔═╗╔╦╗╔╗─╔══╗╔══╗╔═╗╔═╗╔══╗
║╔╝║╔╗║║║─║╔╝║║║║║─║╔╗║╚╗╗║║║║║╬║║╔╗║
║╚╗║╠╣║║╚╗║╚╗║║║║╚╗║╠╣║╔╩╝║║║║║╗╣║╠╣║
╚═╝╚╝╚╝╚═╝╚═╝╚═╝╚═╝╚╝╚╝╚══╝╚═╝╚╩╝╚╝╚╝\033[m

 \033[1;32m
   ╔╗─╔╗╔═══╗╔═══╗╔╗╔═╗╔═══╗╔═══╗
   ║║─║║║╔═╗║║╔═╗║║║║╔╝║╔══╝║╔═╗║
   ║╚═╝║║║─║║║║─╚╝║╚╝╝─║╚══╗║╚═╝║
   ║╔═╗║║╚═╝║║║─╔╗║╔╗║─║╔══╝║╔╗╔╝
   ║║─║║║╔═╗║║╚═╝║║║║╚╗║╚══╗║║║╚╗
   ╚╝─╚╝╚╝─╚╝╚═══╝╚╝╚═╝╚═══╝╚╝╚═╝\033[m"""
print(inicio)
import os,math
soma=lambda a,b:a+b;subtrai=lambda a,b:a-b;multiplica=lambda a,b:a*b;dividi=lambda a,b:a/b
while True:
	try:
		entrada = int(input("""
		1 para soma
		2 subtrai
		3 multiplica
		4 para dividir
		5 raiz de numero:
		6 para sair    """ ))
	
	
	except ValueError:
		print("ocorreu um error")
		
	else:
		if (entrada ==1):
			n1 = int(input("Numero 1: "))
			
			n2 = int(input("Numero 2: "))
			print(f"A soma e {soma(n1,n2)}")
		
		elif (entrada ==2):
			n1 = int(input("Numero 1: "))
			n2 = int(input("Numero 2: "))
			print(f"a subtração e {subtrai(n1,n2)}")
		
			
		elif (entrada == 3):
			n1 = int(input("Numero 1: "))
			n2 = int(input("Numero 2: "))
			print(f"A multiplicação e {multiplica(n1,n2)}")
		elif (entrada ==4):		
			n1 = int(input("Numero 1: "))
			n2 = int(input("Numero 2: "))
			print(f"A divisão e {dividi(n1,n2)}")

		elif (entrada == 5):
			num = int(input("digite um numero para saber a Raiz dele "))
			print(f"a raiz e {math.sqrt(num)}")
		elif (entrada == 6):
			print("voce saiu ")
			break
