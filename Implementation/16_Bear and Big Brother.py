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
    limak, bob = invr()

    years = 0
    while limak <= bob:
        limak *= 3
        bob *= 2
        years += 1
    
    print(years)
        