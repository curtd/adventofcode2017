import numpy as np
matrix = np.zeros((lower_right_corner,lower_right_corner))
idx = (lower_right_corner-1)/2
idy = idx
matrix[idx,idy] = 1
levels = lower_right_corner
sum_nbrs = lambda mat, idx, idy: np.sum(mat[idx-1:idx+2,idy-1:idy+2])
found = False
# This is gross, but it works
for lvl in range(1,lower_right_corner):
    lvl = 2*lvl
    idx += 1
    for dy in range(lvl):
        matrix[idx,idy] = sum_nbrs(matrix,idx,idy)
        if matrix[idx,idy] > value:
            print(matrix[idx,idy])
            found = True
            break
        if dy < lvl-1:
            idy += 1
    if found:
        break
    idx -= 1
    for dx in range(lvl):
        matrix[idx,idy] = sum_nbrs(matrix,idx,idy)
        if matrix[idx,idy] > value:
            print(matrix[idx,idy])
            found = True
            break
        if dx < lvl-1:
            idx -= 1
    if found:
        break
    idy -= 1
    for dy in range(lvl):
        matrix[idx,idy] = sum_nbrs(matrix,idx,idy)
        if matrix[idx,idy] > value:
            print(matrix[idx,idy])
            found = True
            break
        if dy < lvl-1:
            idy -= 1
    if found:
        break
    idx += 1
    for dx in range(lvl):
        matrix[idx,idy] = sum_nbrs(matrix,idx,idy)
        if matrix[idx,idy] > value:
            print(matrix[idx,idy])
            found = True
            break
        if dx < lvl-1:
            idx += 1
    if found:
        break

print("Next integer after input: {}".format(matrix[idx,idy]))