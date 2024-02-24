############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))


if __name__ == "__main__":
    n, bottles, ml, limes, slices, salt, min_ml, min_salt = invr()

    total_ml = bottles * ml
    toasts = total_ml//min_ml

    total_limes = limes*slices

    salt_toasts = salt//min_salt

    ans = min(min(toasts, total_limes), salt_toasts)//n

    print(ans)
