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
    ans = 0

    ans += n // 4
    n = n % 4
    ans += n // 2

    return ans

if __name__ == "__main__":
    for tc in range(inp()):
        n = inp()
        print(solve(n))
        
            