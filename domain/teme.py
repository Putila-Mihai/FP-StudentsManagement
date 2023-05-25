class tema:
    def __init__(self,id,nr,nota):
        '''
        initializeaza  obicetul de tip tema
        '''
        self.__id = id
        self.__nr = nr
        self.__nota = nota

    def getid(self):
        return self.__id

    def getnr(self):
        return self.__nr

    def getnota(self):
        return self.__nota

    def setid(self,value):
        self.__id = value

    def setnr(self,value):
        self.__nr = value

    def setnota(self,value):
        self.__nota = value

    def __str__(self):
        return 'Student:' + str(self.__id) + 'problema:' + str(self.__nr) + 'Nota :' + str(self.__nota)

    def __repr__(self):
        return str(self)