# -*- coding: utf-8 -*-
import lib.Init as init


class Interpolation(object):
    def __init__(self,
                 xList: list = [],
                 yList: list = [],
                 yDer1th: list = []) -> None:
        self._xList = xList
        self._yList = yList
        self._yDer1th = yDer1th
        self._len = len(xList)

    def setKPoints(self, KnowPoints: list) -> None:
        self._xList = KnowPoints[0]
        self._yList = KnowPoints[1]
        self._yDer1th = KnowPoints[2]

    def setListX(self, xList: list) -> None:
        self._xList = xList
        self._len = len(xList)

    def getListX(self) -> list:
        return self._xList

    def setListY(self, yList: list) -> None:
        self._yList = yList

    def getListY(self) -> list:
        return self._yList

    def setListYDer1th(self, yDer1th: list) -> None:
        self._yDer1th = yDer1th

    def getListYDer1th(self) -> list:
        return self._yDer1th

    # Lagrangian Interpolation Method
    # 拉格朗日插值法
    def Lagrange(self, x: float) -> float:
        self._l = self._LagIBF(x)
        L = 0
        for i in range(self._len):
            L += self._l[i]*self._yList[i]
        return L

    # Newtow Interpolation Method
    # 牛顿插值法
    def Newton(self, x: float) -> float:
        self._diffQuo = self._DiffQuotient()
        N = self._diffQuo[0]
        for i in range(1, self._len):
            N += self._diffQuo[i]*self._xSubX(x, i)
        return N

    # Hermite Interpolation Method
    # 埃尔米特三次插值
    def Hermite(self, x: float) -> float:
        x0 = self._xList[0]
        x1 = self._xList[1]
        y0 = self._xList[0]
        y1 = self._xList[1]
        yDer0 = self._xList[0]
        yDer1 = self._xList[1]
        return (1+2*(x-x0)/(x1-x0))*((x-x1)/(x0-x1)**2)*y0 + \
            (1+2*(x-x1)/(x0-x1))*((x-x0)/(x1-x0)**2)*y1 + \
            (x-x0)*(((x-x1)/(x0-x1))**2)*yDer0 + \
            (x-x1)*(((x-x0)/(x1-x0))**2)*yDer1

    # Used to generate Lagrange basis functions
    # 用于生成拉格朗日基函数
    def _LagIBF(self, x: float) -> list:
        resultVector = init.vector(self._len)
        for i in range(self._len):
            lagIBF = 1
            for j in range(self._len):
                if i != j:
                    lagIBF *= ((x-self._xList[j]) /
                               (self._xList[i]-self._xList[j]))
            resultVector[i] = lagIBF
        return resultVector

    # Used to construct difference quotient
    # 用于构建差商
    def _DiffQuotient(self) -> list:
        resultVector = init.vector(self._len)
        resultVector[0] = self._yList[0]
        for i in range(1, self._len):
            diffQuo = 0
            for j in range(i+1):
                diffQuo += self._yList[j]/self._xSubX(self._xList[j], i+1, j)
            resultVector[i] = diffQuo
        return resultVector

    def _xSubX(self,
               x: float,
               size: int,
               index: int = -1) -> float:
        xSubX = 1
        for i in range(size):
            if i != index:
                xSubX *= x - self._xList[i]
        return xSubX
