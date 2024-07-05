import random

print(f"{'*' * 10} LANÇADOR DE DADOS {'*' * 10}")
jogar = True

try:
    while jogar:
        lados = int(input("Número de lados do dado: "))
        giro = random.randint(1, lados)
        print(f"Saída: {giro}")
        print(""" Novo lançamento?
            [1] - SIM
            [2] - NÃO""")
        nova_jogada = int(input("> "))
        if nova_jogada != 1:
            jogar = False
            print("Encerrando")
except ValueError:
    print("Valor inválido. Programa encerrado.")
