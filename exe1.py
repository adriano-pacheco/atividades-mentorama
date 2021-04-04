pessoas = dict()
listaPessoas = list()
resposta = "s"
while resposta =="s":
    pessoas['nome'] = str(input('Insira o nome: '))
    pessoas['sexo'] = str(input('Qual o sexo: '))
    pessoas['idade'] = str(input('Qual a idade: '))
    listaPessoas.append(pessoas.copy())
    resposta = str(input('Deseja continuar s/n: '))
   
