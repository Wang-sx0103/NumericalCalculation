# -*- coding: utf-8 -*-
'''
This module contains a class with the same name.
'''
from .lib import Init as init
from .error import error

class TriDecomposition():
    '''
    This class contains several triangular decomposition methods
    for solving linear equations.
    '''
    def __init__(self, augMat: list = []) -> None:
        '''
        augMat: You need to provide an augmented matrix in the constructor.
        If you do not provide the augMatrix here,
        you must provide it at the function called
        setAugMat().\n
        '''
        self._augMatrix = augMat
        self._len = len(self._augMatrix)
        self._LMatrix = init.LMat(self._len)
        self._UMatrix = init.UMat(self._augMatrix)
        self._xList = init.vector(self._len)
        self._yList = init.vector(self._len)

    def setAugMat(self, augMat: list) -> None:
        '''
        augMat: You can provide an augmented matrix.
        '''
        self._augMatrix = augMat

    def getAugMat(self) -> list:
        '''
        return: We will return the augmented matrix.
        '''
        return self._augMatrix

    def getLMat(self) -> list:
        '''
        return: We will return the L matrix.
        '''
        return self._LMatrix

    def getUMat(self) -> list:
        '''
        return: We will return the U matrix.
        '''
        return self._UMatrix

    def Doolittle(self) -> list:
        '''
        Doolittle decomposition method.\n
        reteurn: We will return the solution of the equations as a list.
        '''
        self._yList[0] = self._augMatrix[0][-1]
        for i in range(self._len):
            tempSumY = 0
            for j in range(i, self._len):
                tempSumU = 0
                tempSumL = 0
                for k in range(0, i):
                    tempSumU += self._LMatrix[i][k]*self._UMatrix[k][j]
                    if j == self._len - 1:
                        continue
                    else:
                        tempSumL += self._LMatrix[j+1][k]*self._UMatrix[k][i]
                self._UMatrix[i][j] = self._augMatrix[i][j] - tempSumU
                if j == self._len - 1:
                    continue
                else:
                    self._LMatrix[j+1][i] = (self._augMatrix[j+1][i] -
                                             tempSumL) / self._UMatrix[i][i]
            for m in range(i):
                tempSumY += self._LMatrix[i][m]*self._yList[m]
            self._yList[i] = self._augMatrix[i][-1] - tempSumY
        for p in range(self._len-1, -1, -1):
            tempSumX = 0
            for q in range(p+1, self._len):
                tempSumX += self._UMatrix[p][q]*self._xList[q]
            self._xList[p] = (self._yList[p] - tempSumX) / \
                self._UMatrix[p][p]
        return self._xList

    def Chase(self) -> list:
        '''
        Chasedecomposition method.\n
        return: We will return the solution of the equations as a list.
        '''
        self._UMatrix[0][0] = self._augMatrix[0][0]
        self._yList[0] = self._augMatrix[0][-1]
        for i in range(1, self._len):
            for j in range(self._len):
                if (i - 1) == j:
                    if round(self._UMatrix[i-1][i-1], 5) == 0.00000:
                        print(error[201])
                        return
                    self._LMatrix[i][j] = self._augMatrix[i][j] / \
                        self._UMatrix[i-1][i-1]
                    self._UMatrix[i][j+1] = self._augMatrix[i][j+1] - \
                        self._UMatrix[i-1][j+1]*self._LMatrix[i][j]
                    self._yList[i] = self._augMatrix[i][-1] - \
                        self._LMatrix[i][j]*self._yList[i-1]
                    break
        self._xList[-1] = self._yList[-1]/self._UMatrix[-1][-1]
        for i in range(self._len - 2, -1, -1):
            self._xList[i] = (self._yList[i] - self._UMatrix[i][i+1] *
                              self._xList[i+1]) / self._UMatrix[i][i]
        return self._xList
