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
    maxSum = float('-inf')
    currentSum = 0
    start_idx = 0
    end_idx = 0
    
    for i in range(n):
        currentSum += arr[i]
        end_idx = i
        
        if currentSum > maxSum:
            maxSum = currentSum
        
        if currentSum < 0:
            currentSum = 0
            start_idx = i+1
    
    return maxSum, start_idx, end_idx
       

if __name__ == "__main__":
    for tc in range(inp()):
        n, k = invr()
        arr = inlt()

        modulo = (10**9)+7

        summ, s_idx, e_idx = maxSubArray(arr, n)
        total_sum = summ

        for i in range(k):
            if summ <= 0:
                arr.insert(s_idx, 0)
            else:
                arr.insert(s_idx, summ)

            total_sum = total_sum + summ
            summ = total_sum

            
            e_idx += 1
            n += 1
        
        ans = sum(arr) % modulo

        print(ans)

            

        

        


        
