# chute o numero
import random

valor_aleatorio = random.randint(1, 10)
acertou = False

while not acertou:  # enquanto não acertou
    chute = int(input("Escolha um número entre 1 a 10: "))

    if chute > valor_aleatorio:
        print("Chute foi maior que o valor gerado.")
    elif chute < valor_aleatorio:
        print("Chute foi menor que o valor gerado.")
    else:  # se acertou
        acertou = True
        print("Você acertou!")