board=[[0,0,0,7,0,0,0,0,3],
      [0,9,6,0,0,0,0,0,0],
      [2,0,0,8,5,0,0,0,0],
      [1,7,0,2,0,4,0,3,6],
      [0,6,0,0,7,0,0,4,0],
      [0,8,2,6,0,3,5,1,0],
      [0,0,0,0,1,7,0,0,8],
      [0,0,0,0,0,0,2,5,0],
      [9,0,0,0,0,2,0,0,0]]


def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row,col=find

    for i in range(1,10):
        if (valid(grid,(row,col),i)):
            grid[row][col]=i

            if solve(grid):
                return True

            grid[row][col]=0

    return False

def printgrid(grid):
      i=0
      j=0
      for i in range(0,9):
            if (i%3==0):
                  print('_'*22)
            for j in range(0, 9):
               print(str(grid[i][j]),end=' ')
               if(j%3==2):
                        print('|',end=' ')
               if(j==8):
                  print()
                  break


def find_empty(grid):
    for i in range(0, 9):
        for j in range(0, 9):
            if (grid[i][j] == 0):
                return (i,j)
    return None


def valid(grid,pos,a):

    #check row
    for i in range(len(grid)):
        if grid[pos[0]][i]==a and pos[1]!=i:
            return False

    #check column
    for i in range(len(grid)):
       if grid[i][pos[1]] == a and pos[0] != i:
           return False

   #check cubes
    box_x=pos[1]//3
    box_y=pos[0]//3
    for i in range (box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if grid[i][j]==a and (i,j)!=pos:
                return False

    return True


printgrid(board)
solve(board)
print('_______________________________________________________________________________________________________')
print()
printgrid(board)
