# -*- coding: utf-8 -*-
'''
This module contains a class with the same name.
'''
from .lib import Init as init
from .Elimination import Elimination as et


class FuncAppro ():
    '''
    This class contains a methods in order to construct an n-order polynomial.
    '''
    def __init__(self,
                 xList: list = [],
                 yList: list = []) -> None:
        '''
        xList: You need to provide a set of x-points.
        need to provide
        yList: You need to provide a set of y-points.
        If you do not provide the vector here,
        you must provide it at the function called
        setListY().\n
        The length of "xList" must be equal to "yList".
        '''
        self._xList = xList
        self._yList = yList
        self._len = len(xList)

    def setListX(self, xList) -> None:
        '''
        xList: You can provide a set of x-points.
        '''
        self._xList = xList

    def getListX(self) -> list:
        '''
        return: We will return a list contain all x-points.
        '''
        return self._xList

    def setListY(self, yList) -> None:
        '''
        yList: You can provide a set of y-points.
        '''
        self._yList = yList

    def getListY(self) -> list:
        '''
        return: We will return a list contain all y-points.
        '''
        return self._yList

    def geAugMat(self) -> list:
        '''
        return: We will return the coefficient matrix of the normal equations.
        Its size: (order, order+1)
        '''
        return self._augMat

    def PolyFitting(self, order: int) -> list:
        '''
        Fitting an n-order polynomial.\n
        order: It represents the order of the fitting polynomial,
        you must provide an integer less than the number of coordinates.\n
        return: We will return a list with a length of "order"+1.\n
        It represents the coefficients of the fitting polynomial
        from low to high.
        '''
        self._augMat = self._conCoeffMat(order)
        coefficientList = et(self._augMat).completeEliminate()
        return coefficientList

    def _conCoeffMat(self, n: int) -> list:
        resultMat = init.Matrix(n+1, n+2)
        for i in range(n+1):
            for j in range(i, n+1):
                for k in range(self._len):
                    resultMat[i][j] += self._xList[k]**(j+i)
                    if j == n:
                        if i == 0:
                            resultMat[i][-1] += self._yList[k]
                        else:
                            resultMat[i][-1] += self._yList[k] * \
                                self._xList[k]**(i)
            resultMat[j][i] = resultMat[i][j]
        resultMat[0][0] = self._len
        return resultMat
