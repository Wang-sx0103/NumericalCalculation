# -*- coding: utf-8 -*-
'''
Power
    This class contains several power methods in order to
    solve the maximum eigenvalue according to the mold and
    the corresponding eigenvector
Function list
    NorPower: Normalized power method
    OriginShift: Origin shift method
    Aitken: Aitken acceleration
    InversePower: Inverse power methond
'''
import lib.MatCal as mc
import lib.Init as init
import CNum.TriDecomposition as td


class Power(object):
    '''
    This class contains several power methods in order to
    solve the maximum eigenvalue according to the mold and
    the corresponding eigenvector
    '''
    def __init__(self,
                 Matrix: list = [],
                 xList: list = [],
                 iteraNum: int = 100,
                 threshold: float = 0.000001) -> None:
        '''
        Matrix: You need to provide an matrix, but this is't necessary.
        XList: You need to provide an initial value of X vector.
        If you do not provide the vector here,
        you must provide it at the function called
        setInitEigenvectors().
        iteraNum: You need to provide a number of iterations.
        If you don't provide, we will default to 100.
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
        self._matrix = Matrix
        self._row = len(Matrix)
        self._col = len(Matrix)

    def getMatrix(self, mantissa: int = 3) -> list:
        for i in range(self._row):
            for j in range(self._col):
                self._matrix[i][j] = round(self._matrix[i][j], mantissa)
        return self._matrix

    def setInitEigenvectors(self, xList: list) -> None:
        self._xList = mc.vectorToMat(xList)

    def getEigenvectors(self, mantissa: int = 3) -> list:
        for i in range(self._row):
            for j in range(len(self._xList[0])):
                self._xList[i][j] = round(self._xList[i][j], mantissa)
        return self._xList

    def setIteraNum(self, iteraNum: int) -> None:
        self._iteraNum = iteraNum

    def getIteraNum(self) -> float:
        return self._iteraNum

    def setThreshold(self, threshold: float) -> None:
        self._threshold = threshold

    def getThreshold(self) -> float:
        return self._threshold

    # 规范化幂法
    def NorPower(self, mantissa: int = 3) -> float:
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
        return round(maxEigenvalue, mantissa)

    # 原点移位法
    def OriginShift(self, lambda0: float = 0, mantissa: int = 3) -> float:
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
        return round(maxEigenvalue + lambda0, mantissa)

    # Aitken加速法 Aitken acceleration
    def Aitken(self, mantissa: int = 3) -> float:
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
        return round(maxEigenvalue, mantissa)

    # 反幂法 Inverse power methond
    def InversePower(self, appro: float = 0, mantissa: int = 3) -> float:
        shiftMat = init.Matrix(self._row, self._col)
        shiftMat = mc.matSub(self._matrix, init.Identity(self._row, appro))
        dtd = td.TriDecomposition(shiftMat)
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
        return round(appro + 1/minEigenvalue, mantissa)
