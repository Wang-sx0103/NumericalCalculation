# -*- coding: utf-8 -*-
from __future__ import annotations


class Matrix(object):
    def __init__(self, row: int, col: int = 1):
        self._row = row
        self._col = col
        self._itera = 0
        self._array: list = [[0]*col for _ in range(row)]

    def __setitem__(self, key, value: float):
        try:
            if isinstance(key[0], int) and isinstance(key[1], int):
                self._array[key[0]][key[1]] = value
            else:
                if key[0].start is None:
                    index1Start = 0
                else:
                    index1Start = key[0].start
                if key[0].stop is None:
                    index1Stop = self._row
                else:
                    index1Stop = key[0].stop
                if key[0].step is None:
                    index1Step = 1
                else:
                    index1Step = key[0].step

                if key[1].start is None:
                    index2Start = 0
                else:
                    index2Start = key[1].start
                if key[1].stop is None:
                    index2Stop = self._col
                else:
                    index2Stop = key[1].stop
                if key[1].step is None:
                    index2Step = 1
                else:
                    index2Step = key[1].step
                c1 = 0
                c2 = 0
                for i in range(index1Start, index1Stop, index1Step):
                    for j in range(index2Start, index2Stop, index2Step):
                        self._array[i][j] = value[c1][c2]
                        c2 += 1
                    c1 += 1
                    c2 = 0
        except IndexError:
            print("IndexError: Matrix assignment index out of range")

    def __getitem__(self, key) -> float:
        try:
            if isinstance(key[0], int) and isinstance(key[1], int):
                return self._array[key[0]][key[1]]
            else:
                if key[0].start is None:
                    index1Start = 0
                else:
                    index1Start = key[0].start
                if key[0].stop is None:
                    index1Stop = self._row
                else:
                    index1Stop = key[0].stop
                if key[0].step is None:
                    index1Step = 1
                else:
                    index1Step = key[0].step

                if key[1].start is None:
                    index2Start = 0
                else:
                    index2Start = key[1].start
                if key[1].stop is None:
                    index2Stop = self._col
                else:
                    index2Stop = key[1].stop
                if key[1].step is None:
                    index2Step = 1
                else:
                    index2Step = key[1].step
                return self._array[index1Start:
                                   index1Stop:
                                   index1Step][
                                   index2Start,
                                   index2Stop,
                                   index2Step]
        except IndexError:
            print("IndexError: Matrix index out of range")

    def __len__(self) -> tuple:
        return (self._row, self._row)

    def __repr__(self) -> str:
        rep = "size:" + str(self._row) + chr(215) + str(self._row) + "\n"
        for i in range(self._row):
            if i == self._row - 1:
                rep += str(self._array[i])
            else:
                rep += str(self._array[i]) + "\n"
        return rep

    def __str__(self) -> str:
        return self.__repr__()

    def __add__(self, num: float) -> None:
        for i in range(self._row):
            for j in range(self._col):
                self._array[i][j] = self._array[i][j]+num

    def __sub__(self, num: float) -> None:
        for i in range(self._row):
            for j in range(self._col):
                self._array[i][j] = self._array[i][j]-num

    def __mul__(self, num: float) -> None:
        for i in range(self._row):
            for j in range(self._col):
                self._array[i][j] = self._array[i][j]*num

    def __truediv__(self, num: float) -> None:
        for i in range(self._row):
            for j in range(self._col):
                self._array[i][j] = self._array[i][j]/num

    def __iter__(self) -> int:
        return self

    def __next__(self) -> float:
        if self._itera < self._row*self._col:
            row = self._itera//self._col
            col = self._itera % self._col
            self._itera += 1
            return self._array[row][col]
        else:
            raise StopIteration

    def isNS(self) -> bool:
        if self.det == 0.0:
            return False
        else:
            return True

    def size(self) -> tuple:
        return self.__len__()

    def tran(self) -> None:
        for i in range(self._row):
            for j in range(self._col):
                if i > j:
                    self._array[j][i], self._array[i][j] = \
                        self._array[i][j], self._array[j][i]

    def max(self, flag: int = 0) -> float:
        max = 0
        for i in range(self._row):
            for j in range(self._col):
                if max < abs(self._array[i][j]):
                    max = abs(self._array[i][j])
                    indexI = i
                    indexJ = j

        if flag == 0:
            return self._array[indexI][indexJ]
        else:
            return max

    def det(self) -> float:
        resultDet = 1
        if self._row == self._col:
            self._copyArray = self.copyArray()
            n = 0
            for k in range(self._row):
                n += self._changeOrder(k)
                for i in range(k, self._row-1):
                    ratio = self._copyArray[i+1][k]/self._copyArray[k][k]
                    for j in range(k, self._row):
                        self._copyArray[i+1][j] = self._copyArray[i+1][j] - \
                            ratio * self._copyArray[k][j]
                resultDet *= self._copyArray[k][k]
            return resultDet*(-1)**n
        else:
            return 0.0

    def inverse(self) -> Matrix:
        self._copyArray = self._augMat()
        for k in range(self._row):
            self._changeOrder(k)
            for i in range(k, self._row-1):
                ratio = self._copyArray[i+1][k]/self._copyArray[k][k]
                for j in range(k, self._row*2):
                    self._copyArray[i+1][j] = self._copyArray[i+1][j] - \
                        ratio * self._copyArray[k][j]
        for m in range(self._row):
            akk = self._copyArray[m][m]
            for n in range(m, self._col*2):
                self._copyArray[m][n] = self._copyArray[m][n]/akk
        for p in range(self._row-2, -1, -1):
            for q in range(p, -1, -1):
                ratio = self._copyArray[q][p+1]
                for o in range(p+1, self._col*2):
                    self._copyArray[q][o] = self._copyArray[q][o] - \
                        ratio*self._copyArray[p+1][o]
        result = Matrix(self._row, self._col)
        for i in range(self._row):
            for j in range(self._col):
                result[i, j] = self._copyArray[i][self._col+j]
        return result

    def copyArray(self) -> list:
        result = [[0]*self._row for _ in range(self._row)]
        for i in range(self._row):
            for j in range(self._col):
                result[i][j] = self._array[i][j]
        return result

    def _augMat(self) -> list:
        result = [[0]*self._row*2 for _ in range(self._row)]
        for i in range(self._row):
            for j in range(self._col*2):
                if i < self._row and j < self._col:
                    result[i][j] = self._array[i][j]
                elif j == self._col + i:
                    result[i][j] = 1
        return result

    def _changeOrder(self, column: int) -> int:
        colList = [0 for _ in range(self._row)]
        for i in range(column, self._row):
            colList[i] = abs(self._copyArray[i][column])
        maxColumn = colList.index(max(colList))
        if maxColumn == column:
            return 0
        else:
            self._copyArray[column], self._copyArray[maxColumn] = \
                self._copyArray[maxColumn], self._copyArray[column]
            return 1
