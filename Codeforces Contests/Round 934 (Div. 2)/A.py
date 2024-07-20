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

def solve(n, k):
    if k >= n - 1:
        return 1
    
    # If Dominater can destroy fewer bridges than the number of islands, Everule can reach all islands
    # except for those directly connected to island 1
    return n
       

if __name__ == "__main__":
    for tc in range(inp()):
        n, k = invr()

        print(solve(n, k))
            

        

        


        
