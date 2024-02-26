################ ---- Input Functions ---- ################
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def inpsl():
    return(list(map(str,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

############ ---- End Of Input Functions ---- ############

def solve(table_card, cards):
    for card in cards:
        if card[0] == table_card[0] or card[1] == table_card[1]:
            return "YES"

    return "NO"


if __name__ == "__main__":
    table_card = input()

    cards = list(map(str,input().split()))

    print(solve(table_card, cards))
