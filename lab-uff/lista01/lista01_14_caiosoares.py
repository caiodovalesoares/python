# Nome: Caio do Vale Soares
# Data: 02/11/2024
# Programa que analisa 90 bois e escreve o boi mais pesado e o boi mais leve entre eles

#variáveis
num_bois = 90
mais_gordo = 0
mais_magro = float('inf')
id_mais_gordo = 0
id_mais_magro = 0

#lendo peso e identificação dos bois
for i in range(num_bois):
    id_boi = int(input("Digite o número de identificação do boi: "))
    peso_boi = float(input("Digite o peso do boi: "))

    if peso_boi > mais_gordo:
        mais_gordo = peso_boi
        id_mais_gordo = id_boi

    if peso_boi < mais_magro:
        mais_magro = peso_boi
        id_mais_magro = id_boi

#resultado
print("Boi mais gordo: ID =", id_mais_gordo, ", Peso =", mais_gordo)
print("Boi mais magro: ID =", id_mais_magro, ", Peso =", mais_magro)

#responda: se houver dois ou mais bois com o mesmo peso, maior que todos os demais, este algoritmo escreverá o número de qual deles?
#resposta: caso dois bois tenham o mesmo peso e sejam maiores que os demais, o meu algoritmo escreverá o número apenas do primeiro deles, pois o comando if peso_boi > mais_gordo só vai ser ativado quando um boi registrar um peso maior que o que está guardado na variável. como eles teriam o mesmo peso, esse comando não seria ativado.