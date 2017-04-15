def matrixElementsSum(matrix):
    total = 0
    final = len(matrix)
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                matrix[i + 1][j] = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total += matrix[i][j]

    return total

