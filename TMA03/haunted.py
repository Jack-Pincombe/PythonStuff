matrix = [[0, 1, 1, 2],
          [2, 5, 0, 0],
          [2, 0, 3, 3]]
total = 0
for i in range(len(matrix)-1):
    for j in range(len(matrix[i])):
        print matrix
        if matrix[i][j] == 0:
            matrix[i+1][j] = 0
        elif matrix[i][j] != 0:
            total += 1
