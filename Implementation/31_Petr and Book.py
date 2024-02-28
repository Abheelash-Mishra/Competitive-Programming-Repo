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


def solve(arr, pages):
    pages_read = 0

    n = len(arr)
    idx = 0

    while pages_read < pages:
        pages_read += arr[idx]

        if pages_read >= pages:
            break

        if idx == n-1:
            idx = 0
        else:
            idx += 1
    
    # print(pages_read)
    return idx + 1
    

if __name__ == "__main__":
    pages = inp()
    rate = inlt()
        
    print(solve(rate, pages))