#Crie um programa que leia o nome, sexo e idade
#de varias pessoas, guardando os dados de cada 
#pessoa em um dicionario e todos os dicionaris em uma lista.
#No final mostre:

pessoas = dict()
listaPessoas = list()
resposta = "s"

while resposta =="s":
    pessoas['nome'] = str(input('Insira o nome: '))
    pessoas['sexo'] = str(input('Qual o sexo: '))
    pessoas['idade'] = int(input('Qual a idade: '))
    listaPessoas.append(pessoas.copy())
    resposta = str(input('Deseja continuar s/n: '))

#a)Quantidade de pessoas que foram cadastradas
pessoasCadastradas = len(listaPessoas)
print(f'A quantidade de pessaos ccadastradas são {pessoasCadastradas}')
#b)A média de idade
media = 0
for cont in pessoas:
    media = media + cont
#c)Uma lista com as mulheres
#d)Uma lista de pessoas com idade acima da média

