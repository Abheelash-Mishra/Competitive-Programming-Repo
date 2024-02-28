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


def solve(x, y):
    if x == y:
        return 0
    
    if y % x != 0 or (y % 2 != 0 and y % 3 != 0):
        return -1
    
    factor = y // x
    moves = 0

    while factor % 2 == 0 or factor % 3 == 0:
        if factor % 2 == 0:
            factor = factor // 2
            moves += 1
        
        if factor % 3 == 0:
            factor = factor // 3
            moves += 1
        
    if factor != 1:
        return -1
    
    return moves
    

if __name__ == "__main__":
    x, y = invr()

    print(solve(x, y))
    