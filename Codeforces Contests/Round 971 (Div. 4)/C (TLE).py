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

from math import ceil

def solve(x, y, k):
    right = True
    moves = 0
    coords = [0, 0]

    x_lock, y_lock = coords[0] == x, coords[1] == y

    while True:
        if right and not x_lock:
            coords[0] += k
            if coords[0] == x:
                x_lock = True

        elif not right and not y_lock:
            coords[1] += k
            if coords[1] == y:
                y_lock = True

        moves += 1
        right = not right
        
        if coords[0] + k >= x and coords[1] + k >= y:
            break
    
    if x_lock and not y_lock:
        if right:
            moves += 1
        
        left = y - coords[1]
        moves += ceil(left / k)

    elif y_lock and not x_lock:
        if not right:
            moves += 1
        
        left = x - coords[0]
        moves += ceil(left / k)

    return moves

if __name__ == "__main__":
    for tc in range(inp()):
        x, y, k = invr()

        print(solve(x, y, k))




