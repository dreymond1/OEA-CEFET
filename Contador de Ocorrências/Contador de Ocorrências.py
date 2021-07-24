
arquivoPath = input("Caminho do arquivo no seu computador: ") #Busca o arquivo no seu PC
try:
    with open(arquivoPath) as arquivoFinal: #Nomeia o path do arquivo de "arquivoFinal"
        conteudo = arquivoFinal.read() #Atribui a leitura do arquivo a "conteudo"
        
    
except:
    print("Arquvo não encontrado no path")
    quit()

letrasMaiusculas = 0
letrasMinusculas = 0
contDigitos = 0
espacoBranco = 0
quebraLinhas = 0
outraCoisa = 0

for i,j in enumerate(conteudo): #um looping que vai enumerar a quantidade de conteudo especificado
    if j.isupper():
        letrasMaiusculas += 1
    elif j.islower():
        letrasMinusculas += 1
    elif j in "0123456789":
        contDigitos += 1
    elif j == " ":
        espacoBranco += 1
    elif j == "\t":
        espacoBranco += 4
    elif j == "\n":
        quebraLinhas += 1
    else:
        outraCoisa += 1

print('''
Letras Maisculas: %d
Letras Minusculas: %d
Digitos de 0 a 9: %d
Espaços em branco: %d
Linhas quebradas: %d
Outra coisa: %d'''%(letrasMaiusculas, letrasMinusculas, contDigitos, espacoBranco, quebraLinhas, outraCoisa))
