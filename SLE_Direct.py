# -*- coding: utf-8 -*-

class ClassGE(object):
    def __init__(self, augMatrix):
        self.__augMatrix = augMatrix
        self.__len = len(self.__augMatrix)
        self.__xIndex = []
        self.__ininXIndex()
        self.__xList = [0 for i in range(self.__len)]

# 直接使用高斯消元法

    def gauss(self):
        for k in range(self.__len):
            for i in range(k, self.__len-1):
                if round(self.__augMatrix[k][k], 5) == 0.00000:
                    return "主元素存在为0的情况," + \
                        "请更换为其它消元法!"
                ratio = self.__augMatrix[i+1][k]/self.__augMatrix[k][k]
                for j in range(k, self.__len+1):
                    self.__augMatrix[i+1][j] = self.__augMatrix[i+1][j] - \
                        ratio * self.__augMatrix[k][j]
        if round(self.__augMatrix[self.__len-1][self.__len-1], 5) == 0.00000:
            return "线性方程组无解！"
        self.__xList[-1] = self.__augMatrix[self.__len-1][-1] / \
            self.__augMatrix[self.__len-1][self.__len-1]
        for i in range(self.__len-2, -1, -1):
            sum = 0
            for j in range(i + 1, self.__len):
                sum += self.__augMatrix[i][j]*self.__xList[j]
            self.__xList[i] = (self.__augMatrix[i][-1] - sum) / \
                self.__augMatrix[i][i]
        return self.__xList

# 列主元素高斯消元法

    def orderEliminateGauss(self):
        for k in range(self.__len):
            self.__changeOrder(k)
            for i in range(k, self.__len-1):
                if round(self.__augMatrix[k][k], 5) == 0.00000:
                    return "主元素存在为0的情况," + \
                        "请更换为全主元素法!"
                ratio = self.__augMatrix[i+1][k]/self.__augMatrix[k][k]
                for j in range(k, self.__len+1):
                    self.__augMatrix[i+1][j] = self.__augMatrix[i+1][j] - \
                        ratio * self.__augMatrix[k][j]
        if round(self.__augMatrix[self.__len-1][self.__len-1], 5) == 0.00000:
            return "线性方程组无解！"
        self.__xList[-1] = self.__augMatrix[self.__len-1][-1] / \
            self.__augMatrix[self.__len-1][self.__len-1]
        for i in range(self.__len-2, -1, -1):
            sum = 0
            for j in range(i + 1, self.__len):
                sum += self.__augMatrix[i][j]*self.__xList[j]
            self.__xList[i] = (self.__augMatrix[i][-1] - sum) / \
                self.__augMatrix[i][i]
        return self.__xList

# 全主元素法

    def completeEliminateGauss(self):
        for k in range(self.__len):
            self.__allChangeOrder(k)
            for i in range(k, self.__len-1):
                if round(self.__augMatrix[k][k], 5) == 0.00000:
                    return "线性方程组无解！"
                ratio = self.__augMatrix[i+1][k]/self.__augMatrix[k][k]
                for j in range(k, self.__len+1):
                    self.__augMatrix[i+1][j] = self.__augMatrix[i+1][j] - \
                        ratio * self.__augMatrix[k][j]
        if round(self.__augMatrix[self.__len-1][self.__len-1], 5) == 0.00000:
            return "线性方程组无解！"
        self.__xList[-1] = self.__augMatrix[self.__len-1][-1] / \
            self.__augMatrix[self.__len-1][self.__len-1]
        for i in range(self.__len-2, -1, -1):
            sum = 0
            for j in range(i + 1, self.__len):
                sum += self.__augMatrix[i][j]*self.__xList[j]
            self.__xList[i] = (self.__augMatrix[i][-1] - sum) / \
                self.__augMatrix[i][i]
        return self.__changeXList()

    def __changeOrder(self, column):
        temp = []
        for i in range(column, self.__len):
            temp.append(abs(self.__augMatrix[i][column]))
        maxColumn = temp.index(max(temp)) + column
        self.__augMatrix[column], self.__augMatrix[maxColumn] = \
            self.__augMatrix[maxColumn], self.__augMatrix[column]

    def __allChangeOrder(self, column):
        max = 0
        rowMax = 0         # 最大值的行索引
        listMax = 0        # 最大值的列索引
        for i in range(column, self.__len):
            for j in range(column, self.__len):
                if abs(self.__augMatrix[i][j]) > max:
                    max = abs(self.__augMatrix[i][j])
                    rowMax = i
                    listMax = j
                temp = round(self.__augMatrix[-1][-2])
                if column == (self.__len-1) and (temp == 0.00000):
                    rowMax = column
                    listMax = column
        self.__augMatrix[column], self.__augMatrix[rowMax] = \
            self.__augMatrix[rowMax], self.__augMatrix[column]
        for k in range(self.__len):
            self.__augMatrix[k][listMax], self.__augMatrix[k][column] = \
                self.__augMatrix[k][column], self.__augMatrix[k][listMax]
        self.__xIndex[listMax], self.__xIndex[column] = \
            self.__xIndex[column], self.__xIndex[listMax]

    def __ininXIndex(self):
        for index in range(self.__len):
            self.__xIndex.append(index)

    def __changeXList(self):
        changedXList = []
        for i in range(len(self.__xList)):
            changedXList.append(self.__xList[self.__xIndex[i]])
        return changedXList


