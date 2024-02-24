############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


if __name__ == "__main__":
    arr = inlt()
    arr = sorted(arr)

    print((arr[1] - arr[0]) + (arr[2] - arr[1]))
    
