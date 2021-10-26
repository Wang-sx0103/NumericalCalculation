# -*- coding: utf-8 -*-
import lib.Init as init


class SquareRoot(object):
    def __init__(self, augMatrix):
        self._augMatrix = augMatrix
        self._len = len(self._augMatrix)
        self._LMatrix = init.initLMat(self._len)
        self._xList = init.initList(self._len)
        self._yList = init.initList(self._len)

    def CholeskyDecomposition(self):
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

    def LDLT(self):
        d = init.initList(self._len)
        self._initLMatrix()
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
