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
    # for tc in range(inp()):
    n = inp()

    while n != 1:
        print(n, end = " ")

        if n % 2 == 0:
            n = n // 2
        else:
            n = (n*3) + 1

    print(1)