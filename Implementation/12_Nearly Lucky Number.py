################ ---- Input Functions ---- ################
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

############ ---- End Of Input Functions ---- ############


if __name__ == "__main__":
    n = input()
    
    count = 0

    for i in n:
        if i == "4" or i == "7":
            count += 1

    if count == 4 or count == 7:
        print("YES")
    else:
        print("NO")
        



    
