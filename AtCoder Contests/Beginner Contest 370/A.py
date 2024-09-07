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


# def solve(x, y, k):
    

#     return moves

if __name__ == "__main__":
    # for tc in range(inp()):
    l, r = invr()

    if (l == 1 and r == 1) or (l == 0 and r == 0):
        print("Invalid")
    elif l == 1:
        print("Yes")
    elif r == 1:
        print("No")




