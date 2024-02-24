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
    num = input()
    ans = ""
 
    if int(num[0]) >= 5 and int(num[0]) < 9:
        ans += str(9 - int(num[0]))
    else:
        ans += num[0]
 
    for i in range(1, len(num)):
        digit = int(num[i])
 
        if digit >= 5:
            digit = 9 - digit
        
        ans += str(digit)
    
    print(ans)