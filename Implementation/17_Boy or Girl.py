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
    name = input()

    characters = {}

    for i in name:
        if i not in characters:
            characters[i] = 1
    
    if len(characters) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")