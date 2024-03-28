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

def solve(arr, n):

    return

if __name__ == "__main__":
    for tc in range(inp()):
        n, m, k = invr()

        left = inlt()
        right = inlt()

        count = 0

        for i in range(n):
            for j in range(m):
                if left[i] + right[j] <= k:
                    count += 1

        print(count)

        


        
