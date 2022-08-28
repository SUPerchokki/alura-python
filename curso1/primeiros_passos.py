def saudacao():
    nome = input('Qual o seu nome?')
    idade = input('Qual a sua idade?')
    print('seu nome é ', nome,' e sua idade é ', idade)
    
saudacao()

def saudacaoComParametro(nome,idade):
    print('seu nome é ', nome, ' sua idade é ', idade)

nome = input('qual seu nome?')
idade = input('qual a sua idade?')

saudacaoComParametro(nome, idade)