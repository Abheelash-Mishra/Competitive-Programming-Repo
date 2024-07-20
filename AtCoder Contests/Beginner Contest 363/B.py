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


if __name__ == "__main__":
    # for tc in range(inp()):
    n, t, p = invr()
    arr = inlt()

    days = 0

    arr.sort(reverse = True)

    ans = t - arr[p-1]

    if ans < 0:
        print(0)
    else:
        print(ans)
        
            