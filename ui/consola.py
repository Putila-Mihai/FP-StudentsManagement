
from datetime import *



class console:
    """
    initializeaza consola
    """

    def __init__(self, services, servicep, servteme):
        self.__servstud = services
        self.__servprob = servicep
        self.__servteme = servteme

    def __add_student(self):
        """
        adauga un student in repo
        """
        nume = input('Numele studentului este:')
        try:
            id = int(input('Id ul studentului este:'))
            grupa = int(input('Grupa studentului este:'))
        except ValueError:
            print('id-ul si grupa studentului  trebuie sa fie numere naturale')
            return 0
        try:
            self.__servstud.srv_add_stud(id, nume, grupa)
            print('\nAdaugat cu succes\n')
        except ValueError as ve:
            print(ve)

    def __show_all_studs(self):
        '''
        afiseaza lista de  studenti
        '''
        print(self.__servstud.get_all())

    def __delete(self):
        """
        sterge un student din lista
        """
        try:
            id = int(input('\nId-ul studentului pe care doriti sa-l stergeti'))
        except ValueError:
            print("id-ul trebuie sa fie un numar natural\n")
        try:
            self.__servstud.srv_delete(id)
            print('\nSters cu succes\n')
        except ValueError as ve:
            print(ve)

    def __modify(self):
        """
        modifica un student
        """
        try:
            id = int(input('\nId-ul studentului pe care doriti sa-l modificati'))
            grupa = int(input('\n grupa este:'))
        except ValueError:
            print("id-ul si grupa trebuie sa fie numere naturale\n")
        numele = input('Numele este:')
        try:
            self.__servstud.srv_modify(id, numele, grupa)
            print('\nSters cu succes\n')
        except ValueError as ve:
            print(ve)

    def __add_prob(self):
        """
        adauga o problema la multimea de probleme
        """
        try:
            nr = int(input("numarul problemei: "))
        except:
            ValueError('\nnumarul trebuie sa fie un numaru natural\n')
        descriere = input('Descrierea Problemei: ')
        try:
            deadline = datetime.strptime(input('Deadline-ul problemei este(yyyy-mm-dd):'), '%Y-%m-%d')
        except ValueError:
            print('Data trebuie sa fie de tipul %Y-%m-%d')
        try:
            self.__servprob.srv_add_prob(nr, descriere, deadline)
            print('\nAdaugat cu succes\n')
        except ValueError as ve:
            print(ve)

    def __delete_prob(self):
        """
        sterge o problema dupa numar
        """
        try:
            nr = int(input("numarul problemei: "))
        except:
            ValueError('\nnumarul trebuie sa fie un numaru natural\n')
        try:
            self.__servprob.srv_del(nr)
            print('\nSters cu succes\n')
        except ValueError as ve:
            print(ve)

    def __show_all_prob(self):
        """
        tipareste lista cu toate problemele
        :return:
        """
        print(self.__servprob.get_all())

    def __modify_prob(self):
        """
        modifica deadline-ul unei probleme
        """
        try:
            nr = int(input("numarul problemei: "))
        except:
            ValueError('\nnumarul trebuie sa fie un numaru natural\n')
        try:
            deadline = datetime.strptime(input('Deadline-ul problemei este(yyyy-mm-dd):'), '%Y-%m-%d')
        except ValueError:
            print('Data trebuie sa fie de tipul %Y-%m-%d')
        try:
            self.__servprob.srv_modify(nr, deadline)
            print('\nModifdicat cu succes\n')
        except ValueError as ve:
            print(ve)

    def __search_s(self):
        '''
        cauta student dupa id
        '''
        try:
            id = int(input('\nId-ul studentului pe care doriti sa-l cautati'))
        except ValueError:
            print("id-ul trebuie sa fie un numar natural\n")
        try:
            print(self.__servstud.srv_search(id))
        except ValueError:
            print('Studentul cu acest id nu exista')

    def __search_p(self):
        '''
        cauta student dupa id
        '''
        try:
            nr = int(input("numarul problemei: "))
        except:
            ValueError('\nnumarul trebuie sa fie un numaru natural\n')
        try:
            print(self.__servprob.srv_search(nr))
        except ValueError:
            print('Problema cu acest numar nu exista')

    def __show_grades(self):
        """
        afiseaza toate notele si studenti
        :return:
        """
        print(self.__servteme.get_all())

    def __asignare(self):
        """
        asigneaza probleme de laborator studentilor
        :return:
        """
        try:
            id = int(input("id-ul studentului este:"))
            nr = int(input('Numarul problemei este:'))
            nota = int(input('Nota pe care a obtinut-o studentul'))
            if nota > 10 or nota < 1:
                x = int('s')
        except ValueError:
            print('id,nr trebuie sa fie numere naturale,iar nota un numar intre 1 si 10')
            return 0
        x = 0
        try:
            x = self.__servstud.srv_search(id)
            x = self.__servprob.srv_search(nr)
            x = 1
        except ValueError as ve:
            print(ve)
        if x == 1:
            self.__servteme.create_tema(id, nr, nota)
            print('\nadaugat cu succes')
        else:
            print("incercati din nou ... nereusit")

    def __note(self):
        """
        lista de studenți și notele lor la o problema de laborator dat, ordonat
        """
        problema = int(input("Id-ul problemei este:"))
        for i in self.__servteme.raport(problema):
            print('\n',i)

    def __afiseazafile(self):
        """
        afiseaza studneti dintr -un fisier text
        :return:
        """
        print(self.__servstud.srv_show_all())

    def __promovati(self):
        """
        afiseaza studenti care au media notelor sub 5
        :return:
        """
        for i in self.__servteme.nepromovati():
            print(i)


    def ui(self):
        while True:
            print(
                '\nComenzi disponibile: gestionare_studenti ,gestionare_probleme,cautare,asignare_lab,statistici, undo, exit\n')
            cmd = input('comanda este:')
            cmd = cmd.lower().strip()
            if cmd == 'gestionare_studenti':
                print('Comenzi disponibile: adauga,modifica,sterge,afiseaza\n')
                cmd2 = input('Comanda este:  ')
                if cmd2 == 'adauga':
                    self.__add_student()
                elif cmd2 == 'afiseaza':
                    self.__show_all_studs()
                elif cmd2 == 'sterge':
                    self.__delete()
                elif cmd2 == 'modifica':
                    self.__modify()
                # if cmd2 == 'afiseaza':
                #     self.__afiseazafile()
            elif cmd == 'gestionare_probleme':
                print('Comenzi disponibile: adauga,modifica,sterge,afiseaza\n')
                cmd2 = input('Comanda este:  ')
                if cmd2 == 'adauga':
                    self.__add_prob()
                elif cmd2 == 'afiseaza':
                    self.__show_all_prob()
                elif cmd2 == 'sterge':
                    self.__delete_prob()
                elif cmd2 == 'modifica':
                    self.__modify_prob()
            elif cmd == 'cautare':
                print('\nCautari disponibile: cautare_student(dupa id)/ cautare_problema(dupa numar)\n')
                cmd2 = input('comanda este:\n')
                if cmd2 == 'cautare_student':
                    self.__search_s()
                elif cmd2 == 'cautare_problema':
                    self.__search_p()
                else:
                    print('comanda introdusa este gresita')
            elif cmd == 'asignare_lab':
                print('\n asignare, afisare')
                cmd2 = input('comanda este\n')
                if cmd2 == 'asignare':
                    self.__asignare()
                elif cmd2 == 'afisare':
                    self.__show_grades()
                else:
                    print('\ncomanda inexistenta\n')
            elif cmd == 'statistici':
                print('\n [1]lista de studenți și notele lor la o problema de laborator dat, ordonat: alfabetic după nume,după notă,\n [2]Toți studenții cu media notelor de laborator mai mic decât 5\n')
                cmd2 = input('Comanda este([1],[2]):')
                if cmd2 == '1':
                    self.__note()
                elif cmd2 == '2':
                    self.__promovati()
                else:
                    print('\ncomanda inexistenta\n')
            elif cmd == 'exit':
                return
            else:
                print('\nComanda introdusa este INEXISTENTA\n')


