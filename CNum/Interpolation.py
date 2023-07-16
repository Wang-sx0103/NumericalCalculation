# -*- coding: utf-8 -*-
'''
This module contains a class with the same name.
'''
from .lib import Init as init
from .lib import MatCal as mc
from .TriDecomposition import TriDecomposition as td


class Interpolation():
    '''
    This class contains several interpolation methods in order to
    construct the interpolation polynomial function and
    calculate the value at X-point.
    '''
    def __init__(self,
                 xList: list = None,
                 yList: list = None) -> None:
        '''
        xList: You need to provide a set of x-points.
        If you do not provide the vector here,
        you must provide it at the function called
        "setListX" or "setKPoints".\n
        yList: You need to provide a set of y-points.
        If you do not provide the vector here,
        you must provide it at the function called
        "setListY" or "setKPoints".\n
        The length of "xList" must be equal to "yList".
        '''
        self._xList = xList
        self._yList = yList
        self._len = len(xList)
        self._l = []
        self._diffQuo = []

    def setKPoints(self, KnowPoints: list) -> None:
        '''
        knowPoints: You can provide a list of 2-rows and N-columns.
        '''
        self._xList = KnowPoints[0]
        self._yList = KnowPoints[1]

    def setListX(self, xList: list) -> None:
        '''
        xList: You can provide a set of x-points.
        '''
        self._xList = xList
        self._len = len(xList)

    def getListX(self) -> list:
        '''
        return: We will return a list contain all x-points.
        '''
        return self._xList

    def setListY(self, yList: list) -> None:
        '''
        yList: You can provide a set of y-points.
        '''
        self._yList = yList
        self._len = len(yList)

    def getListY(self) -> list:
        '''
        return: We will return a list contain all x-points.
        '''
        return self._yList

    def Lagrange(self, x: float) -> float:
        '''
        Lagrangian Interpolation Method.\n
        x: You must provide a real number.\n
        return: We will return the value at x-point
        calculated by this interpolation method.
        '''
        self._l = self._LagIBF(x)
        L = 0
        for i in range(self._len):
            L += self._l[i]*self._yList[i]
        return L

    def Newton(self, x: float) -> float:
        '''
        Newtow Interpolation Method.\n
        x: You must provide a real number
        return: We will return the value at x-point
        calculated by this interpolation method.
        '''
        self._diffQuo = self._DiffQuotient()
        N = self._diffQuo[0]
        for i in range(1, self._len):
            N += self._diffQuo[i]*self._xSubX(x, i)
        return N

    def Hermite(self, x: float, yDer1th: list) -> float:
        '''
        Hermite Interpolation Method.\n
        x: You must provide a real number.\n
        yDer1th: You need to provide a set of first derivative values
        at both ends of the XList in a list.
        return: We will return the value at x-point
        calculated by this interpolation method.
        '''
        x0 = self._xList[0]
        x1 = self._xList[1]
        y0 = self._xList[0]
        y1 = self._xList[1]
        yDer0 = yDer1th[0]
        yDer1 = yDer1th[1]
        return (1+2*(x-x0)/(x1-x0))*((x-x1)/(x0-x1)**2)*y0 + \
            (1+2*(x-x1)/(x0-x1))*((x-x0)/(x1-x0)**2)*y1 + \
            (x-x0)*(((x-x1)/(x0-x1))**2)*yDer0 + \
            (x-x1)*(((x-x0)/(x1-x0))**2)*yDer1

    def CubicSpline(self, x: float,
                    flag: int,
                    endpointDer: list = None) -> float:
        '''
        Spline Interpolation Method.\n
        This method constructs the interpolation function
        through the three-rotations equation.\n
        flag: First derivative value at given two end points.\n
            0: First derivative value at given two end points.
            1: Periodic function.
            2: Second derivative value at given two end points.\n
        endPointDer:  You need to provide a set of derivative values
        at both ends of the XList in a list.\n
        return: We will return the value at x point
        calculated by this interpolation method.
        '''
        sdm: list = self._secondDerMat(endpointDer, flag)
        j: int = self._findIndex(x)
        hj: float = self._xList[j+1] - self._xList[j]
        return sdm[j+1]*((x-self._xList[j])**3)/(6*hj) -\
            sdm[j]*((x-self._xList[j+1])**3)/(6*hj) +\
            (self._yList[j+1]-(sdm[j+1]*hj**2)/6) *\
            ((x-self._xList[j])/hj) -\
            (self._yList[j]-(sdm[j]*hj**2)/6) *\
            ((x-self._xList[j+1])/hj)

    # Used to generate Lagrange basis functions
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

    def _secondDerMat(self, endpointDer: list, flag: int) -> list:
        a = init.vector(self._len)
        b = init.vector(self._len)
        c = init.vector(self._len)
        MList = init.vector(self._len)
        for j in range(1, self._len-1):
            hjs1: float = self._xList[j] - self._xList[j-1]
            hj: float = self._xList[j+1] - self._xList[j]
            a[j] = hjs1/(hjs1+hj)
            b[j] = hj/(hjs1+hj)
            c[j] = 6*((self._yList[j+1]-self._yList[j])/hj -
                      (self._yList[j]-self._yList[j-1])/hjs1)/(hjs1+hj)
        if flag == 0:
            b[0] = 1
            a[-1] = 1
            h0 = self._xList[1]-self._xList[0]
            hns1 = self._xList[-1]-self._xList[-2]
            c[0] = (6/h0)*((self._yList[1]-self._yList[0])/h0-endpointDer[0])
            c[-1] = (6/hns1)*(endpointDer[-1] - (self._yList[-1] -
                                                 self._yList[-2])/hns1)
            augMat = init.AugMat(self._coeMat(a, b, flag), mc.vectorToMat(c))
            MList = td(augMat).Chase()
            return MList
        elif flag == 2:
            a = a[1:]
            b = b[1:]
            c = c[1:]
            c[0] = c[0] - a[0]*endpointDer[0]
            c[-2] = c[-2] - b[-2]*endpointDer[-1]
            augMat = init.AugMat(self._coeMat(a, b, flag), mc.vectorToMat(c))
            MList[1:-1] = td(augMat).Chase()
            MList[0] = endpointDer[0]
            MList[-1] = endpointDer[-1]
            return MList
        elif flag == 1:
            a = a[1:]
            b = b[1:]
            c = c[1:]
            h0 = self._xList[1]-self._xList[0]
            hns1 = self._xList[-1]-self._xList[-2]
            a[-1] = hns1/(h0 + hns1)
            b[-1] = h0/(h0 + hns1)
            c[-1] = (6/h0+hns1)*((self._yList[1] - self._yList[0])/h0 -
                                 (self._yList[-1] - self._yList[-2])/hns1)
            augMat = init.AugMat(self._coeMat(a, b, flag), mc.vectorToMat(c))
            MList[1:] = td(augMat).Chase()
            MList[0] = endpointDer[0]
            return MList

    def _findIndex(self, x: float) -> int:
        for i in range(self._len-1):
            if x >= self._xList[i] and x <= self._xList[i+1]:
                return i
            elif x < min(self._xList):
                return 0
            elif x > max(self._xList):
                return self._len-2

    def _coeMat(self, alpha: list, beta: list, flag: int) -> list:
        size = self._len - flag
        resultMat = init.Identity(size, 2)
        for i in range(size):
            if i == 0:
                resultMat[i][i+1] = beta[i]
            elif i == size - 1:
                resultMat[i][i-1] = alpha[i]
            else:
                resultMat[i][i-1] = alpha[i]
                resultMat[i][i+1] = beta[i]
        if flag == 1:
            resultMat[0][-1] = alpha[0]
            resultMat[-1][0] = beta[-1]
        return resultMat
