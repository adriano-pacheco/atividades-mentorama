#Faça um programa que tenha uma função chamada 
# maior(), que receba vário parâmetros com valores inteiros.

#Seu programa tem que analizar os valores e dizer qual deles é maior.
def lin():
    print('-='*30)

def maior(*num):
    cont = 0
    maior2 = 0 
    lin()
    print('A  lista de numeros são ...' ) 
    for valor in num:         
        cont += 1
        print(valor,end=' ')
        if valor > maior2:
            maior2 = valor
    print()
   
    print(f'O maior numero nessa lista é {maior2}, e a quantidade de numeros são {cont} ')
    lin()

maior(10,20,50,0,60,81)
maior(10,1)
maior(10,20,83,81)
maior(10,25)
maior(0)



