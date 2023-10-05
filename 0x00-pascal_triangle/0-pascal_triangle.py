#!/usr/bin/python3
''' pascal '''
def pascal_triangle(n):
    ''' pascal list '''
    list = []
    if type(n) is not int or n <= 0:
        return list
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(list[i - 1][j - 1] + list[i - 1][j])
        list.append(line)
    return list
