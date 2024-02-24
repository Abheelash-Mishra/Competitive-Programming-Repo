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
    n, k = invr()

    for i in range(k):
        if n%10 == 0:
            n = n//10
        else:
            n -= 1
    
    print(n)
        