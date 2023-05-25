from validator.prob_valid import ProbValid
from domain.problema import problema
from Repo.repositoryP import ProbRepo
from Algorithm.Sort import ShellSort

class probservice():
    """

    """

    def __init__(self, repop, ProbValid):
        """
        initializeaza service-ul pentru probleme
        """
        self.__repo = repop
        self.__valid = ProbValid

    def get_all(self):
        """
        :return:  toti studentii
        """
        l = self.__repo.get_all_prob()
        return ShellSort(l,lambda X: X.getnr())

    def srv_add_prob(self, nr, descriere, deadline):
        """
        adauga o problema in multime
        :param nr: nr problemei
        :param descriere: descriere
        :param deadline:  deadline -ul problemei
        """
        P = problema(nr, descriere, deadline)
        self.__valid.validate(P)
        self.__repo.store(P)

    def srv_del(self,nr):
        """
        sterge o problema
        :param nr: numarul problemei
        """
        delete = self.__repo.search_by_nr(nr)
        if delete == -1:
            raise ValueError("\nnu exista un student cu acest id\n")
        else:
            self.__repo.remov(delete)
    def srv_modify(self,nr,deadline):
        """
        modifica deadline-ul unei probleme
        :param nr: numarul problemei
        :return:
        """
        obiect = self.__repo.search_by_nr(nr)
        if obiect == -1:
            raise ValueError("\nNu exista o problema cu acest nr\n")
        else:
            obiect_nou = problema(nr, obiect.getdescriere(), deadline)
            self.__repo.modify(obiect, obiect_nou)

    def srv_search(self,nr):
        """
        cauta o problema dupa un numar
        :param nr: numarul problemei
        :return: problema cautata
        """
        obiect = self.__repo.search_by_nr(nr)
        if obiect == -1:
            raise ValueError("\nNu exista o problema cu acest nr\n")
        else:
            return obiect


def test_add_stud():
    repo = ProbRepo()
    validator = ProbValid()
    test_srv = probservice(repo, validator)
    test_srv.srv_add_prob(12, 'suma primelor doua numere prime mai mici decat n', 250)

    assert (len(test_srv.get_all()) == 1)
    try:
        test_srv.srv_add_prob(2, 'asd', 12)
        assert False
    except ValueError:
        assert True


test_add_stud()
