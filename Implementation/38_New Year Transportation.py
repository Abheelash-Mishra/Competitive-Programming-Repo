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

def solve():

    return


if __name__ == "__main__":
    n, idx = invr()
    arr = inlt()

    i = 0
    ans = "NO"

    while i <= n-1:
        if i == idx-1:
            ans = "YES"
            break
        
        if i > len(arr) - 1:
            break

        # print(i)
        i += arr[i]
    
    print(ans)

        


        
