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

# def solve():
    
    

if __name__ == "__main__":
    for tc in range(inp()):
        n = inp()
        arr = inlt()

        for i in range(n):
            if arr[i] < 0:
                arr[i] *= -1

        print(sum(arr))
