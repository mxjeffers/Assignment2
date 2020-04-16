# Malcolm Jeffers
# CS261 Assignment 2
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
        """Returns the list"""
        return self._list[:self._size]

    def get_capacity(self):
        """Returns Capacity"""
        return self._capacity

    def _more_capacity(self):
        """Adds double the capacity"""
        # Doubles the capacity. Then creates a new list, copies the list
        # and replaces it.
        self._capacity *= 2
        new_list = np.empty([self._capacity], np.int16)
        for i in range(0, self._size):
            new_list[i] = self._list[i]
        self._list = new_list

    def append(self, val):
        """Adds a value to the list"""
        # Determines if the list is full. If it is add more capacity
        if self._size != 0:
            if self._capacity / self._size == 1:
                self._more_capacity()

        # Add the value to the end of the list
        self._list[self._size] = val
        self._size += 1

    def pop(self):
        """Pops and returns the value at the end of the list"""
        if self._size > 0:
            self._size -= 1
            popped = self._list[self._size]
            return popped

    def insert(self, index, val):
        """Puts a value at the requested index."""
        # Checks capacity if full adds more
        if self._size != 0:
            if self._capacity / self._size == 1:
                self._more_capacity()
        # If the index is larger than the current size append it to the end.
        if index >= self._size:
            self.append(val)
        # Inserts the value at the index and move other values over one space.
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
        """Removes the first instance of a value"""
        # Searches for a requested value. If found moves all values to
        # the left and decreases the list size.
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
        """Initializes the list to the beginning settings."""
        self.__init__()

    def count(self, val):
        """Counts the amount of times a value is in the list and returns it."""
        count = 0
        if self._size > 0:
            for i in range(0, self._size):
                if val == self._list[i]:
                    count += 1
                    i += 1
        return count

    def get(self, index):
        """Returns the value at a location."""
        if index <= self._size:
            return self._list[index]


if __name__ == '__main__':
    Student = StudentList()
    Student.pop()
    Student.append(15)
    Student.pop()
    Student.append(19)
    Student.append(25)
    Student.pop()
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
