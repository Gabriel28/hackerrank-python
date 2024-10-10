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