def islandPerimeter(grid):
    
    peri = 0
    stack = []
    
    for i in range(len(grid)):
        
        for j in range (len(grid[i])):
            
            
            if (grid[i][j] == 1):
                stack.append((i,j))
                break
        else:
            continue  # only executed if the inner loop did NOT break
        break  # only executed if the inner loop DID break
            
    if len(stack) == 0:
        return 0
    
    while(len(stack) > 0):
        
        row, col = stack.pop()

        
        if (not validCoordinates(grid, row, col)):
            continue
            
        if (grid[row][col] == 0):
            continue
            
            
        if (grid[row][col] == 2):
            peri -= 2
            continue
        
        grid[row][col] = 2
        peri += 4
        
        pix = [(row, col-1),(row+1, col),(row, col+1),(row+1, col)]

        for p in pix:
            stack.append(p)
        # stack.append((row, col-1))
        # stack.append((row, col+1))
        # stack.append((row-1, col))
        # stack.append((row+1, col))
    
    return peri
        
def validCoordinates(matrix, row, col):
    return (row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[row]))


a=islandPerimeter([[1,1],[1,1]])
print(a)