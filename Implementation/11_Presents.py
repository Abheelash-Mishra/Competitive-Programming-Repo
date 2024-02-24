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

    res = [0 for i in range(n)]

    for i in range(len(arr)):
        res[arr[i] - 1] = i + 1

    for i in res:
        print(i, end = " ")
        



    
