def titulo(txt): #criando linha com texto
    print('_'*30)
    print(txt)
    print('_'*30)

def soma(a, b): #somando 2 numeros
    print('_'*30 )
    print(f'A = {a} e B = {b}')
    s = a + b 
    print(f'A soma A + B = {s}')
    print('_'*30)

def contador(*num): #inserindo varios numeros em uma tupla
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
    #isso cria uma tupla

def dobra(lst): #dobrando os valores de uma lista
    pos = 0
    while pos < len(lst):
        lst[pos]*= 2
        pos +=1
    
def soma2(*valores):#somando todos os valores de uma tupla
    s = 0
    for num in valores:
        s+= num
    print(f'Somando os valores {valores} temos {s}')


soma2(2,3,7,8,40,60)