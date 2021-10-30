# -*- coding: utf-8 -*-

import lib.MatCal as mc
import lib.Init as init
import CNum.TriDecomposition as td


class Power(object):
    def __init__(self,
                 Matrix: list = [],
                 xList: list = [],
                 iteraNum: int = 100,
                 threshold: float = 0.000001) -> None:

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

    def getMatrix(self) -> list:
        return self._matrix

    def setInitEigenvectors(self, xList: list) -> None:
        self._xList = mc.vectorToMat(xList)

    def getEigenvectors(self) -> list:
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
    def NorPower(self) -> float:
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

    # 原点移位法
    def OriginShift(self, lambda0: float = 0):
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

    # Aitken加速法 Aitken acceleration
    def AitkenAcc(self) -> float:
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

    # 反幂法 Inverse power methond
    def InversePower(self, appro: float = 0) -> float:
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
            shiftMat = init.AugMat(shiftMat,
                                   mc.matDivNum(self._xList,
                                                mc.absMax(self._xList, 1)))
            dtd.setAugMat(shiftMat)
            self._xList = mc.vectorToMat(dtd.DirTriDecomposition())
            minEigenvalue = mc.absMax(self._xList, 1)
            deltaNum = abs(1/minEigenvalue-1/mu)
            mu = minEigenvalue
            count += 1
        self._xList = mc.matDivNum(self._xList, mc.absMax(self._xList, 1))
        return appro + 1/minEigenvalue
