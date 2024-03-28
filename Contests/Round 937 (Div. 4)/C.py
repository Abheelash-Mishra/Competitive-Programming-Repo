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

# def maxSubArray(arr, n):
    
#     return 
       

if __name__ == "__main__":
    for tc in range(inp()):
        string = input()

        string = string.split(":")
        
        num = int(string[0])
        
        
        if num == 12:
            string.append(" PM")

        elif num > 12:
            string.append(" PM")
            num -= 12
            string[0] = str(num)
        
        else:
            if num == 0:
                num = 12
                string[0] = str(num)
            
            string.append(" AM")

        string.insert(1,":")

        if len(string[0]) == 1:
            print("0"+string[0], end = "")

            for i in string[1:]:
                print(i, end = "")
        
        else:
            for i in string:
                print(i, end = "")
        print()

        
        
                





            

        

        


        
