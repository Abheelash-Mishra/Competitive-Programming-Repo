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


def solve(n):
    increment = False

    spaces = n -1
    for row in range(n+1):
        for _ in range(spaces, -1, -1):
            print(" ", end = " ")
        
        for l_val in range(row):
            print(l_val, end = " ")

        for r_val in range(row, -1, -1):
            print(r_val, end = " ")

        spaces -= 1
        
        print()
    
    spaces = 0
    
    for row in range(n-1, -1, -1):
        for _ in range(spaces, -1, -1):
            print(" ", end = " ")
        
        for l_val in range(row):
            print(l_val, end = " ")

        for r_val in range(row, -1, -1):
            print(r_val, end = " ")

        spaces += 1
        
        print()
    

if __name__ == "__main__":
    n = inp()

    solve(n)
    