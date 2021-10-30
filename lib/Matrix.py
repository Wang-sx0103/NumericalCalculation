# -*- coding: utf-8 -*-


class Matrix(object):
    def __init__(self, row: int, col: int = 1):
        self._row = row
        self._col = col
        self._array: list = [[0]*col for _ in range(row)]

    def __setitem__(self, key, value: float):
        try:
            self._array[key[0]][key[1]] = value
        except IndexError:
            print("IndexError: Matrix assignment index out of range")

    def __getitem__(self, key):
        try:
            return self._array[key[0]][key[1]]
        except IndexError:
            print("IndexError: Matrix index out of range")

    def __len__(self) -> tuple:
        return (self._row, self._row)

    def __repr__(self) -> str:
        return '%r' % self._array

    def __add__(self, num: float) -> list:
        self._returnArray: list = [[0]*self._col for _ in range(self._row)]
        for i in range(self._row):
            for j in range(self._col):
                self._returnArray[i][j] = self._array[i][j]+num
        return self._returnArray

    def __sub__(self, num: float) -> list:
        self._returnArray: list = [[0]*self._col for _ in range(self._row)]
        for i in range(self._row):
            for j in range(self._col):
                self._returnArray[i][j] = self._array[i][j]-num
        return self._returnArray

    def __mul__(self, num: float) -> list:
        self._returnArray: list = [[0]*self._col for _ in range(self._row)]
        for i in range(self._row):
            for j in range(self._col):
                self._returnArray[i][j] = self._array[i][j]*num
        return self._returnArray

    def __truediv__(self, num: float) -> list:
        for i in range(self._row):
            for j in range(self._col):
                self._returnArray[i][j] = self._array[i][j]/num
        return self._returnArray
