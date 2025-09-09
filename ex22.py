s = 0                                 # Começa a soma com 0
for i in range(0, 6):                 # Repete 6 vezes (de 0 até 5)
    num = int(input("Digite um número: \n"))  # Pede um número inteiro ao usuário
    if num % 2 == 0:                  # Se o número for par
        s += num                      # Soma o número na variável 's'
print("Soma: {}.".format(s))         # Mostra a soma total
