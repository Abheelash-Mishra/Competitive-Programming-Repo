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


def min_removals(n):
    total_len = len(n)
    zeros_so_far = 0
    max_prefix_zeros = 0

    for ch in n:
        if ch == '0':
            zeros_so_far += 1
        else:
            max_prefix_zeros = max(max_prefix_zeros, zeros_so_far)

    keep = 1 + max_prefix_zeros

    return total_len - keep

if __name__ == "__main__":
    for _ in range(int(input())):
        n = input().strip()

        print(min_removals(n))






    