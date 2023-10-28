#!/usr/bin/python3
""" module """


def pascal_triangle(n):
    """ print pascal tri """
    if n <= 0:
        return []
    lis = [[1]]
    for i in range(n):
        newlist = [[]]
        newlist.append(lis[i][0])
        for j in range(len(lis) - 1):
            newlist.append(sum((lis[i][j]), (lis[i][j + 1])))
        newlist.append(lis[i][-1])
        lis.append(newlist)
    return lis
