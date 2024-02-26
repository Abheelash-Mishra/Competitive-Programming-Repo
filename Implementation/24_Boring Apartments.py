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

def solve(x):
    count = 0

    for i in range(1, 10):
        s = ""
        for j in range(1, 5):
            s += str(i)
            count += j

            if s == x:
                return count


if __name__ == "__main__":
    for tc in range(inp()):
        x = input()

        print(solve(x))
