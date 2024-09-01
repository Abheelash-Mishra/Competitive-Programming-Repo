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


def solve(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return "YES"
    
    if b % 2 != 0:
        b = b % 2
    
    if 2*b <= a and (a - 2*b) % 2 == 0:
        return "YES"
    
    return "NO"


if __name__ == "__main__":
    for tc in range(inp()):
        a, b = invr()
        print(solve(a, b))

        
        
        


        
        
        
            