s = 0                                        # Inicia a soma em 0
for num in range(1, 501):                    # Vai de 1 até 500
    if num % 2 != 0:                         # Verifica se é ímpar
        if num % 3 == 0:                     # E também se é múltiplo de 3
            s += num                         # Se for, soma à variável 's'
print("A soma dos múltiplos é: {}.".format(s))  # Mostra o resultado da soma