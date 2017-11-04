# Given an NxM matrix, and a robot (only able to move down and right),
# starting at the top left corner, calculate the number of possible paths from
# the starting point to the bottom right corner.

# Notice that there is only one path to reach each tile in the top row,
# or the left column. For other tiles, the number of ways to reach that
# location is the sum of the ways to reach the tile from the left, and the
# number of ways to reach the tile from the right. We can initialize a matrix
# and solve it using a bottom-up approach.

def num_paths(N, M):
    matrix = [[1] * M for _ in xrange(N)]
    for x in xrange(1, N):
        for y in xrange(1, M):
            matrix[x][y] = matrix[x][y-1] + matrix[x-1][y]
    return matrix[N-1][M-1]

if __name__=="__main__":
    assert num_paths(1, 1) == 1
    assert num_paths(2, 2) == 2
    assert num_paths(2, 3) == num_paths(3, 2) == 3
    assert num_paths(3, 3) == 6
