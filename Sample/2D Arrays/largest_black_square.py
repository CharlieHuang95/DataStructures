def find_largest_black_square(matrix):
    n = len(matrix)
    for m in range(len(matrix), 0, -1):
        for x in range(0, n - m + 1):
            for y in range(0, n - m + 1):
                if is_enclosed(matrix, n, m, x, y) == 1:
                    return m

def is_enclosed(matrix, n, m, x, y):
    is_black = 1
        # Check the top
    for index in range(x, x + m):
        is_black *= matrix[y][index]
        # Check bottom
        is_black *= matrix[y+m-1][index]
    for index in range(y, y+m):
        is_black *= matrix[index][x]
    # Check left
        is_black *= matrix[index][x + m-1]
    # Check right
    return is_black
