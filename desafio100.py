from random import randint
#Faça um programa que tenha uma lista chamada
#numeros e duas funções chamadas sorteio()
#e somarPar(). A primeira função vai sortear 5 
#numeros e vai coloca-los dentro da lista e a 
#segunda função vai mostrar a soma entre todos os 
#numeors pares sorteados pela função anterior.

def lin ():
    print('~'*30)

numeros = list()

def sorteio(lista):
    cont = 0
    while cont < 5:
        lista.append(randint(1,10))
        cont += 1
#sorteio(numeros)

def somarPar(lista):
    sorteio(numeros)
    total = 0
    ehPar = list()
    lin()
    for num in lista:
        if num % 2 ==0:
            ehPar.append(num)
            total = total + num
    print(f'Numeros sorteados: {numeros}')       
    print(f'numeros pares {ehPar}!')
    print(f'A soma deles são {total}!')
    lin()


somarPar(numeros)
