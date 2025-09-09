import math

dados = [10, 12, 23, 23, 16, 23, 21, 16]

media = sum(dados) / len(dados)
soma_quadrados = sum((x - media) ** 2 for x in dados)
desvio_padrao = math.sqrt(soma_quadrados / len(dados))

print(f"Média: {media}")
print(f"Desvio Padrão: {desvio_padrao}")
