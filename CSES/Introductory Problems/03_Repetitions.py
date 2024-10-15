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


if __name__ == "__main__":
    maxi = float("-inf")
    count = 0
    s = input()

    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            count += 1
        else:
            maxi = max(maxi, count + 1)
            count = 0

    maxi = max(maxi, count + 1)
    
    print(maxi)
    