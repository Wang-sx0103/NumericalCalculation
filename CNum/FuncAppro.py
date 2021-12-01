# -*- coding: utf-8 -*-
import lib.Init as init
from CNum.Elimination import Elimination as et


class Approximation (object):
    def __init__(self,
                 xList: list = [],
                 yList: list = []) -> None:
        self._xList = xList
        self._yList = yList
        self._len = len(xList)

    def setListX(self, xList) -> None:
        self._xList = xList

    def getListX(self) -> list:
        return self._xList

    def setListY(self, yList) -> None:
        self._yList = yList

    def getListY(self) -> list:
        return self._yList

    def geAugMat(self) -> list:
        return self._augMat

    def PolyFitting(self, n: int) -> list:
        self._conCoeffMat(n)
        alist = et(self._augMat).completeEliminate()
        return alist

    def _conCoeffMat(self, n: int) -> list:
        self._augMat = init.Matrix(n+1, n+2)
        for i in range(n+1):
            for j in range(i, n+1):
                for k in range(self._len):
                    self._augMat[i][j] += self._xList[k]**(j+i)
                    if j == n:
                        if i == 0:
                            self._augMat[i][-1] += self._yList[k]
                        else:
                            self._augMat[i][-1] += self._yList[k] * \
                                self._xList[k]**(i)
            self._augMat[j][i] = self._augMat[i][j]
        self._augMat[0][0] = self._len
