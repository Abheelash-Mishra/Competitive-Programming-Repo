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

def solve(arr1, arr2):
    l, r = arr1[0], arr1[1]
    L, R = arr2[0], arr2[1]

    rooms = [0 for x in range(101)]

    for i in range(l, r+1):
        rooms[i] += 1
    
    for i in range(L, R+1):
        rooms[i] += 1

    if r < L or l > R:
        return 1
    
    # print(rooms)

    locks = 0
    for i in range(1, len(rooms)):
        if rooms[i] == 2 and rooms[i-1] != 0:
            locks += 1
        elif rooms[i] == 1 and rooms[i-1] == 2:
            locks += 1
    
    return locks

if __name__ == "__main__":
    for tc in range(inp()):
        arr1 = inlt()
        arr2 = inlt()

        print(solve(arr1, arr2))
        
        
        
        
            