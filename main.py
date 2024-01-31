from pessoa import calculo_idade



nome = input('cumé c chama?')
ano = input('qual o ano do seu nascimento?')

idade = calculo_idade(ano)

print('seu nome é', nome, 'e tem', idade, 'anos de idade.')