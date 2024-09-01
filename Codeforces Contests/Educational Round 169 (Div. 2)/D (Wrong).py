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

from collections import deque, defaultdict

def solve(arr, x, y):
    q = deque([(x, 0)])
    visited = set()
    visited.add(x)

    while q:
        curr, cost = q.popleft()

        if curr == y:
            return cost

        for portal in arr[curr-1]:
            for option in paths[portal]:
                if option not in visited:
                    visited.add(option)
                    q.append((option, cost + abs(option - curr)))

    return -1


if __name__ == "__main__":
    for tc in range(inp()):
        n, q = invr()
        arr = inst()
        
        queries = []
        for _ in range(q):
            temp = init()
            queries.append(temp)
        
        paths = defaultdict(list)
        for city in range(1, n+1):
            paths[arr[city-1][0]].append(city)
            paths[arr[city-1][1]].append(city)


        for x, y in queries:
            if x == y:
                print(0)
            else:
                print(solve(arr, x, y))
        


        
        
        
            