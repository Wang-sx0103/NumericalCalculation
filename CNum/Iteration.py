# -*- coding: utf-8 -*-

'''
This module contains a class with the same name.
'''


class Iteration():
    '''
    This class contains several iterative methods
    in order to solve linear equations.
    '''
    def __init__(self,
                 augMat: list = [],
                 xList: list = [],
                 iteraNum: int = 100,
                 threshold: float = 0.000001) -> None:
        '''
        augMat: You need to provide an augmented matrix,
        If you do not provide the augMatrix here,
        you must provide it at the function called
        setAugMat().\n
        xList: You need to provide an iterative initial value of XList,
        If you do not provide the list here,
        you must provide it at the function called
        setIteraValue().\n
        iteraNum: You need to provide a number of iterations.
        If you don't provide, we will default to 100.\n
        threshold: You need to provide an error in ending iteration.
        If you don't provide, we will default to 1/1000000.\n
        '''
        self._augMatrix = augMat
        self._len = len(augMat)
        self._xList = xList
        self._IteraNum = iteraNum
        self._threshold = threshold

    def setAugMat(self, augMat: list) -> None:
        '''
        augMat: You can provide an augmented matrix.
        '''
        self._augMatrix = augMat
        self._len = len(self._augMatrix)

    def getAugMat(self) -> list:
        '''
        return: We will return an augmented matrix..
        '''
        return self._augMatrix

    def setIteraValue(self, xList: list) -> None:
        '''
        XList: You need to provide the initial value of the iteration.
        '''
        self._xList = xList

    def getIteraResults(self) -> list:
        '''
        return: We will return the iteration results.
        '''
        return self._xList

    def setIteraNum(self, IteraNum: int) -> None:
        '''
        IteraNum: You need to provide the number of iterations.
        '''
        self._IteraNum = IteraNum

    def getIteraNum(self) -> float:
        '''
        return: We will return the number of iterations.
        '''
        return self._IteraNum

    def setThreshold(self, threshold: float) -> None:
        '''
        threshold: You need to provide an error in ending iteration.
        '''
        self._threshold = threshold

    def getThreshold(self) -> float:
        '''
        return: We will return the error in ending iteration.
        '''
        return self._threshold

    def Jacobi(self) -> list:
        '''
        Jacob Iterative method.\n
        return: We will return the solution of the equations as a list.
        '''
        count = 0
        deltaList = 1
        while deltaList > self._threshold:
            deltaList = 0
            if count == self._IteraNum:
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

    def GaussSeidel(self) -> list:
        '''
        Gauss-Seidel Iteration.\n
        return: We will return the solution of the equations as a list.
        '''
        count = 0
        deltaList = 1
        while deltaList > self._threshold:
            deltaList = 0
            if count == self._IteraNum:
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

    def SOR(self, omega: float = 1) -> list:
        '''
        Successive Over - Relaxation Iteration.\n
        omega: you need to provide a Relaxation factor.
        If you don't provide, we will default to 100.\n
        return: We will return the solution of the equations as a list.
        '''
        count = 0
        deltaList = 1
        while deltaList > self._threshold:
            deltaList = 0
            if count == self._IteraNum:
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
