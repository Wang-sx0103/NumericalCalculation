# -*- coding: utf-8 -*-
'''
This module contains a class with the same name.
'''


class Integral():
    '''
    This class contains several quadrature methods in order to
    calculate the approximation of the integrand.\n
    But The integrand function needs to be provided by yourself.
    '''
    def __init__(self, endPoint: list = []) -> None:
        '''
        endPoint: You need to provide the value
        of the endpoint of the integral interval.
        If you do not provide the vector here,
        you must provide it at the function called
        "setEndPoint".\n
        '''
        self._leftPoint = endPoint[0]
        self._rightPoint = endPoint[1]

    def setEndPoint(self, endPoint: list) -> None:
        '''
        endPoint: You can provide the value
        of the endpoint of the integral interval.
        '''
        self._leftPoint = endPoint[0]
        self._rightPoint = endPoint[1]

    def Trapezoid(self, callback, num: int = 1) -> float:
        '''
        Composite Trapezoidal rule.\n
        callback: This is a callback function.\n
        The integrand function needs to be provided by yourself.\n
        num: Number of interval bisections.
        If you don't provide, we will default to 1.\n
        return: We will return an approximation of the integrand.
        like this:\n
            def f(x) -> float:
                return a+b*x

            itg = CNum.Integral([0, 1])
            itg.Trapezoid(f, 10)
        '''
        sumfx = 0
        h = (self._rightPoint - self._leftPoint)/num
        for i in range(1, num):
            xi = self._leftPoint+i*h
            sumfx += callback(xi)
        Tn = (h/2)*(callback(self._leftPoint)+callback(self._rightPoint) +
                    2*sumfx)
        return Tn

    def Simpson(self, callback, half: int = 1) -> float:
        '''
        Composite Simpson rule.\n
        callback: This is a callback function.\n
        The integrand function needs to be provided by yourself.\n
        half: Half of number of interval bisections.
        So the actual number of intervals is twice that of "half".
        If you don't provide, we will default to 1.\n
        return: We will return an approximation of the integrand.
        like this:\n
            def f(x) -> float:
                return a+b*x

            itg = CNum.Integral([0, 1])
            itg.Simpson(f, 10)
        '''
        num = 2*half
        sumfx2k = 0
        sumfx2ks1 = 0
        h = (self._rightPoint - self._leftPoint)/num
        for i in range(1, num):
            if i % 2 == 0:
                xi = self._leftPoint+i*h
                sumfx2k += callback(xi)
            else:
                xi = self._leftPoint+i*h
                sumfx2ks1 += callback(xi)
        Sn = (h/3)*(callback(self._leftPoint)+callback(self._rightPoint) +
                    2*sumfx2k + 4*sumfx2ks1)
        return Sn

    def TrapezoidHalf(self,
                      callback,
                      threshold: float = 0.000001,
                      iteraNum: int = 1000) -> float:
        '''
        Successive half division algorithm of Trapezoidal function.\n
        callback: This is a callback function.\n
        The integrand function needs to be provided by yourself.\n
        threshold: You must provide an error in ending iteration.
        If you don't provide, we will default to 1/1000000.\n
        iteraNum: You need to provide a number of iterations.
        If you don't provide, we will default to 1000.\n
        return: We will return an approximation of the integrand.
        like this:\n
            def f(x) -> float:
                return a+b*x

            itg = CNum.Integral([0, 1])
            itg.TrapezoidHalf(f, 10, 0.00001, 100)
        '''
        m = 1
        count = t = t0 = 0
        h = (self._rightPoint-self._leftPoint)/2
        t0 = h*(callback(self._leftPoint)+callback(self._rightPoint))
        delta = iteraNum
        while delta > 3*threshold:
            if iteraNum < count:
                break
            else:
                count += 1
            f = 0
            k = 2**(m-1)
            for i in range(1, k+1):
                f += callback(self._leftPoint+(2*i - 1)*h)
            t = 0.5*t0 + h*f
            delta = abs(t-t0)
            m = m+1
            h = h/2
            t0 = t
        return t

    def SimpsonHalf(self,
                    callback,
                    threshold: float = 0.000001,
                    iteraNum: int = 1000) -> float:
        '''
        Successive half division algorithm of Simpson function.\n
        callback: This is a callback function.\n
        The integrand function needs to be provided by yourself.\n
        threshold: You must provide an error in ending iteration.
        If you don't provide, we will default to 1/1000000.\n
        iteraNum: You need to provide a number of iterations.
        If you don't provide, we will default to 1000.\n
        return: We will return an approximation of the integrand.
        like this:\n
            def f(x) -> float:
                return a+b*x

            itg = CNum.Integral([0, 1])
            itg.SimpsonHalf(f, 10)
        '''
        count = s = s0 = 0
        f1 = (self._rightPoint+self._leftPoint)
        f2 = callback((self._rightPoint+self._leftPoint)/2)
        s0 = ((self._rightPoint-self._leftPoint)/6)*(f1+4*f2)
        m = 2
        h = (self._rightPoint-self._leftPoint)/4
        delta = iteraNum
        while delta > 15*threshold:
            if iteraNum < count:
                break
            else:
                count += 1
            f3 = 0
            k = 2**(m-1)
            for i in range(1, k+1):
                f3 += callback(self._leftPoint+(2*i - 1)*h)
            s = (f1+2*f2+4*f3)*h/3
            delta = abs(s-s0)
            m = m+1
            h = h/2
            f2 = f2+f3
            s0 = s
        return s

    def Romberg(self,
                callback,
                threshold: float = 0.000001,
                iteraNum: int = 1000) -> float:
        '''
        Romberg quadrature formula, also called
        Successive half acceleration method.\n
        callback: This is a callback function.\n
        The integrand function needs to be provided by yourself.\n
        threshold: You must provide an error in ending iteration.
        If you don't provide, we will default to 1/1000000.\n
        iteraNum: You need to provide a number of iterations.
        If you don't provide, we will default to 1000.\n
        return: We will return an approximation of the integrand.
        like this:\n
            def f(x) -> float:
                return a+b*x

            itg = CNum.Integral([0, 1])
            itg.Romberg(f, 10)
        '''
        count = 0
        h = self._rightPoint - self._leftPoint
        TMat = []
        t00 = (callback(self._rightPoint)+callback(self._leftPoint))*h/2
        TMat.append([t00])
        k = 1
        delta = iteraNum
        while delta > threshold:
            if iteraNum < count:
                break
            else:
                count += 1
            sumf = 0
            for i in range(1, 2**(k-1)+1):
                sumf += callback(self._leftPoint+(i-0.5)*h)
            t0k = 0.5*(TMat[k-1][0]+h*sumf)
            TMat.append([t0k])
            for j in range(1, k+1):
                tkj = (4**j*TMat[k][j-1]-TMat[k-1][j-1])/(4**j-1)
            TMat[k].append(tkj)
            delta = abs(TMat[k][-1] - TMat[k][-1])
            resultT = TMat[k][-1]
            h = h/2
            k = k+1
        return resultT
