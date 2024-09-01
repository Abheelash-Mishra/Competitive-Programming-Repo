################ ---- Input Functions ---- ################
def inp():
    return(int(input()))
def inlt():
    return(list(map(str,input().split())))
def insr():
    s = input().lower()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

############ ---- End Of Input Functions ---- ############

# def solve(n):
    

if __name__ == "__main__":
    for tc in range(inp()):
        n, k = invr()

        mat = []

        for i in range(n):
            temp = inlt()
            for i in temp:
                mat.append(i)
        
        ans = []

        for i in range(0, n, k):
            temp = []
            for j in range(0, n, k):
                temp.append(mat[i][j])
            
            ans.append(temp)
        
        for i in range(len(ans)):
            for j in range(len(ans)):
                print(ans[i][j], end="")
            print()
        
            