# -*- coding: utf-8 -*-

# 判断是否是矩阵（二维列表）
def isMatrix(mat: list) -> bool:
    if len(mat) == 0:
        return False
    else:
        return isinstance(mat[0], list)


# 判断两矩阵是否可以相乘
def isMatMul(mat1: list, mat2: list) -> bool:
    if len(mat1[0]) == len(mat2):
        return True
    else:
        return False
