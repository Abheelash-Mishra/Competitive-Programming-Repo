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

def solve(arr, n):
    if n > 2:
        return "NO"
    
    if arr[0] + 1 == arr[1]:
        return "NO"
    
    return "YES"

if __name__ == "__main__":
    for tc in range(inp()):
        n = inp()
        arr = inlt()

        print(solve(arr,n))
        
        
        
        
            