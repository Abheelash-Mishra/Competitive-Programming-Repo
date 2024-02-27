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

# def solve():
    
    
if __name__ == "__main__":
    for tc in range(inp()):
        a, b, l = invr()

        x, y = 0, 0
        count = 0

        possible_values = set()

        while a**x <= l and b**y <= l:
            for i in range(25):
                x = i
                for j in range(25):
                    y = j

                    if l % (a**x * b**y) == 0:
                        # print(f"{l} / ({a**x} * {b**y})")
                        possible_values.add(int(l / (a**x * b**y)))

        print(len(possible_values))

        
