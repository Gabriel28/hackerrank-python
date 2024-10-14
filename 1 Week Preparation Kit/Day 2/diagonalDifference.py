def diagonal_diff(arr):

    # Diagonal Diff
    #
    # -------------
    #| 1 | 2 | 3 |  A esquerda é composta pelos elementos arr[0][0], arr[1][1], arr[2][2] = 1, 5, 9 = 15
    # -------------  A direita é composta pelos elementos arr[0][2], arr[1][1], arr[2][0] = 3, 5, 7 = 15
    #| 4 | 5 | 6 |
    # -------------  O resultado deve ser a diferença absoluta entre as somas das diagonais.
    #| 7 | 8 | 9 |
    # -------------
    #

    n = len(arr)
    left_sum = 0
    right_sum = 0

    for i in range(n):
        left_sum += arr[i][i]
        right_sum += arr[i][n - i - 1]

    print(abs(left_sum - right_sum))

if __name__ == '__main__':
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    diagonal_diff(a)
