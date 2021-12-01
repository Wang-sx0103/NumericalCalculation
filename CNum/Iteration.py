# -*- coding: utf-8 -*-

'''
Iteration
    This class contains several iterative methods for solving linear equations.
Function list
    Jacobi: Jacob Iterative method.
    GaussSeidel: Gauss-Seidel Iteration.
    SOR: Successive Over - Relaxation Iteration.
'''


class Iteration(object):
    '''
    This class contains several iterative methods for solving linear equations
    '''
    def __init__(self,
                 augMatrix: list = [],
                 xList: list = [],
                 iteraNum: int = 100,
                 threshold: float = 0.000001,
                 relaxaFactor: float = 1) -> None:
        '''
        augMatrix: You need to provide an augmented matrix,
        but this is't necessary.
        xList: You need to provide an iterative initial value of X vector,
        but this is't necessary.
        iteraNum: You need to provide a number of iterations.
        If you don't provide, we will default to 100.
        threshold: You need to provide an error in ending iteration.
        If you don't provide, we will default to 1/1000000.
        relaxaFactor: When you use the Successive Over-Relaxation Iteration,
        you need to provide a relaxation factor
        '''
        self._augMatrix = augMatrix
        self._len = len(self._augMatrix)
        self._xList = xList
        self._IteraNum = iteraNum
        self._threshold = threshold
        self._relaxaFactor = relaxaFactor

    def setAugMat(self, augMat: list) -> None:
        self._augMatrix = augMat

    def getAugMat(self) -> list:
        return self._augMatrix

    def setIteraValue(self, xList: list) -> None:
        self._xList = xList

    def getIteraResults(self) -> list:
        return self._xList

    def setIteraNum(self, IteraNum: int) -> None:
        self._IteraNum = IteraNum

    def getIteraNum(self) -> float:
        return self._IteraNum

    def setThreshold(self, threshold: float) -> None:
        self._threshold = threshold

    def getThreshold(self) -> float:
        return self._threshold

    def setRelaxaFactor(self, relaxaFactor: float) -> None:
        self._relaxaFactor = relaxaFactor

    def getRelaxaFactor(self) -> float:
        return self._relaxaFactor

    # 雅各比迭代法 Jocobi Iteration

    def Jacobi(self) -> list:
        count = 0
        deltaList = 1
        while deltaList > self._threshold:
            deltaList = 0
            if count == self._IteraNum:
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

    # 高斯-赛德尔迭代法 Gauss-Seidel Iteration

    def GaussSeidel(self) -> list:
        count = 0
        deltaList = 1
        while deltaList > self._threshold:
            deltaList = 0
            if count == self._IteraNum:
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

    # 松弛法 Successive Over - Relaxation Iteration

    def SOR(self, omega=1) -> list:
        count = 0
        deltaList = 1
        while deltaList > self._threshold:
            deltaList = 0
            if count == self._IteraNum:
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
