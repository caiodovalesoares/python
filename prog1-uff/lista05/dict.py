# Criando um dicionário
meu_dict = {
    "nome": "Alice",
    "idade": 25,
    "cidade": "São Paulo"
}

# Acessando valores
print(meu_dict["nome"])  # Saída: Alice

# Adicionando e atualizando itens
meu_dict["profissão"] = "Engenheira"
meu_dict["idade"] = 26

# Removendo itens
del meu_dict["cidade"]
idade = meu_dict.pop("idade")

# Iterando sobre o dicionário
for chave, valor in meu_dict.items():
    print(f"{chave}: {valor}")

# Usando métodos úteis
chaves = meu_dict.keys()
valores = meu_dict.values()
itens = meu_dict.items()
idade = meu_dict.get("idade", "Chave não encontrada")

# Limpando o dicionário
meu_dict.clear()

# Criando uma lista de dicionários
lista_dicts = [
    {"nome": "Alice", "idade": 25},
    {"nome": "Bob", "idade": 30},
    {"nome": "Charlie", "idade": 35}
]

# Removendo um dicionário da lista com base em uma condição
nome_a_remover = "Bob"
lista_dicts = [d for d in lista_dicts if d["nome"] != nome_a_remover]

# Imprimindo a lista atualizada
print(lista_dicts)

# Removendo um dicionário da lista de forma mais simples
for d in lista_dicts:
    if d["nome"] == nome_a_remover:
        lista_dicts.remove(d)
        break

# Imprimindo a lista atualizada
print(lista_dicts)