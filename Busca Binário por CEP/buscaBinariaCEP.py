from io import SEEK_SET
import os

path = input("Caminho do arquivo no seu computador: ") #Vai ler o arquivo .dat
try:
    resultado = os.stat(path).st_size
    arquivo = open("cep_ordenado.dat", "r")
    
except:
    print("Arquvo não encontrado no path")
    quit()

#tamanhoLinha = 300
qtdLinhas = resultado//300
CEP_usuario = int(input("Escreva o CEP (apenas os numeros): "))

def buscaBinariaCEP(inicio, fim, CEP_usuario): 
    meio = (inicio+fim)//2
    arquivo.seek(meio*300, SEEK_SET)
    linha = arquivo.readline()
    CEP_lista = int(linha[290:298])
    #print(CEP_lista)

    if(CEP_lista == CEP_usuario):
        print("CEP encontrado")
        linha = " ".join(linha.split())
        print(linha)
    elif(inicio>fim):
        print("CEP não encontrado ou não existe")
    elif(CEP_usuario < CEP_lista):
        fim = meio-1
        buscaBinariaCEP(inicio, fim, CEP_usuario)
    elif(CEP_usuario>CEP_lista):
        inicio = meio+1
        buscaBinariaCEP(inicio, fim, CEP_usuario)

buscaBinariaCEP(1, qtdLinhas, CEP_usuario)


