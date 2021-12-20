# -*- coding: utf-8 -*-
'''
This module contains a class with the same name.
'''
from .lib import Init as init


class SquareRoot():
    '''
    This class contains several square root methods for
    solving linear equations that it contains a coefficient matrix
    with positive definite symmetry.
    '''
    def __init__(self, augMat: list = []) -> None:
        '''
        augMat: You need to provide an augmented matrix in the constructor.
        If you do not provide the augMatrix here,
        you must provide it at the function called setAugMat().\n
        '''
        self._augMatrix = augMat
        self._len = len(self._augMatrix)
        self._LMatrix = init.LMat(self._len)
        self._xList = init.vector(self._len)
        self._yList = init.vector(self._len)

    def setAugMat(self, augMat) -> None:
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

    def Cholesky(self) -> list:
        '''
        Cholesky factorization.\n
        return: We will return the solution of the equations as a list.
        '''
        for i in range(self._len):
            tempSumL = 0
            tempSumY = 0
            for m in range(i):
                tempSumL += self._LMatrix[i][m]**2
                tempSumY += self._LMatrix[i][m]*self._yList[m]
            self._LMatrix[i][i] = pow(self._augMatrix[i][i] -
                                      tempSumL, 0.5)
            self._yList[i] = (self._augMatrix[i][-1] - tempSumY) / \
                self._LMatrix[i][i]
            for j in range(i+1, self._len):
                tempSumL = 0
                for n in range(i):
                    tempSumL += self._LMatrix[j][n]*self._LMatrix[i][n]
                self._LMatrix[j][i] = (self._augMatrix[j][i] -
                                       tempSumL) / self._LMatrix[i][i]
        for k in range(self._len-1, -1, -1):
            tempSumX = 0
            for p in range(k+1, self._len):
                tempSumX += self._LMatrix[p][k]*self._xList[p]
            self._xList[k] = (self._yList[k] - tempSumX)/self._LMatrix[k][k]
        return self._xList

    def LDLT(self) -> list:
        '''
        Improved square root method.\n
        return: We will return the solution of the equations as a list.
        '''
        d = init.vector(self._len)
        for i in range(self._len):
            tempSumd = 0
            tempSumY = 0
            for m in range(i):
                tempSumd += self._LMatrix[i][m]**2*d[m]
                tempSumY += self._LMatrix[i][m]*self._yList[m]
            d[i] = self._augMatrix[i][i] - tempSumd
            self._yList[i] = self._augMatrix[i][-1] - tempSumY
            for j in range(i+1, self._len):
                tempSumL = 0
                for n in range(i):
                    tempSumL += self._LMatrix[j][n]*d[n]*self._LMatrix[i][n]
                self._LMatrix[j][i] = (self._augMatrix[j][i]-tempSumL) / d[i]
        for k in range(self._len-1, -1, -1):
            tempSumX = 0
            for p in range(k+1, self._len):
                tempSumX += self._LMatrix[p][k]*self._xList[p]
            self._xList[k] = self._yList[k]/d[k] - tempSumX
        return self._xList
