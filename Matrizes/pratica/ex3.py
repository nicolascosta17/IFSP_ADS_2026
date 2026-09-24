'''Crie um programa que preencha uma matriz 3x3 de números inteiros e verifique
se essa matriz forma um quadrado mágico. Um quadrado mágico é formado
quando a soma dos elementos de cada linha é igual:
- à soma dos elementos de cada coluna da matriz;
- à soma dos elementos da diagonal principal;
- à soma dos elementos da diagonal secundária;

Por exemplo, veja um quadrado mágico de lado 3 cujas somas sempre são 15: 
    8 3 4
    1 5 9
    6 7 2
'''

matriz = []
linha = []
lin = 0
linhas = []
colunas = []
diagonal1 = []
diagonal2 = []
while lin < 3:
    print(f"Digite 3 números para a linha {lin}:")
    col = 0
    while col < 3:
        valor = int(input())
        linha.append(valor)
        col+=1
    matriz.append(linha)
    linha = []
    lin+=1

lin = 0
col = 0
diag1 = 0
diag2 = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        lin += matriz[i][j]
        col += matriz[j][i]
        diag1 = matriz[j][0] + matriz[j][1] + matriz[j][2]
        diag2 = matriz[j][2] + matriz[j][1] + matriz[j][0]
        if j == 2:
            linha.append(lin) 
            colunas.append(col)
            diagonal1.append(diag1)
            diagonal2.append(diag2)
            lin = 0 

print(lin)
print(linha)
print(colunas)
print(diagonal1)
print(diagonal2)

for i in range(len(matriz)):
    print(matriz[i], end="; ")
