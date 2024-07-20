################ ---- Input Functions ---- ################
def inp():
    return(int(input()))
def inlt():
    return(list(map(str,input().split())))
def insr():
    s = input().lower()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

############ ---- End Of Input Functions ---- ############


if __name__ == "__main__":
    # for tc in range(inp()):
    n = inp()

    if n >= 0 and n <= 99:
        print(100 - n)
    elif n >= 100 and n <= 199:
        print(200 - n)
    elif n >= 200 and n <= 299:
        print(300 - n)
    elif n >= 300 and n <= 399:
        print(400 - n)
        
            