# Lista de listas dos Alunos

alunos = [['sc134778', 'Elaine Silva', 'elaina@gmail.com'],
          ['sc134534', 'Mario Sergio', 'mario@gmail.com'],
          ['sc233555', 'Luciana Maria', 'luma@gmail.com']]

# Local e nome onde será criado o arquivo
nome = './Dados_aluno.txt'
# Variável que abre o arquivo da variável 'nome' que permite escrever no arquivo
ref_arq = open(nome, 'w')

# Percorre as lista dos alunos
for i in range(len(alunos)):
    # Cria uma variável string vazia
    registro_aluno = ''
    # Percorre os elementos da lista dentro da lista
    for j in range(len(alunos[i])):
        # Adiciona a string 'registro_aluno' os elementos das listas 
        # dentro da lista e adiciona um ';' no final de cada
        registro_aluno += alunos[i][j] + '; '
    # Divide a linha após acabar os elementos da lista dentro da lista
    registro_aluno += '\n'
    # escreve no arquivo os dados da variável 'registro_aluno'
    ref_arq.write(registro_aluno)
"""
for linha in ref_arq:
    lista = linha.split()
    print(lista)
"""
