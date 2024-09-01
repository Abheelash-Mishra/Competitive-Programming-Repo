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

def solve(intervals, n, s, m):
    if intervals[0][0] >= s or m - intervals[n-1][1] >= s:
        return "YES"
    
    for i in range(n-1):
        if intervals[i+1][0] - intervals[i][1] >= s:
            return "YES"
    
    return "NO"

if __name__ == "__main__":
    for tc in range(inp()):
        n, s, m = invr()

        intervals = []
        for i in range(n):
            temp = inlt()
            intervals.append(temp)
        
        # print(intervals)

        print(solve(intervals, n, s, m))
        
        
            