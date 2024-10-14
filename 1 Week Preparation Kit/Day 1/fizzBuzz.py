#
# Desafio de introdução - FizzBuzz
#
# Primeiro passo, devemos criar um loop para simular os inputs
# Segundo passo, devemos criar a regra:
# Se é multiplicador de 3 e de 5, deve imprimir "FizzBuzz"
# Se for multiplicador de 5 mas não de 3, deve imprimir "Buzz"
# Se for multiplicador de 3 mas não de 5, deve imprimir "Fizz"
# Não satisfazendo nenhuma das condições devemos retornar o N

def fizz_buzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

if __name__ == '__main__':
    fizz_buzz()
