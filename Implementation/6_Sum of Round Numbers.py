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


def is_round(n):
    n = str(n)

    for i in range(1, len(n)):
        if n[i] != "0":
            return False
    
    return True

if __name__ == "__main__":
    tc = inp()

    for _ in range(tc):
        n = inp()

        if is_round(n):
            print(1)
            print(n)
            continue

        temp_arr = []
        power_of_10 = 0

        for i in range(len(str(n))):
            temp_arr.append(n % 10)
            n = n // 10

        count = 0
        for i in temp_arr:
            if i != 0:
                count += 1
        
        print(count)
        
        for i in temp_arr:
            if i*(10**power_of_10) != 0:
                print(i*(10**power_of_10), end = " ")
            power_of_10 += 1
        print()
    
