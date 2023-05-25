from domain.Student import student
class serv:
    """
    obiect de tip service
    """
    def __init__(self,repo,vali):
        self.__repo = repo
        self.__validator = vali

    def srv_add_stud(self,id,nume,grupa):
        c = student(id,nume,grupa)
        self.__repo.store(c)

    def srv_show_all(self):
        return self.__repo.get_all()

    def srv_search(self,id):
        """
        cauta un student dupa id in  multimea de studenti
        :param id: id studnet
        :return: studentul daca aceasta exista
        """
        obiect = self.__repo.search_stud(id)
        if obiect == -1 :
            raise ValueError('Studentul nu exista')
        else:
            return obiect