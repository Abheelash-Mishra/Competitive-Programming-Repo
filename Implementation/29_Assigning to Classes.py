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

def solve(arr):
    n = len(arr)//2

    return arr[n] - arr[n-1]
    

if __name__ == "__main__":
    for tc in range(inp()):
        split = inp()

        arr = inlt()
        arr = sorted(arr)

        print(solve(arr))
