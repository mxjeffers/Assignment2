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

    def append(self, val):

        def larger(current_list, capacity, size):
            new_list = np.empty([capacity * 2],np.int16)
            for i in range(0,size):
                new_list[i] = current_list[i]
            current_list = new_list

        if self._size !=0:
            if self._capacity / self._size == 1:
                larger(self._list,self._capacity,self._size)
                self._capacity *=2
            self._list[self._size] = val
            self._size +=1

    def pop(self):
        # FIXME: You will write this function

    def insert(self, index, val):
        # FIXME: You will write this function

    def remove(self, val):
        # FIXME: You will write this function

    def clear(self):
        # FIXME: You will write this function

    def count(self):
        # FIXME: You will write this function

    def get(self, index):
        # FIXME: You will write this function
