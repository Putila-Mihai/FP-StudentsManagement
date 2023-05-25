class ProbRepo:
    """
    clasa pentru gestionarea multimii de probleme
    """

    def __init__(self):
        self.__prob = []

    def store(self, problema):
        self.__prob.append(problema)

    def get_all_prob(self):
        return self.__prob

    def search_by_nr(self,nr):
        """
        cauta o problema dupa numar
        :param nr: numarul problemei
        :return:
        """
        for i in self.get_all_prob():
            if i.getnr() == nr:
                return i
        return -1

    def remov(self,delete):
        """
        sterge o problema din multime
        :param delete: problema ce va fi stearsa
        """
        self.__prob.remove(delete)

    def modify(self,obiect,obiect_nou):
        """
        modifica o problema
        :param obiect: problema  modificata
        :param obiect_nou: noua problema
        """
        index = self.__prob.index(obiect)
        self.__prob[index] = obiect_nou
