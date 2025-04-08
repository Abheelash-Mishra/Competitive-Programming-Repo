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


def vadim_value(n, i, j):
    if n == 1:
        if (i, j) == (0, 0):
            return 1
        if (i, j) == (0, 1):
            return 4
        if (i, j) == (1, 0):
            return 3

        return 2

    half = 1 << (n - 1)
    block_size = 1 << (2*n - 2)

    # Top left
    if i < half and j < half:
        q, i2, j2 = 0, i, j

    # Bottom right
    elif i >= half and j >= half:
        q, i2, j2 = 1, i - half, j - half

    # Bottom left
    elif i >= half and j < half:
        q, i2, j2 = 2, i - half, j

    # Top right
    else:
        q, i2, j2 = 3, i, j - half


    return q * block_size + vadim_value(n - 1, i2, j2)

def vadim_coords(n, d):
    if n == 1:
        if d == 1:
            return (0, 0)
        if d == 4:
            return (0, 1)
        if d == 3:
            return (1, 0)
        # d == 2
        return (1, 1)

    half = 1 << (n - 1)
    block_size = 1 << (2*n - 2)

    q = (d - 1) // block_size
    offset = d - q * block_size

    i2, j2 = vadim_coords(n - 1, offset)

    # Top left
    if q == 0:
        return (i2, j2)

    # Bottom right
    elif q == 1:
        return (i2 + half, j2 + half)

    # Bottom left
    elif q == 2:
        return (i2 + half, j2)

    # Top right
    else:  # q == 3
        return (i2, j2 + half)



if __name__ == "__main__":
    for _ in range(int(input())):
        n = inp()
        q = inp()
        size = 1 << n

        for _ in range(q):
            parts = input().split()
            if parts[0] == '->':
                x, y = map(int, parts[1:])
                i, j = x-1, y-1

                print(vadim_value(n, i, j))
            else:
                d = int(parts[1])
                i, j = vadim_coords(n, d)

                print(i+1, j+1)
        








    