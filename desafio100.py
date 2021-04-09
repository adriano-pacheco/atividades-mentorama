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
    lin()
    for cont in range (0,5):
        lista.append(randint(1,10))
    print(lista)
    lin()
sorteio(numeros)

#def somarPar(lista):
    #total = 0
    #lin()
    #print(f'Os numeros pares são:')
    #for num in lista:
     #   if num % 2 ==0:
      #      total = total + num
       #     print(f'{num}', end= '-') 

#    print(f'. E a soma deles são {total}!')
 #   lin()

    #print(f'Os numeros pares são {num} e \na soma total deles são {total}\n', end=' ')
    #print(f'A soma total da lista é {total}')


#numerinho = [0,5,17,12,14,15]
#somarPar(numerinho)

