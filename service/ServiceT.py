from domain.teme import tema
from operator import itemgetter

class TemeService():
    def __init__(self,repo,vali,repos,repop):
        self.__teme_repo = repo
        self.__teme_validator = vali
        self.__student_repo = repos
        self.__problem_repo = repop

    def create_tema(self,id,nr,nota):
        """
         creaza si adauga o tema in multime
        :param id: id-ul studentului
        :param nr: id-ul problemei
        :param nota: nota
        :return:
        """
        t = tema(id,nr,nota)
        self.__teme_repo.store(t)

    def raport(self,problema):
        """
        lista de studenți și notele lor la o problema de laborator dat, ordonat
        :param problema: problema data
        :return: lista de studenti si notele lor la aceasta problema
        """
        lista = []
        for tema in self.__teme_repo.get_all():
            if tema.getnr() == problema:
                lista.append([self.__student_repo.search_by_id(tema.getid()).getnume(),tema.getnota()])
        lista = sorted(lista, key = itemgetter(1))
        return lista


    def nepromovati(self):
        """
        :return: lista de studenti care au media notelor sub 5
        """
        all_stud = self.__student_repo.get_all_stud()
        stud_nepromovati = []
        for stud in all_stud:
            suma = 0
            probleme = self.__teme_repo.all_grades(stud)
            for problema in probleme :
                suma = suma + problema.getnota()
            if suma/len(probleme) < 5:
                stud_nepromovati.append([stud.getnume(),suma/len(probleme)])
        return stud_nepromovati

    def get_all(self):
        return self.__teme_repo.get_all()

