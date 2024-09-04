STRING = input("Insira uma string de até 100 caracteres para ser invertido: ")
INVERTIDO = ""
i = 0
try:
    while (i < 100):
        i = i + 1
        print(STRING[-i], end="")
except:
    print("")