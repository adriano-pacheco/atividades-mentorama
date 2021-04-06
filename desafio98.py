#Faça um programa que tenha uma função chamada contador(),
#que receba 3 parâmetros: inicio, fim e passo, e realize
#a contagem.

#Seu programa tem que contar 3 contagens através da
#função criada:

#a)de 1 até 10, de um em 1
#b)de 10 até 0, de 2 em 2
#c)uma contagem personalizada

def lin():
    print('~'*30)


def contador(inicio, fim, passo):
    lin()
    print(f'Contando do {inicio} até {fim}, de {passo} em {passo}.')
    if passo == 0:
        passo = 1

    if passo < 0:
        passo = passo*-1
        
    if inicio > fim:
        print(f'Contando de ini')
        while inicio >= fim:
            print(inicio, end=' ')
            inicio = inicio - passo
            
    else:
        while fim >= inicio:
            
            print(inicio, end=' ')
            inicio = inicio + passo
            
    print('FIM!')
    lin()
        

def pergunta():
    inicio = int(input('Digite o primeiro valor: '))
    fim = int(input('Digite o segundo valor: '))
    passo = int(input('Digite o contador: '))
    lin()
    print(f'Contando do {inicio} até {fim}, de {passo} em {passo}.')
    if passo == 0:
        passo = 1

    if passo < 0:
        passo = passo*-1
        
    if inicio > fim:
        while inicio >= fim:
            print(inicio, end=' ')
            inicio = inicio - passo
            
    else:
        while fim >= inicio:
            
            print(inicio, end=' ')
            inicio = inicio + passo
            
    print('FIM!')
    lin()

contador(1,10,0)
pergunta()