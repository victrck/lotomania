import numpy as np 
import random  as rd



lista_quant_numeros_linha = []
lista_index_numeros_linha =[]
lista_auxiliar_sequencia_coluna = []
lista_verif_colunas = []
bilhete_premiado = []
sequencia_coluna=[]

i = 0
acumulador = 0
linha = 0 
coluna = 0

def geradorIndices(quant_numeros_linha):
	flag = True
	while(flag):
		index_numeros_linha = rd.sample(range(0, 10), quant_numeros_linha)
		index_numeros_linha.sort()
		for i in range(len(index_numeros_linha) - 3):
			if index_numeros_linha[i] + 1 == index_numeros_linha[i + 1] == index_numeros_linha[i + 2] - 1 == index_numeros_linha[i + 3] - 2:
				break
		else:
			return index_numeros_linha

def gerarListaIndices(lista_quant_numeros_linha):
	lista_index_numeros_linha = []
	for i in range(len(lista_quant_numeros_linha)):
		index_numeros_linha = geradorIndices(lista_quant_numeros_linha[i])
		index_numeros_linha.sort()
		lista_index_numeros_linha.append(index_numeros_linha)		
	return lista_index_numeros_linha


def verificacaoColunaQuant(lista_index_numeros_linha):
	for i in range(10):
		quant_sum = sum(x.count(i) for x in lista_index_numeros_linha)
		# print(quant_sum)
		if(quant_sum > 6):		
			return True		
	return False

def gerarListaVerificadas(lista_quant_numeros_linha):
	flag = True
	while(flag):
		lista_index_numeros_linha = gerarListaIndices(lista_quant_numeros_linha)
		flag = verificacaoColunaQuant(lista_index_numeros_linha)
	return lista_index_numeros_linha


def verificarSeqColuna(sequencia_coluna, lista_quant_numeros_linha):
	lista_final = []
	lista_final = gerarListaVerificadas(lista_quant_numeros_linha)
	flag = True
	while(flag):
		for i in range(len(sequencia_coluna) - 3):
			if sequencia_coluna[i]  == sequencia_coluna[i + 1] == sequencia_coluna[i + 2]  == sequencia_coluna[i + 3]:
				lista_final = gerarListaVerificadas(lista_quant_numeros_linha)
				# print("tem sequencia")
		flag = False
	return lista_final


def geradorDeDinheiro():
	lista_quant_numeros_linha = []
	lista_index_numeros_linha =[]
	lista_auxiliar_sequencia_coluna = []
	lista_verif_colunas = []
	bilhete_premiado = []
	sequencia_coluna=[]

	i = 0
	acumulador = 0
	linha = 0 
	coluna = 0


	for x in range(10):
		quant_numeros_totais_faltando = 50 - acumulador
		if(acumulador < 50):
			if(acumulador < 50 and (quant_numeros_totais_faltando <= 7) and (quant_numeros_totais_faltando >= 3)):
				quant_numeros_linha = rd.randint(3, quant_numeros_totais_faltando)
				lista_quant_numeros_linha.append(quant_numeros_linha)
				acumulador = quant_numeros_linha + acumulador
				break;
			else:
				if(acumulador >= 48):
					break
				else:
					quant_numeros_linha = rd.randint(3, 7)
					lista_quant_numeros_linha.append(quant_numeros_linha)
					acumulador = quant_numeros_linha + acumulador
		else:
			break

	quant_numeros_totais_faltando = 50 - acumulador;

	while(quant_numeros_totais_faltando > 0):
		i = rd.randint(0, (len(lista_quant_numeros_linha)-1))
		if(lista_quant_numeros_linha[i] < 7 and quant_numeros_totais_faltando > 0):
			lista_quant_numeros_linha[i] = lista_quant_numeros_linha[i] + 1
			quant_numeros_totais_faltando = quant_numeros_totais_faltando - 1


	lista_verif_colunas = []


	lista_index_numeros_linha = gerarListaVerificadas(lista_quant_numeros_linha)
	

	quant = 0
	for i in range(10):
		quant = sum(x.count(i) for x in lista_index_numeros_linha)
		lista_verif_colunas.append(quant)




	for x in range(10):
		for y in range(10):
			try:
				sequencia_coluna.append(lista_index_numeros_linha[y][x])
			except Exception as e:
				# print("Não Existe")
				pass
		
	lista_index_numeros_linha = verificarSeqColuna(sequencia_coluna, lista_quant_numeros_linha)
	for i in lista_index_numeros_linha:
		for x in i:
			if(linha > 0):
				aux = 1 + x + (linha * 10)
				bilhete_premiado.append(aux)
			else:
				aux = x + linha + 1
				bilhete_premiado.append(aux)
		
		linha += 1

	try:
		with open(nome_arquivo + ".txt") as file:
			for line in file:
				if((str(bilhete_premiado) + "\n") == line):
					# print("DEU IGUAL KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
					lista_index_numeros_linha = geradorDeDinheiro()
	except Exception as e:
		pass			
	return lista_index_numeros_linha



quant_bilhetes = input("Digite a quantidade de bilhetes: ")
nome_arquivo = input("Digite o nome do arquivo: ")

for quant_bilhe in range(int(quant_bilhetes)):
	lista_quant_numeros_linha = []
	lista_index_numeros_linha =[]
	lista_auxiliar_sequencia_coluna = []
	lista_verif_colunas = []
	bilhete_premiado = []
	sequencia_coluna=[]

	i = 0
	acumulador = 0
	linha = 0 
	coluna = 0
	lista_index_numeros_linha = geradorDeDinheiro()

	for i in lista_index_numeros_linha:
		for x in i:
			if(linha > 0):
				aux = 1 + x + (linha * 10)
				bilhete_premiado.append(aux)
			else:
				aux = x + linha + 1
				bilhete_premiado.append(aux)
		
		linha += 1

	bilhete_premiado.sort()
	
	# bilhete_premiado = [2, 3, 4, 6, 7, 9, 10, 11, 15, 16, 18, 19, 21, 22, 28, 29, 34, 35, 38, 41, 43, 46, 47, 48, 50, 51, 52, 53, 55, 57, 59, 63, 64, 66, 68, 73, 74, 75, 81, 82, 84, 85, 86, 88, 89, 92, 93, 95, 96, 97]
	# try:
	# 	with open(nome_arquivo + ".txt") as file:
	# 		for line in file:
	# 			print(line)
	# 			if((str(bilhete_premiado) + "\n") == line):
	# 				lista_index_numeros_linha = geradorDeDinheiro()
	# except Exception as e:
	# 	pass
	

	arquivo = open(nome_arquivo + ".txt", "a")
	arquivo.write("BILHETE " + str(quant_bilhe+1) + "\n")
	arquivo.write(str(bilhete_premiado) + "\n"+ "\n")
	# arquivo = open(nome_arquivo + ".txt", "a")
	# arquivo.write(str(bilhete_premiado) + "\n"+ "\n")
	# print(bilhete_premiado)