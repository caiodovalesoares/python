# Nome: Caio do Vale Soares
# Data: 01/11/2024
# Programa que lê o nome e preço de produtos, além de informar o mais caro deles

maiorPreco = 0
produto = str(input('Digite o nome do produto: '))
while produto != "xxx":
    preco = int(input('Digite o preço do produto: '))
    if maiorPreco < preco: #aqui eu determinei o que acontece caso o programa leia o produto mais caro
        maiorPreco = preco
        maisCaro = produto
    produto = str(input('Digite o nome do produto: '))
else:
    print('Produto mais caro da loja: ', maisCaro)