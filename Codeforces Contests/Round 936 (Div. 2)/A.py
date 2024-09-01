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

def solve(n, k):

    return n
       

if __name__ == "__main__":
    for tc in range(inp()):
        n = inp()
        arr = inlt()

        arr = sorted(arr)

        mid = ((n-1)//2)

        count = 0
        for i in range(mid, n-1):
            arr[i] += 1
            count += 1
            if arr[i] <= arr[i+1]:
                break
            if i == n-2 and arr[-1] < arr[-2]:
                count += 1
        
        if n == 1:
            count += 1

        print(count)

            

        

        


        
