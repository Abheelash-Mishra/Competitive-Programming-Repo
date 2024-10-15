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
    arr = init()
    sett = set([x for x in range(1, n+1)])

    for n in arr:
        sett.remove(n)
    
    print(sett.pop())