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

import math

def is_perfect_square(x):
    root = int(math.sqrt(x))
    return root * root == x

def check_beautiful_matrix(n, s):
    if not is_perfect_square(n):
        return "No"
    
    root = int(math.sqrt(n))
    grid = [[-1 for _ in range(root)] for _ in range(root)]

    for i in range(root):
        for j in range(root):
            grid[i][j] = int(s[(i*root) + j])
    
    oneSum = 0
    for i in [0, root-1]:
        for j in range(root):
            oneSum += grid[i][j]
            if grid[i][j] == 0:
                return "No"
            
    for j in [0, root-1]:
        for i in range(root):
            oneSum += grid[i][j]
            if grid[i][j] == 0:
                return "No"
    
    total = 0
    for row in grid:
        total += sum(row)

    if total != oneSum - 4:
        return "No"
    
    return "Yes"


if __name__ == "__main__":
    for tc in range(inp()):
        n = inp()
        binary = input()

        print(check_beautiful_matrix(n, binary))
        
        
        


        
        
        
            