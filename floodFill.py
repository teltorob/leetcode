def validCoordinates(matrix, row, col):
    return (row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[row]))

image= [[1,1,1],[1,1,0],[1,0,1]]
row=1
col=1

print(not validCoordinates(image,row,col))