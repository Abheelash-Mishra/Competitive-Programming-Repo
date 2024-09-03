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
    for tc in range(inp()):
        a, b = invr()
        mini = float('inf')

        for c in range(a, b+1):
            calc = (c-a) + (b-c)
            mini = min(mini, calc)
        
        print(mini)



