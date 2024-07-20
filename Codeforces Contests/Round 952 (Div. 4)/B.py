################ ---- Input Functions ---- ################
def inp():
    return(int(input()))
def inlt():
    return(list(map(str,input().split())))
def insr():
    s = input().lower()
    return(list(s[:len(s)]))
def invr():
    return(map(str,input().split()))

############ ---- End Of Input Functions ---- ############

def maxSum(x, n):
    sum = 0
    operand = x

    while operand <= n:
        sum += operand
        operand += x

    return sum


if __name__ == "__main__":
    for tc in range(inp()):
        n = inp()

        summ = -1
        ans = -1
        for i in range(2, n+1):
            newSum = maxSum(i, n)

            if summ < newSum:
                ans = i
                summ = newSum

        print(ans)

        




    
        
                
