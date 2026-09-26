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
            linhas.append(lin) 
            colunas.append(col)
            diagonal1.append(diag1)
            diagonal2.append(diag2)
            lin = 0 
            col = 0

    
print("Soma Linhas:")
for i in range(len(linhas)):
    print(linhas[i], end="; ")

print("")
print("Soma colunas:")
for i in range(len(colunas)):
    print(colunas[i], end="; ")

print("")
print("Soma Diagonal Principal:")
for i in range(len(diagonal1)):
    print(diagonal1[i], end="; ")

print("")
print("Soma Diagonal Secundária:")
for i in range(len(diagonal2)):
    print(diagonal2[i], end="; ")

i = 0
f = 0
v = 0
while i < len(matriz):
    if linhas[i] == colunas[i] == diagonal1[i] == diagonal2[i]:
        f+=1
    else:
        v+=1
        break
    i+=1

print("")
if v == 0:
    print("Essa Matriz Forma um quadrado mágico!")
else:
    print("Essa Matriz NÃO Forma um quadrado mágico!")