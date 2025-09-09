print("**********************************************************")
print("Bem vindo ao jogo de adivinhação ")
print("**********************************************************")

numero_secreto = 42
chute = int(input("Digite o seu número:"))
print ("Você digitou: ", chute)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    else:
        print("Você errou! O seu chute foi menor que o núemro secreto. ")

