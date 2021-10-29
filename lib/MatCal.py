# -*- coding: utf-8 -*-


import lib.Init as init
import lib.IsOk as ok


def matMul(mat1: list, mat2: list) -> list:
    mat1 = vectorToMat(mat1)
    mat2 = vectorToMat(mat2)
    lenMat1Row = len(mat1)
    lenMat2Col = len(mat2[0])
    lenCom = len(mat1[0])
    resultMat = init.Matrix(lenMat1Row, lenMat2Col)
    for i in range(lenMat1Row):
        for j in range(lenMat2Col):
            for k in range(lenCom):
                resultMat[i][j] += mat1[i][k]*mat2[k][j]
    return resultMat


def matDivNum(mat: list, num: float) -> list:
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = mat[i][j]/num
    return mat


def absMax(mat: list, flag: int = 0) -> float:
    max = 0
    indexI = 0
    indexJ = 0
    flag2 = 0
    for i in range(len(mat)):
        if isinstance(mat[i], list):
            flag2 = 1
            for j in range(len(mat[i])):
                if max < abs(mat[i][j]):
                    max = abs(mat[i][j])
                    indexI = i
                    indexJ = j

        else:
            if max < abs(mat[i]):
                max = abs(mat[i])
                indexI = i

    if flag == 1:
        if flag2 == 1:
            return mat[indexI][indexJ]
        else:
            return mat[indexI]
    else:
        return max


def vectorToMat(vector: list) -> list:
    mat = []
    if ok.isMatrix(vector):
        return vector
    else:
        for i in range(len(vector)):
            mat.append([vector[i]])
        return mat
