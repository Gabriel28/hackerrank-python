def lonely_int(arr):
    arr.sort()

    for num in arr:
        if arr.count(num) == 1:
            print(num)

if __name__ == '__main__':
    lonely_int([2, 1, 1, 2, 3, 3, 7, 5, 7]) #Output deve ser 5