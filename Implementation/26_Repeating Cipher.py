################ ---- Input Functions ---- ################
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def inpsl():
    return(list(map(str,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

############ ---- End Of Input Functions ---- ############

def solve(word):
    add_idx = 1
    curr_idx = 0

    ans = ""

    while curr_idx < n:
        ans += word[curr_idx]

        curr_idx += add_idx
        add_idx += 1
    
    return ans
    
    
if __name__ == "__main__":
    n = inp()

    word = input()
    print(solve(word))
