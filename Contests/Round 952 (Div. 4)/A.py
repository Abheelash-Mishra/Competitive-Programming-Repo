################ ---- Input Functions ---- ################
def inp():
    return(int(input()))
def inlt():
    return(list(map(str,input().split())))
def insr():
    s = input().lower()
    return(list(s[:len(s)]))
def invr():
    return(map(str,input().split()))

############ ---- End Of Input Functions ---- ############

if __name__ == "__main__":
    for tc in range(inp()):
        word1, word2 = invr()

        temp = word1[0]
        word1 = word1[:0] + word2[0] + word1[1:]
        word2 = word2[:0] + temp + word2[1:]
        

        print(word1, word2)

        




    
        
                
