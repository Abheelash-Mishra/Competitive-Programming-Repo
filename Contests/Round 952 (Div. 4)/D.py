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


if __name__ == "__main__":
    for tc in range(inp()):
        n, m = invr()

        x = 0
        y = 0

        arr = []

        for _ in range(n):
            temp = input()
            arr.append(temp)

        # print(arr)

        for i in range(n):
            count = 0
            lastIdx = -1
            for j in range(m):
                if arr[i][j] == '#':
                    count += 1
                    lastIdx = j

            if count == 1:
                y = lastIdx+1
                break
        
        for j in range(m):
            count = 0
            lastIdx = -1
            for i in range(n):
                if arr[i][j] == '#':
                    count += 1
                    lastIdx = i

            if count == 1:
                x = lastIdx+1
                break

        print(x, y)
        

        



        




    
        
                
