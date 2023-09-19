def solution(wallpaper):
    answer = []
    min_coor_i, min_coor_j, max_coor_i, max_coor_j = 100, 100, 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                min_coor_i = min(min_coor_i, i)
                min_coor_j = min(min_coor_j, j)
                
                max_coor_i = max(max_coor_i, i)
                max_coor_j = max(max_coor_j, j)
        
    return [min_coor_i, min_coor_j, max_coor_i+1, max_coor_j+1]