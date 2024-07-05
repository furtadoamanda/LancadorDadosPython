# Lançador de Dados em Python 🎲🐍

Projeto criado para praticar os conhecimentos em Python.  
Trata-se de um programa simples de lançamento de dados, em que o usuário informa o número de lados do dado que deseja lançar, podendo repetir quantos lançamentos forem necessários.  

```python
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
```
Inicialmente, é importado o módulo nativo 'random', que será usado mais tarde. É, ainda, exibida a mensagem de inicialização e definida a variável 'jogar' como `True`.  
O bloco `try` será explicado mais adiante.  
No bloco `while`, enquanto a variável 'jogar' for verdadeira, o programa continuará em execução. Nele, inicialmente é solicitado ao usuário que informe o número de lados do dado, sendo convertido o valor informado para o formato `int`.  
A variável 'giro' armazena o valor gerado pela função `random.randint(1, lados)`, a qual gera um valor aleatório entre 1 e o número de lados do dado. Importante pontuar que essa função é inclusiva nas duas extremidades, pelo que não é necessário utilizar 'lados + 1'. O uso da função 'randint' é o motivo da necessidade de importar o módulo 'random'.  
De imediato, o programa exibe a saída gerada pela função e, a seguir, pergunta ao usuário se ele deseja realizar um novo lançamento. A variável 'nova_jogada' converte em `int` a opção selecionada pelo usuário e, de acordo com o valor informado - caso não seja selecionada a opção de nova jogada -, o programa segue no laço while ou se encerra. O encerramento do programa se dá pela alteração do valor da variável 'jogar' para `False`, o que quebra o laço de repetição.  
Sobre o bloco `try`, este engloba todo o bloco de funcionamento do programa, para que, caso ocorra um 'ValueError', isto é, se o usuário inserir um valor que não seja um número inteiro, seja quando da variável 'lados' ou 'nova_jogada', o programa se encerrará com uma mensagem de erro e encerramento.