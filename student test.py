import unittest
from student_list import StudentList


class TestList(unittest.TestCase):

    def Test_1(self):
        Student = StudentList()
        Student.append("Malcolm")