class TriDecomposition(object):

    def __init__(self, augMatrix):
        self.__augMatrix = augMatrix
        self.__len = len(self.__augMatrix)
        # self.__ininXIndex()
        self.__LMatrix = [[0] * self.__len for i in range(self.__len)]
        self.__UMatrix = [[0] * self.__len for i in range(self.__len)]
        self.__initLMatrix()
        self.__initUMatrix()
        self.__xList = [0 for i in range(self.__len)]
        self.__yList = [0 for i in range(self.__len)]

    def DirTriDecomposition(self):
        self.__yList[0] = self.__augMatrix[0][-1]
        for i in range(self.__len):
            tempSumY = 0
            for j in range(i, self.__len):
                tempSumU = 0
                tempSumL = 0
                for k in range(0, i):
                    tempSumU += self.__LMatrix[i][k]*self.__UMatrix[k][j]
                    if j == self.__len - 1:
                        continue
                    else:
                        tempSumL += self.__LMatrix[j+1][k]*self.__UMatrix[k][i]
                self.__UMatrix[i][j] = self.__augMatrix[i][j] - tempSumU
                if j == self.__len - 1:
                    continue
                else:
                    self.__LMatrix[j+1][i] = (self.__augMatrix[j+1][i] -
                                              tempSumL) / self.__UMatrix[i][i]
            for m in range(i):
                tempSumY += self.__LMatrix[i][m]*self.__yList[m]
            self.__yList[i] = self.__augMatrix[i][-1] - tempSumY
        for p in range(self.__len-1, -1, -1):
            tempSumX = 0
            for q in range(p+1, self.__len):
                tempSumX += self.__UMatrix[p][q]*self.__xList[q]
            self.__xList[p] = (self.__yList[p] - tempSumX) / \
                self.__UMatrix[p][p]
        return self.__xList

    def chase(self):
        self.__UMatrix[0][0] = self.__augMatrix[0][0]
        self.__yList[0] = self.__augMatrix[0][-1]
        for i in range(1, self.__len):
            for j in range(self.__len):
                if (i - 1) == j:
                    if round(self.__UMatrix[i-1][i-1], 5) == 0.00000:
                        return "不可用追赶法！"
                    self.__LMatrix[i][j] = self.__augMatrix[i][j] / \
                        self.__UMatrix[i-1][i-1]
                    self.__UMatrix[i][j+1] = self.__augMatrix[i][j+1] - \
                        self.__UMatrix[i-1][j+1]*self.__LMatrix[i][j]
                    self.__yList[i] = self.__augMatrix[i][-1] - \
                        self.__LMatrix[i][j]*self.__yList[i-1]
                    break
        self.__xList[-1] = self.__yList[-1]/self.__UMatrix[-1][-1]
        for i in range(self.__len - 2, -1, -1):
            self.__xList[i] = (self.__yList[i] - self.__UMatrix[i][i+1] *
                               self.__xList[i+1]) / self.__UMatrix[i][i]
        return self.__xList

    def __initLMatrix(self):
        for i in range(self.__len):
            for j in range(self.__len):
                if i == j:
                    self.__LMatrix[i][j] = 1

    def __initUMatrix(self):
        for i in range(self.__len):
            for j in range(self.__len):
                if j == i + 1:
                    self.__UMatrix[i][j] = self.__augMatrix[i][j]
                    continue
            if i == self.__len - 1:
                break


class SquareRoot(object):
    def __init__(self):
        pass
