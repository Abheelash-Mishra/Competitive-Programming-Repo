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


# def solve(grid):
#    pass


if __name__ == "__main__":
    for _ in range(inp()):
        n = inp()
        if n % 2 == 0:
            print("NO")
        else:
            print("YES")
    





    