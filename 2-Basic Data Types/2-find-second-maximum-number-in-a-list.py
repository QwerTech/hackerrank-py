if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = sorted(arr)
    first = arr.pop()
    while arr:
        val = arr.pop()
        if val != first:
            break
    print(val)
