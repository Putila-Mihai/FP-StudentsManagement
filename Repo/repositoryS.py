class StudRepo:
    '''
    clasa pentru gestionarea multimii de studenti
    '''

    def __init__(self):
        self.__stud = []

    def store(self, student):
        """
        adauga un stundent in multime
        :param student: obiect d etip student
        """
        self.__stud.append(student)

    def get_all_stud(self):
        """
        :return:returneaza o lista cu toti studenti
        """
        return self.__stud
    def search_recursiv(self,id,i):
        """
        cauta student dupa id
        :param id: id cautat
        :param i: numarul de ordine student in repo
        :return: studentul cautat sau -1 daca nu exitsa
        """
        lista = self.get_all_stud()
        if i > len(lista):
            return -1
        if lista[i].getid() == id :
            return lista[i]
        return self.search_recursiv(id,i+1)


    def search_by_id(self, id):
        """
        sterge studnet din lista
        :param id: id-ul studentului
        :return:
        """
        for i in self.get_all_stud():
            if i.getid() == id:
                return i
        return -1

    def modify(self, obiect, obiect_nou):
        """
        modifica un stundet dupa id
        :param obiect:  studentul
        :param nume: numele nou
        :param grupa: grupa noua
        """
        index = self.__stud.index(obiect)
        self.__stud[index] = obiect_nou

    def remov(self, student):
        """
        sterge un elev din lsita de dictionare
        """
        self.__stud.remove(student)

# teste !!!!!!!!!!!!!!!!!!!!
