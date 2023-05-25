from domain.Student import student


class StudValid:
    def validate(self, student):
        """
        verifica daca un student este creat corect
        :param student: obiect de tip student
        """
        errors = []
        if student.getid() < 0:
            errors.append("id-ul trebuie sa fie un numar natural")
        if len(student.getnume()) < 3:
            errors.append("numele trebuie sa aiba minim")
        if student.getgrup() < 99 or student.getgrup() > 999:
            errors.append("Grupul trebuie sa fie un numar intre 100 si 1000")

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)


def test_StudValid():
    test = StudValid()
    stud1 = student(10, 'Mihai', 215)
    test.validate(stud1)

    stud2 = student(-12, 'mihai', 140)

    try:
        test.validate(stud2)
        assert False
    except ValueError:
        assert True

    stud3 = student(12, 'mihai', 40)

    try:
        test.validate(stud3)
        assert False
    except ValueError:
        assert True


test_StudValid()
