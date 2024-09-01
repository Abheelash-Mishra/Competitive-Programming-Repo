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
        n = inp()*2

        symbol = "#"
        col_count = 0

        store_symbol = ""

        for i in range(n//2):
            for j in range(n):
                if col_count == 2:
                    if symbol == "#":
                        symbol = "."
                    else:
                        symbol = "#"
                    col_count = 0
                
                store_symbol += symbol

                col_count += 1

            print(store_symbol)
            print(store_symbol)

            store_symbol = ""

            if (n//2)%2 == 0 :
                if symbol == "#":
                    symbol = "."
                else:
                    symbol = "#"

                
