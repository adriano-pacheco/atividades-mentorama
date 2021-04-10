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
    resposta = input('Deseja continuar s/n: ')


#a)Quantidade de pessoas que foram cadastradas
pessoasCadastradas = len(listaPessoas)
print(f'A quantidade de pessoas cadastradas são {pessoasCadastradas}')

#b)A média de idade
media = 0
for i in listaPessoas:
    media = media + i['idade']
media2 = media / pessoasCadastradas
print(f'A média de idade das pessoas cadastradas é {media2}')

#c)Uma lista com as mulheres
listM = []
for i in listaPessoas:
    if i['sexo'] == 'f':
        listM.append(i['nome'])
print(f'A lsita com as mulheres {listM}')
#d)Uma lista de pessoas com idade acima da média
acMedia = []
for i in listaPessoas:
    if i['idade'] > media2:
        acMedia.append(i['nome'])
print(f'As pessoas acima da idade média são : {acMedia}')

