# -*- coding: utf-8 -*-

def vectorIndex(size: int) -> list:
    indexList = []
    for index in range(size):
        indexList.append(index)
    return indexList


def vector(listLen: int, flag: int = 0) -> list:
    if flag == 0:
        return [0 for _ in range(listLen)]
    elif flag == 1:
        returnList = [0 for _ in range(listLen)]
        returnList[-1] = 1
        return returnList
    elif flag == 11:
        returnList = [0 for _ in range(listLen)]
        return returnList


def LMat(size: int) -> list:
    mat = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                mat[i][j] = 1
    return mat


def UMat(AMat: list) -> list:
    size = len(AMat)
    mat = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if j == i + 1:
                mat[i][j] = AMat[i][j]
                continue
        if i == size - 1:
            break
    return mat


def Matrix(row: int, col: int) -> list:
    return [[0]*col for _ in range(row)]


def AugMat(mat: list, vector: list) -> list:
    row: int = len(mat)
    col: int = len(vector[0])
    for i in range(row):
        for j in range(col):
            mat[i].append(vector[i][j])
    return mat


def Identity(order: int, lambda0: float = 1) -> list:
    resultMat = Matrix(order, order)
    for i in range(order):
        for j in range(order):
            if i == j:
                resultMat[i][j] = 1*lambda0
    return resultMat
