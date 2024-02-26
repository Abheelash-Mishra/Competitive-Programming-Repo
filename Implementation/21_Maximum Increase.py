################ ---- Input Functions ---- ################
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

############ ---- End Of Input Functions ---- ############


if __name__ == "__main__":
    n = inp()
    arr = inlt()

    count = 1
    max_count = 1

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            count += 1
        else:
            count = 1

        max_count = max(count, max_count)

    print(max_count)

    