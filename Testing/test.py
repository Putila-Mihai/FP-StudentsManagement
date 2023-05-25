import unittest
from domain.Student import student
from domain.problema import problema


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.stud1 = student(1, 'Mihai', 100)
        self.stud2 = student(2, 'Alex', 101)

    def test_id(self):
        self.assertEqual(self.stud1.getid(),1)
        self.assertEqual(self.stud2.getid(),2)
        self.stud1.setid(2)
        self.stud2.setid(3)
        self.assertEqual(self.stud1.getid(), 2)
        self.assertEqual(self.stud2.getid(), 3)

    def test_nume(self):
        self.assertEqual(self.stud1.getnume(), 'Mihai')
        self.assertEqual(self.stud2.getnume(), 'Alex')
        self.stud1.setnume('Alex')
        self.stud2.setnume('Adda')
        self.assertEqual(self.stud1.getnume(), 'Alex')
        self.assertEqual(self.stud2.getnume(), 'Adda')

    def test_grupa(self):
        self.assertEqual(self.stud1.getgrup(), 100)
        self.assertEqual(self.stud2.getgrup(), 101)
        self.stud1.setgrup(103)
        self.stud2.setgrup(104)
        self.assertEqual(self.stud1.getgrup(), 103)
        self.assertEqual(self.stud2.getgrup(), 104)

class TestProblema(unittest.TestCase):

    def setUp(self):
        self.prob1 = problema(1, 'Suma numerelor 2 numere prime > 2.5','2022-12-12')
        self.prob2 = problema(2, 'demonstrati ca R este subpatiul lui C', '2012-12-12')

    def test_nr(self):
        self.assertEqual(self.prob1.getnr(),1)
        self.assertEqual(self.prob2.getnr(),2)

    def test_descriere(self):
        self.assertEqual(self.prob1.getdescriere(), 'Suma numerelor 2 numere prime > 2.5')
        self.assertEqual(self.prob2.getdescriere(), 'demonstrati ca R este subpatiul lui C')

    def test_deadline(self):
        self.assertEqual(self.prob1.getdeadline(), '2022-12-12')
        self.assertEqual(self.prob2.getdeadline(), '2012-12-12')
