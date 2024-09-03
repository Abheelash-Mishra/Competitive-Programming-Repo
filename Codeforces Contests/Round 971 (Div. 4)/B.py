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
    for tc in range(inp()):
        n = inp()

        grid = []
        for i in range(n):
            grid.append(input())

        res = []
        for i in range(n-1, -1, -1):
            for j in range(4):
                if grid[i][j] == "#":
                    res.append(j+1)
                    break
        
        print(*res)



