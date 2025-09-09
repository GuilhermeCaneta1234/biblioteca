from random import choice
from time import sleep

choices_list = ["pedra", "papel", "tesoura"]
print("""
COMPUTADOR: Vamos jogar Pedra, Papel, Tesoura!
As regras são as seguintes:
- Papel vence Pedra e perde para Tesoura
- Pedra vence Tesoura e perde para Papel
- Tesoura vence Papel e perde para Pedra
""")

player_prompt = str(input("Você escolhe pedra, papel ou tesoura? \n")).lower()

print("JO")
sleep(0.50)
print("KEN")
sleep(0.5)
print("PÔ!!!")

def judge(computer, player):
    print(
    f"""
    Jogador: {player}
    Computador: {computer}
    """
    )

    # Verificação de entrada inválida
    if player not in choices_list:
        return print(f"{player} não é uma opção válida. Escolha pedra, papel ou tesoura!")

    # Condições de empate
    if computer == player:
        return print("Empate. Vamos jogar novamente!")

    # Regras do jogo
    if player == "pedra" and computer == "tesoura": # Pedra x Tesoura: Pedra
        return print("Pedra vence tesoura. Jogador ganhou.")
    if player == "tesoura" and computer == "pedra": # Tesoura x Pedra: Pedra
        return print("Pedra vence tesoura. Computador ganhou.")
    if player == "papel" and computer == "pedra": # Papel x Pedra: Papel
        return print("Papel vence pedra. Jogador ganhou.")
    if player == "pedra" and computer == "papel": # Pedra x Papel: Papel
        return print("Papel vence pedra. Computador ganhou.")
    if player == "papel" and computer == "tesoura": # Papel x Tesoura: Tesoura
        return print("Tesoura vence papel. Computador ganhou.")
    if player == "tesoura" and computer == "papel": # Tesoura x Papel: Tesoura
        return print("Tesoura vence papel. Jogador ganhou.")

# Escolha do computador
computer_choice = choice(choices_list)

# Chamada da função judge
judge(computer_choice, player_prompt)
