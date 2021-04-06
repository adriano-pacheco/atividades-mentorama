#Faça um programa que tenha como uma função 
#chamada area(), que receba as dimensões de 
#um terreno retangular (largura e comprimento)
#e mostre a área do terreno.
def lin():
    print('*'*30)


def area():
    lin()
    largura = int(input('Qual o tamanho da largura?: '))
    altura = int(input('Qual o tamanho da largura?: '))
    m2 = altura * largura
    print(f'A área do terreno é {m2}m²')
    lin()


area()