################ ---- Input Functions ---- ################
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def inpsl():
    return(list(map(str,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

############ ---- End Of Input Functions ---- ############

def solve(arr):
    count = 0

    for i in range(n):
        for j in range(m-1, m):
            if arr[i][j] == "R":
                arr[i][j] == "D"
                count += 1
    
    for i in range(n-1, n):
        for j in range(m):
            if arr[i][j] == "D":
                arr[i][j] == "R"
                count += 1

    return count
    

if __name__ == "__main__":
    for tc in range(inp()):
        n, m = invr()

        arr = []

        for i in range(n):
            temp = insr()
            arr.append(temp)
        
        print(solve(arr))
