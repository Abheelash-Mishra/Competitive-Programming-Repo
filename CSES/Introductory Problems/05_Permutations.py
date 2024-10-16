################ ---- Input Functions ---- ################

def inp():
    return(int(input()))
def inst():
    return(list(map(str,input().split())))
def init():
    return(list(map(int,input().split())))
def insr():
    s = input().lower()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

############ ---- End Of Input Functions ---- ############


if __name__ == "__main__":
    n = inp()
    arr = []

    if n == 1:
        print(1)
    elif n < 4:
        print("NO SOLUTION")
    elif n == 4:
        print("2 4 1 3")
    else:
        if n % 2 == 0:
            for x in range(n, 1, -2):
                arr.append(x)
            for x in range(n-1, 0, -2):
                arr.append(x)
        else:
            for x in range(n-1, 1, -2):
                arr.append(x)
            for x in range(n, 0, -2):
                arr.append(x)

        for x in arr:
            print(x, end=" ")
    
    