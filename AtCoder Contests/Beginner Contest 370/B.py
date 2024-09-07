################ ---- Input Functions ---- ################

def inp():
    return(int(input()))
def inst():
    return(list(map(str,input().split())))
def init():
    return(list(map(int,input().split())))
def insr():
    s = input().lower()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

############ ---- End Of Input Functions ---- ############


if __name__ == "__main__":
    # for tc in range(inp()):
    n = inp()

    arr = []
    for i in range(n):
        arr.append(init())

    element = 1
    for curr in range(1, n+1):
        if element >= curr:
            element = arr[element-1][curr-1]
        else:
            element = arr[curr-1][element-1]

    print(element)




