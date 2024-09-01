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
    for tc in range(inp()):
        l, r = invr()

        count = 0
        current = l
        diff = 1

        while current <= r:
            count += 1
            current += diff
            diff += 1

        print(count)

