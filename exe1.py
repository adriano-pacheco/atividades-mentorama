pessoas = dict()
listaPessoas = list()
resposta = "s"
idade = []
nomes = []
generos = []


while resposta =="s":
    pessoas['nome'] = str(input('Insira o nome: '))
    pessoas['sexo'] = str(input('Qual o sexo: '))
    pessoas['idade'] = int(input('Qual a idade: '))
    listaPessoas.append(pessoas.copy())
    resposta = str(input('Deseja continuar s/n: '))
   
for i in listaPessoas:
   # for n, s, a in i.items():
    nomes.append(pessoas['nome'].copy())
    generos.append(pessoas['sexo'].copy())
    idade.append(pessoas['idade'].copy())

print(idade)
print(nomes)
print(generos)