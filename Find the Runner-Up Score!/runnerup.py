if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    array = list(arr)
    array = sorted(array)
    array = sorted(array)
    max_ele = max(array)
    second_max = max_ele
    i = 0
    for i in range(len(array)):
        if array[i] == max_ele:
            print(array[i - 1])
            exit()
