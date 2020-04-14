# student_list.py
# ===================================================
# Reimplementation of Pythons List
# ===================================================

import numpy as np


# StudentList class is our implementation of Python's List
class StudentList:
    def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0

    def __str__(self):
        return str(self._list[:self._size])

    # You may want an internal function that handles resizing the array.
    # Dont modify get_list or get_capacity, they are for testing

    def get_list(self):
        return self._list[:self._size]

    def get_capacity(self):
        return self._capacity

    def _more_capacity(self):
        self._capacity *= 2
        new_list = np.empty([self._capacity], np.int16)
        for i in range(0, self._size):
            new_list[i] = self._list[i]
        self._list = new_list

    def append(self, val):

        if self._size != 0:
            if self._capacity / self._size == 1:
                self._more_capacity()

        self._list[self._size] = val
        self._size += 1

    def pop(self):
        if self._size > 0:
            self._size -= 1


    def insert(self, index, val):
        if self._size != 0:
            if self._capacity / self._size == 1:
                self._more_capacity()
        # If the index is larger than the current size append it to the end.
        if index >= self._size:
            self.append(val)
        else:
            i = index
            temp = self._list[i]
            i += 1
            while i <= self._size:
                prev = temp
                temp = self._list[i]
                self._list[i] = prev
                i += 1
            self._list[index] = val
            self._size += 1

    def remove(self, val):
        if self._size > 0:
            for i in range(0, self._size):
                if val == self._list[i]:
                    while i < self._size - 1:
                        self._list[i] = self._list[i + 1]
                        i += 1
                    self._size -= 1
                    self._list = self._list[:self._size]
                    return

    def clear(self):
        self.__init__()

    def count(self, val):
        count = 0
        if self._size > 0:
            for i in range(0, self._size):
                if val == self._list[i]:
                    count += 1
                    i += 1
        return count

    def get(self, index):
        if index <= self._size:
            return self._list[index]


if __name__ == '__main__':
    Student = StudentList()
    Student.append(15)
    Student.append(19)
    Student.append(25)
    Student.append(89)
    Student.append(45)
    Student.append(99)
    Student.append(45)
    Student.insert(2, 55)
    Student.insert(0, 49)
    Student.insert(75, 101)
    Student.pop()
    Student.append(45)
    print(Student.get(3))
    Student.remove(25)
    print(Student.count(45))
    Student.clear()
    Student.append(69)
    print('OHYEAH')
