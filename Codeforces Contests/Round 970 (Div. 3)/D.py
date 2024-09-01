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

def solve(n, per, white):
    result = [-1] * n
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            cycle = []
            count = 0
            idx = i
            
            while not visited[idx]:
                visited[idx] = True
                cycle.append(idx)
                if white[idx] == "0":
                    count += 1
                idx = per[idx] - 1
                
            for index in cycle:
                result[index] = count
    
    return result

if __name__ == "__main__":
    for tc in range(inp()):
        n = inp()
        per = init()
        white = input()

        res = solve(n, per, white)
        for r in res:
            print(r, end=" ")
        print()



