# -*- coding: utf-8 -*-

'''
This module contains a class with the same name.
'''


class Root():
    '''
    This class contains several methods
    in order to solve the root of the nonlinear equation.
    '''
    def __init__(self) -> None:
        '''
        nothing!
        '''
        pass

    def Bisection(self,
                  callback,
                  interval: list,
                  iteraNum: int = 1000,
                  threshold: float = 0.000001) -> float:
        '''
        Inter-partition method.\n
        callback: This is a callback function.
        The integrand function needs to be provided by yourself.\n
        interval: You must provide a range as small as possible.\n
        threshold: You must provide an error in ending iteration.
        If you don't provide, we will default to 1/1000000.\n
        iteraNum: You need to provide a number of iterations.
        If you don't provide, we will default to 1000.\n
        return: We will return an approximation of the integrand.
        like this:\n
            import CNum
            def f(x) -> float:
                return x**3+10*X-20

            root = CNum.Root()
            root.Bisection(f, [1, 2])
        '''
        a = interval[0]
        b = interval[1]
        n = 0
        delta = iteraNum
        while delta > threshold:
            if n > iteraNum:
                break
            else:
                n += 1
            xn = (a+b)/2
            if callback(a)*callback(xn) < 0:
                b = xn
            else:
                a = xn
            delta = (b-a)/2
        return xn

    def Steffensen(self,
                   callback,
                   x0,
                   threshold: float = 0.000001,
                   iteraNum: int = 1000) -> float:
        '''
        Steffensen method is one of the simple iterative methods\n
        callback: This is a callback function.
        The integrand function needs to be provided by yourself.\n
        x0: You must provide a value as close as possible.\n
        threshold: You must provide an error in ending iteration.
        If you don't provide, we will default to 1/1000000.\n
        iteraNum: You need to provide a number of iterations.
        If you don't provide, we will default to 1000.\n
        return: We will return an approximation of the integrand.
        like this:\n
            import CNum
            def f(x) -> float:
                return x**3+10*X-20

            root = CNum.Root()
            root.Steffensen(f, 1.5)
        '''
        delta = iteraNum
        n = 0
        while delta > threshold:
            if n > iteraNum:
                break
            else:
                n += 1
            yn = callback(x0)
            zn = callback(x0)
            xn = x0 - ((yn - x0)**2/(zn-2*yn+x0))
            delta = abs(xn - x0)
            x0 = xn
        return xn

    def Newton(self,
               callback1,
               callback2,
               x0,
               threshold: float = 0.000001,
               iteraNum: int = 1000,) -> float:
        '''
        Newton method.\n
        callback1: This is a callback function.
        The function needs to be provided by yourself.\n
        callback2: This is a derivative function
        as well as callback function.\n
        x0: You must provide a value as close as possible.\n
        threshold: You must provide an error in ending iteration.
        If you don't provide, we will default to 1/1000000.\n
        iteraNum: You need to provide a number of iterations.
        If you don't provide, we will default to 1000.\n
        return: We will return an approximation of the integrand.
        like this:\n
            import CNum
            def f(x) -> float:
                return x**3+10*X-20

            root = CNum.Root()
            root.Newton(f, [1.5, 2])
        '''
        delta = iteraNum
        n = 0
        while delta > threshold:
            if n > iteraNum:
                break
            else:
                n += 1
            x = x0 - callback1(x0)/callback2(x0)
            delta = abs(x-x0)
            x0 = x
        return x

    def Secant(self,
               callback,
               initValue: list,
               threshold: float = 0.000001,
               iteraNum: int = 1000,) -> float:
        '''
        Secant.\n
        callback: This is a callback function.
        The integrand function needs to be provided by yourself.\n
        initValue: You need to provide two initial values
        as close to the zero point as possible in a list.\n
        threshold: You must provide an error in ending iteration.
        If you don't provide, we will default to 1/1000000.\n
        iteraNum: You need to provide a number of iterations.
        If you don't provide, we will default to 1000.\n
        return: We will return an approximation of the integrand.
        like this:\n
            import CNum
            def f(x) -> float:
                return x**3+10*X-20

            root = CNum.Root()
            root.Secant(f, 1.5)
        '''
        delta = iteraNum
        n = 0
        x0 = initValue[0]
        x1 = initValue[1]
        f0 = callback(x0)
        f1 = callback(x1)
        while delta > threshold:
            if n > iteraNum:
                break
            else:
                n += 1
            x = x1-(f1*(x1-x0))/(f1-f0)
            delta = abs(x-x1)
            x0 = x1
            x1 = x
            f0 = f1
            f1 = callback(x)
        return x
