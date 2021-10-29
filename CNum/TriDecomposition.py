# -*- coding: utf-8 -*-
import lib.Init as init


class TriDecomposition(object):
    def __init__(self, augMatrix: list) -> None:
        self._augMatrix = augMatrix
        self._len = len(self._augMatrix)
        self._LMatrix = init.LMat(self._len)
        self._UMatrix = init.UMat(self._augMatrix)
        self._xList = init.vector(self._len)
        self._yList = init.vector(self._len)

    def getLMat(self) -> list:
        return self._LMatrix

    def getUMat(self) -> list:
        return self._UMatrix

    # 直接三角分解法

    def DirTriDecomposition(self) -> list:
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

    # 追赶法

    def chase(self) -> list:
        self._UMatrix[0][0] = self._augMatrix[0][0]
        self._yList[0] = self._augMatrix[0][-1]
        for i in range(1, self._len):
            for j in range(self._len):
                if (i - 1) == j:
                    if round(self._UMatrix[i-1][i-1], 5) == 0.00000:
                        return "不可用追赶法！"
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
