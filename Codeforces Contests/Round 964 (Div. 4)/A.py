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

if __name__ == "__main__":
    for tc in range(inp()):
        n = input()
        sum = 0

        for i in n:
            sum += int(i)
        
        print(sum)
        
        
        
            