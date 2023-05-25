from domain.Student import student
class RepofromFile():

    def __init__(self,filename):
        self.__filename = filename
    def __load_from_file(self):
        try:
            f = open(self.__filename, "r")
        except IOError:
            return
        lines = f.readlines()
        all_stud = []
        for line in lines:
            id, nume, grupa = [token.strip() for token in line.split(';')]
            id = int(id)
            grupa = int(grupa)
            s = student(id, nume, grupa)
            all_stud.append(s)
        f.close()
        return all_stud

    def __save_in_file(self, all_stud):
        """
        salveaza noua lista de carti in fisierul cu carti
        :param carte: oiect d etip carte
        """
        with open(self.__filename, 'w') as f:
            for stud in all_stud:
                stud_string = str(stud.getid()) + ';' + str(stud.getnume()) + ';' + str(stud.getgrupa()) + '\n'
                f.write(stud_string)

    def store(self, stud):
        """
        adauga o carte la muktimea de carti
        :param carte: obiect de tip carte
        """
        all_stud = self.__load_from_file()
        all_stud.append(stud)
        self.__save_in_file(all_stud)

    def search_stud(self, id):
        """
        cauta o carte in fisier
        :param id: id-ul cartii
        :return: cartea sau  1 daca aceasta nu ecxista
        """
        all_stud = self.__load_from_file()
        for stud in all_stud:
            if stud.getid() == id:
                return stud
        return -1;

    def get_all(self):
        return self.__load_from_file()