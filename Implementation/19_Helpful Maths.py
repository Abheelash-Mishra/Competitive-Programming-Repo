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
    string = input()

    numbers = []
    for i in range(0,len(string), 2):
        numbers.append(string[i])
    
    numbers = sorted(numbers)

    for i in range(len(numbers) - 1):
        print(numbers[i] + "+", end = "")
    print(numbers[-1])