def solve_maze(maze,x,y,path):
    if x<0 or x>=len(maze) or y<0 or  y>=len(maze[0]) or maze[x][y]==0 or (x,y) in path:
        return False
    if (x,y)==(len(maze)-1,len(maze[0]-1)):
        path.append((x,y))
        return True
    path.append((x,y))
    if ((solve_maze(maze,x+1,y,path)) or (solve_maze(maze,x-1,y,path)) or (solve_maze(maze,x,y+1,path)) or (solve_maze(maze,x,y-1,path))):
        return True
    path.pop()
    return False
maze=[[0,0,0,0]
      [1,1,0,1]
      [0,0,0,0]
      [0,1,1,0]]
path=[]
if solve_maze(maze,0,0,path):
    print('path found',path)
else:
    print('path not found')

