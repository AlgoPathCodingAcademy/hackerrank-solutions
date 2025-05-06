def getDirection(drow,dcolumn):
    direction_dict = {}
    direction_dict[(0,-2)] = "L"
    direction_dict[(0,2)] = "R"
    direction_dict[(-2,-1)] = "UL"
    direction_dict[(-2,1)] = "UR"
    direction_dict[(2,-1)] = "LL"
    direction_dict[(2,1)] = "LR"
    return direction_dict[(drow,dcolumn)]
    

def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.
    from collections import deque
    start = (i_start,j_start)
    # assume that the red knight considers its possible neighbor locations in the following order of priority: UL, UR, R, LR, LL, L
    directions = [(-2,-1),(-2,1),(0,2),(2,1),(2,-1),(0,-2)]
    distance = {}
    path = {}
    
    for i in range(n):
        for j in range(n):
            distance[(i,j)] = -1
            
    distance[start] = 0
    
    path[start] = None
    
    to_do_list = deque()
    to_do_list.append(start)
    visited = {}
    visited[start] = True

    while True:
        if len(to_do_list) == 0:
            break
            
        row,column = to_do_list.popleft()
        
        for drow, dcolumn in directions:
            new_row, new_column = row + drow, column + dcolumn
            if (new_row >= 0 and new_row < n) and \
                (new_column >= 0 and new_column < n):
                if (new_row,new_column) not in visited:
                    visited[(new_row,new_column)] = True
                    to_do_list.append((new_row,new_column))
                    distance[(new_row,new_column)] = distance[(row,column)] + 1
                    path[(new_row,new_column)] = [(row,column),getDirection(drow,dcolumn)] 
                    
    if distance[(i_end,j_end)] == -1:
        print("Impossible")
    else:
        print(distance[(i_end,j_end)])
                
        last_path = (i_end,j_end)
        path_directions = []
        while True:
            if last_path in path:
                if path[last_path] == None:
                    break
                path_directions.append(path[last_path][1])
                last_path = path[last_path][0]
                
            else:
                break
        
        for path in path_directions[::-1]:
            print(path, end = " ")
