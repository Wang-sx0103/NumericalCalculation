# -*- coding: utf-8 -*-
import CNum.Init as init


class ClassGE(object):
    def __init__(self, augMatrix):
        self._augMatrix = augMatrix
        self._len = len(self._augMatrix)
        self._xIndex = init.initListIndex(self._len)
        self._xList = init.initList(self._len)

# 直接使用高斯消元法

    def gauss(self):
        for k in range(self._len):
            for i in range(k, self._len-1):
                if round(self._augMatrix[k][k], 5) == 0.00000:
                    return "主元素存在为0的情况," + \
                        "请更换为其它消元法!"
                ratio = self._augMatrix[i+1][k]/self._augMatrix[k][k]
                for j in range(k, self._len+1):
                    self._augMatrix[i+1][j] = self._augMatrix[i+1][j] - \
                        ratio * self._augMatrix[k][j]
        if round(self._augMatrix[self._len-1][self._len-1], 5) == 0.00000:
            return "线性方程组无解！"
        self._xList[-1] = self._augMatrix[self._len-1][-1] / \
            self._augMatrix[self._len-1][self._len-1]
        for i in range(self._len-2, -1, -1):
            sum = 0
            for j in range(i + 1, self._len):
                sum += self._augMatrix[i][j]*self._xList[j]
            self._xList[i] = (self._augMatrix[i][-1] - sum) / \
                self._augMatrix[i][i]
        return self._xList

# 列主元素高斯消元法

    def orderEliminateGauss(self):
        for k in range(self._len):
            self._changeOrder(k)
            for i in range(k, self._len-1):
                if round(self._augMatrix[k][k], 5) == 0.00000:
                    return "主元素存在为0的情况," + \
                        "请更换为全主元素法!"
                ratio = self._augMatrix[i+1][k]/self._augMatrix[k][k]
                for j in range(k, self._len+1):
                    self._augMatrix[i+1][j] = self._augMatrix[i+1][j] - \
                        ratio * self._augMatrix[k][j]
        if round(self._augMatrix[self._len-1][self._len-1], 5) == 0.00000:
            return "线性方程组无解！"
        self._xList[-1] = self._augMatrix[self._len-1][-1] / \
            self._augMatrix[self._len-1][self._len-1]
        for i in range(self._len-2, -1, -1):
            sum = 0
            for j in range(i + 1, self._len):
                sum += self._augMatrix[i][j]*self._xList[j]
            self._xList[i] = (self._augMatrix[i][-1] - sum) / \
                self._augMatrix[i][i]
        return self._xList

# 全主元素法

    def completeEliminateGauss(self):
        for k in range(self._len):
            self._allChangeOrder(k)
            for i in range(k, self._len-1):
                if round(self._augMatrix[k][k], 5) == 0.00000:
                    return "线性方程组无解！"
                ratio = self._augMatrix[i+1][k]/self._augMatrix[k][k]
                for j in range(k, self._len+1):
                    self._augMatrix[i+1][j] = self._augMatrix[i+1][j] - \
                        ratio * self._augMatrix[k][j]
        if round(self._augMatrix[self._len-1][self._len-1], 5) == 0.00000:
            return "线性方程组无解！"
        self._xList[-1] = self._augMatrix[self._len-1][-1] / \
            self._augMatrix[self._len-1][self._len-1]
        for i in range(self._len-2, -1, -1):
            sum = 0
            for j in range(i + 1, self._len):
                sum += self._augMatrix[i][j]*self._xList[j]
            self._xList[i] = (self._augMatrix[i][-1] - sum) / \
                self._augMatrix[i][i]
        return self._changeXList()

    def _changeOrder(self, column):
        temp = []
        for i in range(column, self._len):
            temp.append(abs(self._augMatrix[i][column]))
        maxColumn = temp.index(max(temp)) + column
        self._augMatrix[column], self._augMatrix[maxColumn] = \
            self._augMatrix[maxColumn], self._augMatrix[column]

    def _allChangeOrder(self, column):
        max = 0
        rowMax = 0         # 最大值的行索引
        listMax = 0        # 最大值的列索引
        for i in range(column, self._len):
            for j in range(column, self._len):
                if abs(self._augMatrix[i][j]) > max:
                    max = abs(self._augMatrix[i][j])
                    rowMax = i
                    listMax = j
                temp = round(self._augMatrix[-1][-2])
                if column == (self._len-1) and (temp == 0.00000):
                    rowMax = column
                    listMax = column
        self._augMatrix[column], self._augMatrix[rowMax] = \
            self._augMatrix[rowMax], self._augMatrix[column]
        for k in range(self._len):
            self._augMatrix[k][listMax], self._augMatrix[k][column] = \
                self._augMatrix[k][column], self._augMatrix[k][listMax]
        self._xIndex[listMax], self._xIndex[column] = \
            self._xIndex[column], self._xIndex[listMax]

    def _changeXList(self):
        changedXList = []
        for i in range(len(self._xList)):
            changedXList.append(self._xList[self._xIndex[i]])
        return changedXList


class TriDecomposition(object):

    def __init__(self, augMatrix):
        self._augMatrix = augMatrix
        self._len = len(self._augMatrix)
        # self.__ininXIndex()
        self._LMatrix = init.initMatrix(self._len)
        self._UMatrix = init.initMatrix(self._len)
        self._initLMatrix()
        self._initUMatrix()
        self._xList = [0 for i in range(self._len)]
        self._yList = [0 for i in range(self._len)]

    def DirTriDecomposition(self):
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

    def chase(self):
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

    def _initLMatrix(self):
        for i in range(self._len):
            for j in range(self._len):
                if i == j:
                    self._LMatrix[i][j] = 1

    def _initUMatrix(self):
        for i in range(self._len):
            for j in range(self._len):
                if j == i + 1:
                    self._UMatrix[i][j] = self._augMatrix[i][j]
                    continue
            if i == self._len - 1:
                break


class SquareRoot(object):
    def __init__(self, augMatrix):
        self._augMatrix = augMatrix
        self._len = len(self._augMatrix)
        self._LMatrix = init.initMatrix(self._len)
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

    def _initLMatrix(self):
        for i in range(self._len):
            for j in range(self._len):
                if i == j:
                    self._LMatrix[i][j] = 1
