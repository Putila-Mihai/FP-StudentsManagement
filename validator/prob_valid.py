from datetime import *

from domain.problema import problema


class ProbValid:
    def validate(self, problema):
        errors = []
        if problema.getnr() < 0:
            errors.append("numarul problemei trebuie sa fie un numar natural")
        if len(problema.getdescriere()) < 10:
            errors.append("descrierea trebuie sa aiba minim 10 caractere")
        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)


def test_ProbValid():
    test = ProbValid()
    prob1 = problema(2, 'Suma a doua numere prime e un numar prim', '2022-12-12')
    test.validate(prob1)
    prob3 = problema(-2, 'fsfzfsdfdsfgs', '2022-12-12')
    try:
        test.validate(prob3)
        assert False
    except ValueError:
        assert True
    prob2 = problema(2, 'fdsfgs', '2022-12-12')
    try:
        test.validate(prob2)
        assert False
    except ValueError:
        assert True


test_ProbValid()
