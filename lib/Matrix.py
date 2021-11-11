# -*- coding: utf-8 -*-


class Matrix(object):
    def __init__(self, row: int, col: int = 1):
        self._row = row
        self._col = col
        self._itera = 0
        self._array: list = [[0]*col for _ in range(row)]

    def __setitem__(self, key, value: float):
        try:
            self._array[key[0]][key[1]] = value
        except IndexError:
            print("IndexError: Matrix assignment index out of range")

    def __getitem__(self, key) -> float:
        try:
            return self._array[key[0]][key[1]]
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

    def size(self) -> tuple:
        return self.__len__()

    def tran(self) -> None:
        for i in range(self._row):
            for j in range(self._col):
                if i > j:
                    self._array[j][i], self._array[i][j] = \
                        self._array[i][j], self._array[j][i]

    def Max(self, flag: int = 0) -> float:
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
