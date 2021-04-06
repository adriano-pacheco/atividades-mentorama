#faça um programa que tenha a função chamada escreva()
# que receba um texto qualquer como parâmetro 
# e mostre uma mensagem com o tamanho adáptvel.

def lin(quantidade):
    print('~'*len(quantidade))


def escreva(txt):
    lin(txt)
    print(txt)
    lin(txt)


escreva('Helo')
escreva('Como é fácil aprender com o Guanabara!')
escreva('Python é muito bom')
escreva('Essa foi fácil')