map=[
 ['0', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O'],
 ['D', 'O', 'O', 'O'],
 ['X', 'O', 'D', 'O']]

print(map)



def TresureIsland(map):

    if not map:
        return -1

    TREASURE, DANGER, SAFE, VISITED = 'X', 'D', 'O', 'V'

    queue = [(0,0)]
    steps = 0

    while queue:
        queue_temp = []
        for x, y in queue:
            for x_dif, y_dif in [[0,1],[0,-1],[1,0],[-1,0]]:
                cur_x = x + x_dif
                cur_y = y + y_dif

                if 0 <= cur_x < len(map) and 0 <= cur_y < len(map[0]):
                    if map[cur_x][cur_y] == TREASURE:
                        return steps + 1
                    if map[cur_x][cur_y] == SAFE:
                        queue_temp.append((cur_x,cur_y))
            map[x][y] = VISITED
        steps +=1
        queue = queue_temp
    return -1


#print (min_steps(map))

print(TresureIsland(map))
