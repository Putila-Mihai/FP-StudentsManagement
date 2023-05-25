from validator.stud_valid import StudValid
from domain.Student import student
from Repo.repositoryS import StudRepo
from Algorithm.Sort import BubbleSort


class studservice:
    """

    """

    def __init__(self, repos, StudValid):
        """
        creaza service-ul responsabil pentru gestionarea studentilor
        :param repos: multimea de studenti
        :param StudValid:  validator studenti
        """
        self.__repo = repos
        self.__validator = StudValid

    def get_all(self):
        """
        :return:  toti studentii
        """
        l =  self.__repo.get_all_stud()
        return BubbleSort(l,lambda X: X.getnume())

    def srv_add_stud(self, id, nume, grupa):
        """
        adauga un student in multime
        :param id: id student
        :param nume: nume student
        :param grupa: grupa student
        :return:
        """
        S = student(id, nume, grupa)
        self.__validator.validate(S)
        self.__repo.store(S)

    def srv_delete(self, id):
        """
        sterge un student din multimea de studenti
        :param id: id-ul studentului ce va fi cautat si sters
        """

        delete = self.__repo.search_by_id(id)
        if delete == -1:
            raise ValueError("\nnu exista un student cu acest id\n")
        else:
            self.__repo.remov(delete)

    def srv_modify(self, id, nume, grupa):
        """
        mdofica un student dupa id
        :param id: id
        :param nume: numele nou
        :oaram grupa: grupa noua
        """
        obiect = self.__repo.search_by_id(id)
        if obiect == -1:
            raise ValueError("\nNu exista un student cu acest id\n")
        else:
            obiect_nou = student(id, nume, grupa)
            self.__repo.modify(obiect, obiect_nou)

    def srv_search(self,id):
        """
        cauta un student dupa id in repo
        :param id: id-ul studentului cautat
        :return: studentul cautat
        """
        obiect = self.__repo.search_recursiv(id,0)
        if obiect == -1:
            raise ValueError("\nNu exista un student cu acest id\n")
        else:
            return obiect


def test_add_stud():
    repo = StudRepo()
    validator = StudValid()
    test_srv = studservice(repo, validator)
    test_srv.srv_add_stud(12, 'mihai', 250)

    assert (len(test_srv.get_all()) == 1)
    try:
        test_srv.srv_add_stud(2, 'asd', 12)
        assert False
    except ValueError:
        assert True


test_add_stud()
