class TemaRepo():
    def __init__(self):
        self.__teme = []

    def store(self,tema):
        self.__teme.append(tema)

    def get_all(self):
        return self.__teme

    def find(self,t):
        for teme in self.__teme:
            if t == teme:
                return teme
        return none

    def all_grades(self,student):
        """
        cauta toate temele unui student
        :param student: student
        :return: lista de teme
        """
        lista = []
        for tema in self.get_all():
            if tema.getid() == student.getid():
                lista.append(tema)
        return lista

