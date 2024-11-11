# Nome: Caio do Vale Soares
# Data: 01/11/2024
# Programa que analisa 10 produtos de uma empresa e no fim escreve o vslor total gasto e a descrição do produto mais caro

#área das variáveis
total_gasto = 0
produto_mais_caro = ""
preco_mais_caro = 0

#aqui eu leio os dados de 10 produtos
for i in range(10):
    descricao = input("Digite a descrição do produto " + str(i+1) + ": ")
    preco_unitario = float(input("Digite o preço unitário do produto " + str(i+1) + ": "))
    quantidade = int(input("Digite a quantidade do produto " + str(i+1) + ": "))

    #calculando total gasto
    total_gasto += preco_unitario * quantidade

    #verificando produto mais caro
    if preco_unitario > preco_mais_caro:
        preco_mais_caro = preco_unitario
        produto_mais_caro = descricao

#resultados do programa
print("\nTotal gasto pela empresa: R$", total_gasto)
print("Produto mais caro:", produto_mais_caro, " - R$", preco_mais_caro)

