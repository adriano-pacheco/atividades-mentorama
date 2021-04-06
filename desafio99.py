#Faça um programa que tenha uma função chamada 
# maior(), que receba vário parâmetros com valores inteiros.

#Seu programa tem que analizar os valores e dizer qual deles é maior.


def maior(*num):
    #cont = 0
    #maior2 = 0 
    for valor in num:
        print(valor, end=' ')
       

maior(10,20,50,0)


