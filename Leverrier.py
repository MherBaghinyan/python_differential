matrix = [[1 for x in range(5)] for x in range(5)]

matrix[0][0] = 2
matrix[1][1] = -1

print(matrix)

def sp(matrix):
    "calculates matrix trail"
    sum =0
    for i in range(0, len(matrix)):
        sum += matrix[i][i]
    print(sum)

def multiply(matrix1, matrix2):
    "multiplies given 2 matrixes"
    row = len(matrix1)
    column = len(matrix1[0])
    result = [[0 for x in range(row)] for x in range(column)]
    for i in range(0, row):
        for j in range(0, column):
            for k in range(0, column):
                result[i][k] += matrix1[i][k] + matrix2[k][j]
    return result

def add_image(img1, img2, k):
    "multiplies 2 given images"
    row = len(img1)
    column = len(img2[0])
    result = [[0 for x in range(row)] for x in range(column)]
    # for i in range(0, k):
    # result += multiply(img1, img2)

sp(matrix)
