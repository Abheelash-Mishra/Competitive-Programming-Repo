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
    initial_cost, dollars, bananas = invr()

    bill = 0

    for i in range(bananas):
        bill += initial_cost*(i+1)

    if bill > dollars:
        print(bill - dollars)
    else:
        print(0)
        