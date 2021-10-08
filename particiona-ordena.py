from io import SEEK_SET
import struct
import os

caminho = "cep.dat"
size_file = os.stat(caminho).st_size

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
tamanhoDaLinha = registroCEP.size
numeroDelinhas = size_file // registroCEP.size
numeroDivisoes = int(input("Numero de divisoes: "))
qtdLinhaPorDivisao = numeroDelinhas // numeroDivisoes

with open(caminho, "rb") as f:  # lendo arquivo
    for divisaoAtual in range(0, numeroDivisoes):
        listaTemp = []
        # faz o deslocamento do ponteiro do arquivo para a divisao pertinente
        f.seek(divisaoAtual * qtdLinhaPorDivisao * tamanhoDaLinha, SEEK_SET)
        line = f.readline(tamanhoDaLinha)

        i = 1
        while(i <= qtdLinhaPorDivisao) and len(line) > 0:
            # Gera tuplas com base na struct definida
            endereco = registroCEP.unpack(line)
            listaTemp.append(endereco)  # adicicona o endereco a lista
            line = f.read(tamanhoDaLinha)
            i += 1

        listaTemp.sort(key=lambda e: e[5])  # ordena o arquivo gerado
        with open("cep_ordenado{}.dat".format(divisaoAtual), "wb") as file:
            for endereco in listaTemp:
                file.write(registroCEP.pack(*endereco))
