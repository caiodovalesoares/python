# Nome: Caio do Vale Soares
# Data: 11/12/24
# Programa que enumera as subsequências não contínuas de uma dada sequência

import itertools

#função que calcula as possíveis sequências
def subsequencias_nao_contínuas(sequencia):
    if len(sequencia) < 2:
        raise ValueError("Sequência deve ter pelo menos 2 elementos")

    sequencia = tuple(sequencia) #convertendo para tupla
    subsequencias = []

    #gerando combinações
    for r in range(2, len(sequencia) + 1):
        for combo in itertools.combinations(sequencia, r):
            if not is_subsequencia_continua(combo, sequencia):
                subsequencias.append(combo)

    return subsequencias

def is_subsequencia_continua(combo, sequencia):
    idx_inicio = sequencia.index(combo[0])
    return combo == sequencia[idx_inicio:idx_inicio + len(combo)]

#resultado
sequencia = (1, 2, 3, 4)
print(subsequencias_nao_contínuas(sequencia))