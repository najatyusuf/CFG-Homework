def search_in_matrix(matrix, target, width):
    """
    :param matrix: matrix (list of lists)
    :param target: target value to search in matrix
    :param width: width of matrix
    :return: coordinates of target value
    """
    i = 0
    j = width - 1  # index of the top right element

    while i < width and j >= 0:

        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1

    return [-1, -1]


matrx = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]

targ = 44
matrx_len = len(matrx[0])  # width of matrix

# returns target coordinates if in matrix
print(search_in_matrix(matrx, targ, matrx_len))
print(search_in_matrix(matrx, 1003, matrx_len))
print(search_in_matrix(matrx, 33, matrx_len))
print(search_in_matrix(matrx, 40, matrx_len))


# returns [-1, -1] if not in matrix
print(search_in_matrix(matrx, 72, matrx_len))
print(search_in_matrix(matrx, 91, matrx_len))
print(search_in_matrix(matrx, 27, matrx_len))
print(search_in_matrix(matrx, 13, matrx_len))
