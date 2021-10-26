# -*- coding: utf-8 -*-
import lib.Init as init


class Elimination(object):
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
