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

def solve(word):
    vowels = ("a", "e", "i", "o", "u", "y")

    n = len(word)
    i = 0

    while i < n:
        if word[i] in vowels:
            word.pop(i)
            n = len(word)
        else:
            i += 1

    ans = ""

    for i in range(len(word)):
        ans += "." + word[i]

    return ans
    

if __name__ == "__main__":
    word = insr()

    print(solve(word))
