import sys
input = sys.stdin.readline
 
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
 
 
if __name__ == "__main__":
    input = sys.stdin.readline
 
    tc = inp()
    num = 0
 
    for _ in range(tc):
        command = input()
 
        if "+" in command:
            num += 1
        elif "-" in command:
            num -= 1
    
    print(num)