# -*- coding: utf-8 -*-
'''
This module contains a class with the same name.
'''
from .lib import MatCal as mc
from .lib import Init as init
from .TriDecomposition import TriDecomposition as td


class Power(object):
    '''
    This class contains several power methods in order to
    solve the maximum or minimum eigenvalue according to the mold and
    the corresponding eigenvector.
    '''
    def __init__(self,
                 Matrix: list = [],
                 xList: list = [],
                 iteraNum: int = 100,
                 threshold: float = 0.000001) -> None:
        '''
        Matrix: You need to provide an matrix.
        If you do not provide the Matrix here,
        you must provide it at the function called
        setMatrix().\n
        XList: You need to provide an initialization eigenvector.
        If you do not provide the vector here,
        you must provide it at the function called
        setInitEigenvectors().\n
        iteraNum: You need to provide a number of iterations.
        If you don't provide, we will default to 100.\n
        threshold: You need to provide an error in ending iteration.
        If you don't provide, we will default to 1/1000000.
        '''
        self._matrix = Matrix
        self._row = len(Matrix)
        self._col = len(Matrix)
        self._xList = mc.vectorToMat(xList)
        self._iteraNum = iteraNum
        self._threshold = threshold

    def setMatrix(self, Matrix: list) -> None:
        '''
        Matrix: You need to provide an matrix.
        '''
        self._matrix = Matrix
        self._row = len(Matrix)
        self._col = len(Matrix)

    def getMatrix(self, mantissa: int = 3) -> list:
        '''
        return: We will return the Matrix.
        '''
        for i in range(self._row):
            for j in range(self._col):
                self._matrix[i][j] = round(self._matrix[i][j], mantissa)
        return self._matrix

    def setInitEigenvectors(self, xList: list) -> None:
        '''
        xList: You need to provide an initialization eigenvector.
        '''
        self._xList = mc.vectorToMat(xList)

    def getEigenvectors(self, mantissa: int = 3) -> list:
        '''
        return: We will return the calculated eigenvector.
        '''
        for i in range(self._row):
            for j in range(len(self._xList[0])):
                self._xList[i][j] = round(self._xList[i][j], mantissa)
        return self._xList

    def setIteraNum(self, iteraNum: int) -> None:
        '''
        iteraNum: You need to provide the number of iterations.
        '''
        self._iteraNum = iteraNum

    def getIteraNum(self) -> float:
        '''
        return: We will return the number of iterations.
        '''
        return self._iteraNum

    def setThreshold(self, threshold: float) -> None:
        '''
        threshold: You need to provide an error in ending iteration.
        '''
        self._threshold = threshold

    def getThreshold(self) -> float:
        '''
        retturn: We will return the error in ending iteration.
        '''
        return self._threshold

    def NorPower(self) -> float:
        '''
        Normalized power method.
        return: We will return the maximum eigenvalue according to the mold.\n
        '''
        count = 0
        deltaNum = 1
        maxEigenvalue = 0
        mu = 0
        while deltaNum > self._threshold:
            if count == self._iteraNum:
                break
            deltaNum = 0
            self._xList = mc.matMul(self._matrix,
                                    mc.matDivNum(self._xList,
                                                 mc.absMax(self._xList, 1)))
            maxEigenvalue = mc.absMax(self._xList, 1)
            deltaNum = abs(maxEigenvalue-mu)
            mu = maxEigenvalue
            count += 1
        return maxEigenvalue

    def OriginShift(self, lambda0: float = 0) -> float:
        '''
        Origin shift method.\n
        return: We will return the maximum eigenvalue according to the mold.\n
        '''
        shiftMat = init.Matrix(self._row, self._col)
        shiftMat = mc.matSub(self._matrix, init.Identity(self._row, lambda0))
        iteraNum = 0
        deltaNum = 1
        maxEigenvalue = 0
        mu = 0
        while deltaNum > self._threshold:
            if iteraNum == self._iteraNum:
                break
            deltaNum = 0
            self._xList = mc.matMul(shiftMat,
                                    mc.matDivNum(self._xList,
                                                 mc.absMax(self._xList, 1)))
            maxEigenvalue = mc.absMax(self._xList, 1)
            deltaNum = abs(maxEigenvalue-mu)
            mu = maxEigenvalue
            iteraNum += 1
        return maxEigenvalue + lambda0

    def Aitken(self) -> float:
        '''
        Aitken acceleration.\n
        return: We will return the maximum eigenvalue according to the mold.\n
        '''
        count = 0
        deltaNum = 1
        maxEigenvalue = 0
        mu = 1
        alpha0 = 0
        alpha1 = 0
        alpha2 = 0
        while deltaNum > self._threshold:
            if count == self._iteraNum:
                break
            deltaNum = 0
            self._xList = mc.matMul(self._matrix,
                                    mc.matDivNum(self._xList,
                                                 mc.absMax(self._xList, 1)))
            alpha2 = mc.absMax(self._xList, 1)
            maxEigenvalue = alpha0 - (pow(alpha1-alpha0, 2) /
                                      (alpha2-2*alpha1+alpha0))
            deltaNum = abs(maxEigenvalue-mu)
            alpha0 = alpha1
            alpha1 = alpha2
            mu = maxEigenvalue
            count += 1
        return maxEigenvalue

    def InversePower(self, appro: float = 0) -> float:
        '''
        Inverse power methond.\n
        return: We will return the minimum eigenvalue according to the mold.\n
        '''
        shiftMat = init.Matrix(self._row, self._col)
        shiftMat = mc.matSub(self._matrix, init.Identity(self._row, appro))
        dtd = td(shiftMat)
        count = 0
        deltaNum = 1
        minEigenvalue = 0
        mu = 1
        while deltaNum > self._threshold:
            if count == self._iteraNum:
                break
            deltaNum = 0
            dtd.setAugMat(init.AugMat(shiftMat,
                                      mc.matDivNum(self._xList,
                                                   mc.absMax(self._xList, 1))))
            self._xList = mc.vectorToMat(dtd.Doolittle())
            minEigenvalue = mc.absMax(self._xList, 1)
            deltaNum = abs(1/minEigenvalue-1/mu)
            mu = minEigenvalue
            count += 1
        self._xList = mc.matDivNum(self._xList, mc.absMax(self._xList, 1))
        return appro + 1/minEigenvalue
