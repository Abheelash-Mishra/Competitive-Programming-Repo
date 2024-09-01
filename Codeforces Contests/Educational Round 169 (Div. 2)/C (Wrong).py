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

def solve(arr, n, k):
    # print(arr)

    if k == 0:
        A = sum(arr[::2])
        B = sum(arr[1::2])

        return A - B

    for i in range(1, n, 2):
        if arr[i] + k <= arr[0]:
            arr[i] += k
            k = 0
        else:
            toAdd = arr[0] - arr[i]
            if toAdd <= k:
                k -= toAdd
                arr[i] += toAdd
    
    if k > 0:
        for i in range(0, n, 2):
            if arr[i] + k <= arr[0]:
                arr[i] += k
                k = 0
            else:
                toAdd = arr[0] - arr[i]
                if toAdd <= k:
                    k -= toAdd
                    arr[i] += toAdd

    # print(arr)

    A = sum(arr[::2])
    B = sum(arr[1::2])

    return A - B


if __name__ == "__main__":
    for tc in range(inp()):
        n, k = invr()
        arr = inlt()

        arr.sort(reverse=True)
        print(solve(arr, n, k))
        
        
        
        
            