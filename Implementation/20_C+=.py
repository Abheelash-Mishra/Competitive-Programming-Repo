################ ---- Input Functions ---- ################
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

############ ---- End Of Input Functions ---- ############


if __name__ == "__main__":
    for tc in range(inp()):
        a, b, n = invr()
        
        count = 0
        sum = 0

        while sum <= n:
            if a > b:
                b += a
                count += 1
                sum = b
                # print(a,b)
            else:
                a += b
                count += 1
                sum = a
                # print(a,b)
            if sum > n:
                break
        
        print(count)