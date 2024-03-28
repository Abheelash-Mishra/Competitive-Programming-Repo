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

def maxSubArray(arr, n):
    
    return 
       

if __name__ == "__main__":
    for tc in range(inp()):
        a, b, c = invr()

        if a < b < c:
            print("STAIR")
        elif a < b > c:
            print("PEAK")
        else:
            print("NONE")

            

        

        


        
