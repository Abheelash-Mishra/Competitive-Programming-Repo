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

import heapq

if __name__ == "__main__":
    left, right = [], []
    while True:
        try:
            temp = input().split()
            heapq.heappush(left, int(temp[0]))
            heapq.heappush(right, int(temp[1]))
        except:
            break
    
    total = 0
    for _ in range(1000):
        total += abs(heapq.heappop(left) - heapq.heappop(right))
    
    print(total)
    