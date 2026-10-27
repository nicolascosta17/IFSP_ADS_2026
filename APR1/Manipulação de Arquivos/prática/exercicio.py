'''Crie um arquivo denominado “estudantes.txt” que contém uma
linha para cada aluno de uma turma de estudantes. O nome de
cada estudante está no início da cada linha e é seguido pelas
suas notas. Com esse arquivo faça:'''

'''a) Uma função que retorna o nome do estudante que possui mais de 6 notas;
b) Uma função que calcula a média das notas e imprime o nome e a média de cada
estudante;
c) Uma função que calcula a nota mínima e máxima de cada estudante e imprima o
nome de cada aluno junto com a sua maior e a menor nota.
'''

nome_notas = [['joao', 10, 15, 20, 30, 40], 
              ['pedro', 23, 16, 19, 22],
              ['suzana', 8, 22, 17, 14, 32, 17, 24, 21, 2, 9, 11, 17],
              ['gisela', 12, 28, 21, 45, 26, 10],
              ['joao', 14, 32, 25, 16, 89]]

nome = './notas_alunos.txt'
req_arq = open(nome, 'w')

def estudantesSeisNotas(estudantes):
    for alunos in estudantes:
        if len(estudantes[alunos]) >= 7:
            print("Aluno valido")

estudantesSeisNotas(nome_notas)
