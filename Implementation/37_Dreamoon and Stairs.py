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


def solve(k):
        
    return 1


if __name__ == "__main__":
    n, m = invr()

    lower_bound = (n+1)//2

    ans = (lower_bound + m - 1)//m*m

    if ans > n:
        ans = -1
    
    print(ans)




        
        



    
 
    
    