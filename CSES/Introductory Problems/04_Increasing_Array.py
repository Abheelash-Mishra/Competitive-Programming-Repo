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
    n = inp()
    arr = init()
    moves = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            moves += arr[i-1] - arr[i]
            arr[i] = arr[i-1]
    
    print(moves)
    