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


def solve(arr, queries, h, w):
    for r, c in queries:
        r -= 1
        c -= 1


        if arr[r][c] == 1:
            arr[r][c] = 0
        else:
            for j in range(c, -1, -1):
                if arr[r][j] == 1:
                    arr[r][j] = 0
                    break

            for j in range(c+1, w):
                if arr[r][j] == 1:
                    arr[r][j] = 0
                    break
            
            for i in range(r, -1, -1):
                if arr[i][c] == 1:
                    arr[i][c] = 0
                    break
            
            for i in range(r+1, h):
                if arr[i][c] == 1:
                    arr[i][c] = 0
                    break

    return sum([sum(i) for i in arr])

if __name__ == "__main__":
    # for tc in range(inp()):
    h, w, q = invr()

    arr = [[1 for i in range(w)] for j in range(h)]

    queries = []
    for i in range(q):
        queries.append(init())

    print(solve(arr, queries, h, w))




