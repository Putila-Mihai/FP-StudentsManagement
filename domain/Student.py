class student:
    no_instances = 0

    def __init__(self, id, nume, grup):
        """
        creaza un nou student cu id, nume si grup
        :param id:id
        :param nume: numele studentului
        :param grup: grupul din care apartine studentul
        """
        self.__id = id
        self.__nume = nume
        self.__grup = grup
        student.no_instances += 1

    def getid(self):
        return self.__id

    def getnume(self):
        return self.__nume

    def getgrup(self):
        return self.__grup

    def setid(self, value):
        self.__id = value

    def setnume(self, value):
        self.__nume = value

    def setgrup(self, value):
        self.__grup = value

    def __str__(self):
        return "\nId :" + str(self.__id) + "; Numele :" + self.__nume + "; grupul: " + str(self.__grup) + '\n'

    def __repr__(self):
        return str(self)

    @staticmethod
    def getNoInstances():
        return student.no_instances


def test_student():
    student1 = student(12, 'mihai', 21)
    assert (student1.getid() == 12)
    assert (student1.getnume() == 'mihai')
    assert (student1.getgrup() == 21)
    student1.setid(1)
    student1.setnume('alex')
    student1.setgrup(2)
    assert (student1.getid() == 1)
    assert (student1.getnume() == 'alex')
    assert (student1.getgrup() == 2)


test_student()
