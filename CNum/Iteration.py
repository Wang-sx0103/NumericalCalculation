# -*- coding: utf-8 -*-
import lib.Init as init


class Iteration(object):
    def __init__(self, augMatrix, xList=[]):
        self._augMatrix = augMatrix
        self._len = len(self._augMatrix)
        self._xList = init.vector(xList)

    def Jacobi(self, num=100, delta=0.00001):
        count = 0
        deltaList = 1
        while deltaList > delta:
            deltaList = 0
            if count == num:
                self._xList
                break
            else:
                count += 1
            lastXList = self._xList[:]
            for i in range(self._len):
                tempSum = 0
                for j in range(self._len):
                    if i != j:
                        tempSum += self._augMatrix[i][j] * lastXList[j]
                    else:
                        continue
                self._xList[i] = (self._augMatrix[i][-1] - tempSum) / \
                    self._augMatrix[i][i]
                deltaList += (self._xList[i] - lastXList[i])**2
            deltaList = pow(deltaList, 0.5)
        return self._xList

    def GaussSeidel(self, num=100, delta=0.00001):
        count = 0
        deltaList = 1
        while deltaList > delta:
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

    def SOR(self, num=100, delta=0.00001, omega=1):
        count = 0
        deltaList = 1
        while deltaList > delta:
            deltaList = 0
            if count == num:
                self._xList
                break
            else:
                count += 1
            lastXList = self._xList[:]
            for i in range(self._len):
                tempSum = 0
                for j in range(self._len):
                    if i != j:
                        tempSum += self._augMatrix[i][j] * self._xList[j]
                    else:
                        continue
                self._xList[i] = (1 - omega) * lastXList[i] + \
                    omega * (self._augMatrix[i][-1] - tempSum) / \
                    self._augMatrix[i][i]
                deltaList += (self._xList[i] - lastXList[i])**2
            deltaList = pow(deltaList, 0.5)
        return self._xList
