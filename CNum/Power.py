# -*- coding: utf-8 -*-

import lib.MatCal as mc


class Power(object):
    def __init__(self,
                 Matrix: list = [],
                 xList: list = [],
                 IteraNum: int = 100,
                 threshold: float = 0.000001) -> None:

        self._matrix = Matrix
        self._len = len(Matrix)
        self._xList = mc.vectorToMat(xList)
        self._IteraNum = IteraNum
        self._threshold = threshold

    def setMatrix(self, Matrix: list) -> None:
        self._matrix = Matrix

    def getMatrix(self) -> list:
        return self._matrix

    def setInitEigenvectors(self, xList: list) -> None:
        self._xList = mc.vectorToMat(xList)

    def getEigenvectors(self) -> list:
        return self._xList

    def setIteraNum(self, IteraNum: int) -> None:
        self._IteraNum = IteraNum

    def getIteraNum(self) -> float:
        return self._IteraNum

    def setThreshold(self, threshold: float) -> None:
        self._threshold = threshold

    def getThreshold(self) -> float:
        return self._threshold

    # 规范化幂法
    def NorPower(self, num=100, delta=0.000001) -> float:
        count = 0
        deltaNum = 1
        lambda0 = 0
        mu = 0
        while deltaNum > delta:
            if count == num:
                break
            deltaNum = 0
            tempY = mc.matDivNum(self._xList, mc.absMax(self._xList, 1))
            self._xList = mc.matMul(self._matrix, tempY)
            lambda0 = mc.absMax(self._xList, 1)
            deltaNum = abs(lambda0-mu)
            mu = lambda0
            count += 1
        return lambda0
