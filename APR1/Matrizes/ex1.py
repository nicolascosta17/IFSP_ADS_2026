def soma(x, y):
    soma = x + y
    return soma

def subtracao(x, y):
    subtracao = x - y
    return subtracao
    
def multiplicacao(x, y):
    multiplicacao = x * y
    return multiplicacao

def divisao(x, y):
    divisao = x/y
    return divisao

def porcentagem(x):
    valor = int(input("Digite a porcentagem desejavel: "))
    porcentagem = x * (valor / 100)
    desconto = x - porcentagem
    print(desconto)

########PGM PRINCIPAL###########
num1 = float(input("Entre com o primeiro valor: "))

porcentagem(num1)
