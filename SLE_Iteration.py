# -*- coding: utf-8 -*-
class Iteration(object):
    def __init__(self, augMatrix, xList=[]):
        self._augMatrix = augMatrix
        self._len = len(self._augMatrix)
        self._xList = self._initXList(xList)

    def jacobiIteration(self, num=100):
        count = 0
        deltaList = 1
        while deltaList > 0.00001:
            deltaList = 0
            if count == num:
                self._xList
                break
            else:
                count += 1
            for i in range(self._len):
                tempSum = 0
                temp = 0
                for j in range(self._len):
                    if i != j:
                        tempSum += self._augMatrix[i][j] * self._xList[j]
                    else:
                        continue
                temp = self._xList[i]
                self._xList[i] = (self._augMatrix[i][-1] - tempSum) / \
                    self._augMatrix[i][i]
                deltaList += (self._xList[i] - temp)**2
            deltaList = pow(deltaList, 0.5)
        return self._xList

    def _initXList(self, xList):
        if len(xList) == 0:
            return [0 for i in range(self._len)]
        else:
            return xList
