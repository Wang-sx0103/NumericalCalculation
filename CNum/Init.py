# -*- coding: utf-8 -*-

def initListIndex(size):
    indexList = []
    for index in range(size):
        indexList.append(index)
    return indexList


def initList(para):
    if isinstance(para, int):
        return [0 for _ in range(para)]
    elif isinstance(para, list):
        return para


def initLMat(size):
    mat = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                mat[i][j] = 1


def initUMat(AMat):
    size = len(AMat)
    mat = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if j == i + 1:
                mat[i][j] = AMat[i][j]
                continue
        if i == size - 1:
            break
