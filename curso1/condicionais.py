idade = int(input('qual a sua idade?'))

def verificaIdade(idade):
    if(idade >= 18):
        print('voce está habilitado a dirigir')
    else:
        print('você ainda não é maior de idade')

verificaIdade(idade)