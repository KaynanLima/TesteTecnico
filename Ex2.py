VALOR = int(input("Insira um valor para conferir se este está na sequência de Fibonacci: "))
SOMA = 0
MENOR = 0
MAIOR = 1
CONFERIDOR = 0

if VALOR == MENOR or VALOR == MAIOR:
    print("\nO valor inserido ESTÁ presente na Sequência de Fibonacci")
    CONFERIDOR = 1
else:
    while (MAIOR < VALOR):
        SOMA = MENOR + MAIOR
        MENOR = MAIOR
        MAIOR = SOMA
        if MAIOR == VALOR:
            print("\nO valor inserido ESTÁ presente na Sequência de Fibonacci")
            CONFERIDOR = 1

if CONFERIDOR == 0:
    print("\nO valor inserido NÃO ESTÁ presente na Sequência de Fibonnacci")