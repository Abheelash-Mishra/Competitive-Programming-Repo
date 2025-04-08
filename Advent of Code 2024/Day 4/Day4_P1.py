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
def count_xmas_occurrences(grid):
    n, m = len(grid), len(grid[0])  # Dimensions of the grid
    word = "XMAS"
    word_len = len(word)
    count = 0

    # Define directions (dx, dy): right, left, down, up, diagonal (4 ways)
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # diagonal down-right
        (1, -1),  # diagonal down-left
        (-1, 1),  # diagonal up-right
        (-1, -1)  # diagonal up-left
    ]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m

    # Function to check for "XMAS" starting at (x, y) in a given direction
    def check_word(x, y, dx, dy):
        for k in range(word_len):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True

    # Traverse each cell and check all directions
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X':  # Only start checking if current cell is 'X'
                for dx, dy in directions:
                    if check_word(i, j, dx, dy):
                        count += 1

    return count


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        grid = [line.strip() for line in file]
    
    result = count_xmas_occurrences(grid)
    print(result)




    