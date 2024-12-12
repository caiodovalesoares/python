# Nome: Caio do Vale Soares
# Data: 11/12/24
# Programa que converte números arábicos menores que 4000 para romanos

#função que converte para números romanos
def int_para_romano(numero):
 #valores em romanos
 valores_decimais = {
 1000: "M",
 900: "CM",
 500: "D",
 400: "CD",
 100: "C",
 90: "XC",
 50: "L",
 40: "XL",
 10: "X",
 9: "IX",
 5: "V",
 4: "IV",
 1: "I"
 }
 
 resultado = ""
 while numero > 0:
    for valor_decimal, simbolo_romano in valores_decimais.items():
        while numero >= valor_decimal:
            resultado += simbolo_romano
            numero -= valor_decimal
 
 return resultado
 
def main():
 while True:
    try:
        #lendo o número
        numero = int(input("Informe um número inteiro (menor que 4000): "))
        if numero > 4000:
            print("Número inválido. Informe um número menor que 4000.")
            break
    except ValueError:
        print("Erro: valor não é um número inteiro.")
    #resultado
    print(int_para_romano(numero))
 
if __name__ == "__main__":
    main()