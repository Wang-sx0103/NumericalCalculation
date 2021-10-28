# -*- coding: utf-8 -*-
import lib.Init as init
import lib.MatCal as mc


class Power(object):
    def __init__(self, Matrix: list = [], xList: list = []):
        self._matrix = Matrix
        self._len = len(Matrix)
        self._xList = xList

    def setMatrix(self, Matrix: list):
        self._matrix = Matrix

    def getMatrix(self):
        return self._matrix

    def setInitEigenvectors(self, xList: list):
        self._xList = mc.vectorToMat(init.initList(xList))

    def getEigenvectors(self):
        return self._xList

    # 规范化幂法
    def NorPower(self, num=100, delta=0.000001):
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
