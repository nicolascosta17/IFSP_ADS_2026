'''Na teoria dos sistemas, o elemento MINMAX de uma matriz é o maior elemento
da linha em que se encontra o menor elemento da matriz. Elabore um programa
que carregue uma matriz 4 x 5 com números reais, identifique e mostre o
MINMAX e a sua posição na matriz. '''

matriz = [[8, 3, 4], [1, 5, 9], [0, 7, 2]]

col = 0
lin = 0
maiorNumero = matriz[0][0]
menorNumero = matriz[0][0]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if maiorNumero < matriz[i][j]:
            posicaoLinhaMaior = lin            
            posicaoColunaMaior = col
            maiorNumero = matriz[i][j]
        elif menorNumero > matriz[i][j]:
            posicaoLinhaMenor = lin
            posicaoColunaMenor = col
            menorNumero = matriz[i][j]
        col+=1
    lin+=1
    col = 0

maiorNumeroDaLinhaComMenorNumero = matriz[posicaoLinhaMenor][0]
for i in range(len(matriz[posicaoLinhaMenor])):
    maiorNumeroDaLinhaComMenorNumero = maiorNumero
    if maiorNumero < matriz[posicaoLinhaMenor][i]:
        maiorNumero = matriz[posicaoLinhaMenor][i]
    

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="; ")

print("")
print(f"Maior Número da linha que tem o menor número: {maiorNumeroDaLinhaComMenorNumero}")
print(f"Maior elemento: {maiorNumero}. Linha: {posicaoLinhaMaior}. Coluna: {posicaoColunaMaior}")
print(f"Menor elemento: {menorNumero}. Linha: {posicaoLinhaMenor}. Coluna: {posicaoColunaMenor}")
