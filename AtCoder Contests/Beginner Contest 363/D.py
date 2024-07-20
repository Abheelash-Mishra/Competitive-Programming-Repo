################ ---- Input Functions ---- ################
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input().lower()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

############ ---- End Of Input Functions ---- ############

def solve(n):
    num = 0

    while n:
        temp = str(num)
        if temp == temp[::-1]:
            n -= 1
            p_num = int(temp)
        
        num += 1
    
    return num - 1

if __name__ == "__main__":
    # for tc in range(inp()):
    n = inp()
    print(solve(n))
        
            