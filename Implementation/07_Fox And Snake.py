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
    m, n = invr()

    left = True

    for i in range(1, m+1):
        if i%2 == 0:
            left = not left

            if not left:
                for j in range(n-1):
                    print(".", end = "")
                print("#", end = "")
            
            if left:
                print("#", end = "")
                for j in range(1, n):
                    print(".", end = "")
                

        if i%2 != 0:
            for j in range(n):
                print("#", end = "")
        
        print()


    
