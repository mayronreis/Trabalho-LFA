arquivo = open('quintupla.txt', 'r')
arquivo2 = open('palavras.txt', 'r')
saida = open('saida.txt', 'w')

palavras = arquivo2.readlines()
linhas = arquivo.readlines()

for i in range(len(linhas)):  # tira todos os \n e \r do arquivo
    aux = ''
    for j in range(len(linhas[i])):
        if (not ((linhas[i][j] == '\n') or (linhas[i][j] == '\r'))):
            aux = aux + linhas[i][j]
    linhas[i] = aux

for i in range(len(palavras)):  # tira todos os \n e \r do arquivo
    aux = ''
    for j in range(len(palavras[i])):
        if (not ((palavras[i][j] == '\n') or (palavras[i][j] == '\r'))):
            aux = aux + palavras[i][j]
    palavras[i] = aux

estados = linhas[0].split(',')
alfabeto = linhas[1].split(',')
inicial = linhas[-2]
regras = linhas[2:-2]

final = linhas[-1].split(',')
word = palavras[0]

tamAlfabeto = len(alfabeto)
tamEstado = len(estados)
tamFinal = len(final)
tamPalavra = len(palavras)

# for que preeche a matriz com '-'
for i in range(len(regras)):
    regras[i] = regras[i].split(',')
mat = [['-' for i in range(tamEstado)] for j in range(tamEstado)]

# Aqui e implementado as regras do automato
for k in range(len(regras)):
    for i in range(tamEstado):
        if estados[i] == regras[k][0]:
            for j in range(tamEstado):
                if estados[j] == regras[k][2]:
                    mat[i][j] = regras[k][1]


def Verifica(palavra, estado):
    if (len(palavra) == 0):
        for i in range(len(final)):
            if estado == final[i]:
                return bool(1)
        return bool(0)
    else:
        for i in range(tamEstado):
            if (estado == estados[i]):
                for j in range(tamEstado):
                    if mat[i][j] == palavra[0]:
                        return Verifica(palavra[1:], estados[j])


for p in range(tamPalavra):
    wordAux = palavras[p]
    saida.write(wordAux)
    print(Verifica(wordAux, inicial))
    if (Verifica(wordAux, inicial)):
        saida.write(' - Aceita \n')
    else:
        saida.write(' - Rejeita \n')
