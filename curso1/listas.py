idades = [18, 22, 15, 50]

def verificaIdade(idade):
    if(idade >= 18):
        print(f'{idade} anos de idade, você pode dirigir')
    else:
        print(f'{idade} anos de idade, você ainda é menor de idade')

for i in idades:
    verificaIdade(i)