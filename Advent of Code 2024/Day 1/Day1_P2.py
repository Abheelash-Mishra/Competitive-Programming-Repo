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
    left, right = [], {}

    for _ in range(1000):
        temp = input().split()

        left.append(int(temp[0]))
        right[int(temp[1])] = right.get(int(temp[1]), 0) + 1
    
    
    similarity_score = 0
    for num in left:
        similarity_score += (num * right.get(num, 0))
    
    print(similarity_score)
    