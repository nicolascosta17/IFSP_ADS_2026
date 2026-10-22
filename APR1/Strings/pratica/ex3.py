"""Escreva um programa que verifique se duas strings fornecidas pelo
usuário são iguais e mostre o total de caracteres de cada uma delas.
Diferencie letras maiúsculas das minúsculas.
"""

palavraUm = input("Digite a primeira palavra: ")
palavraDois = input("Digite a segunda palavra: ")
p1 = 0
p2 = 0

if palavraUm == palavraDois:
    print(f"As duas palavras são iguais: 1-{palavraUm} e 2-{palavraDois}")
    for letra in palavraUm:
        p1+=1
    for letra in palavraDois:
        p2+=1
    print(f"Total de letras: 1- {p1} Letras e 2- {p2} Letras")
else:
    print(f"As palavras são diferentes: 1-{palavraUm} e 2-{palavraDois}")
    for letra in palavraUm:
        p1+=1
    for letra in palavraDois:
        p2+=1
    print(f"Total de letras: 1- {p1} Letras e 2- {p2} Letras")