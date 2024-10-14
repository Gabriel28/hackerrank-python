#
# Desafio - minMaxSum
#
# Primeiro passo, ordenar o array em ordem asc, array esse que terá 5 int e definir uma variável aux
# Segundo passo, criar um laço de repetição para somar os valores
# Para obter o valor máximo devemos subtraír o total - a última (maior) posição do array.
# Para obter o valor mínimo devemos subtraír o total - a primeira (menor) posição do array.
# Imprimir os valores

def min_max_sum_with_for(arr):
    arr.sort()
    total = 0
    for i in arr:
        total += i

    print (total - arr[4], total - arr[0])

def min_max_sum_alt(arr):
    arr.sort()
    total = sum(arr)
    print(total - max(arr), total - min(arr))

if __name__ == '__main__':
    min_max_sum_with_for([2, 7, 8, 1, 2])
    min_max_sum_alt([2, 7, 8, 1, 2])