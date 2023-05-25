class problema:
    no_instances = 0

    def __init__(self, nr, descriere, deadline):
        """
        creaza o noua problema cu un număr laborator_număr problemă ,descriere si deadline
        :param nr: număr laborator_număr problemă
        :param descriere: descrierea problemei
        :param deadline:deadline
        """
        self.__nr = nr
        self.__descriere = descriere
        self.__deadline = deadline  # yyyy-mm-dd

    def getnr(self):
        return self.__nr

    def getdescriere(self):
        return self.__descriere

    def getdeadline(self):
        return self.__deadline

    def setnr(self, value):
        self.__nr = value

    def setdescriere(self, value):
        self.__descriere = value

    def setdeadline(self, value):
        self.__deadline = value

    def __str__(self):
        return "\nNumarul :" + str(self.__nr) + "; Descrierea :" + self.__descriere + "; deadline: " + str(
            self.__deadline) + '\n'

    def __repr__(self):
        return str(self)

    @staticmethod
    def getNoInstances():
        return problema.no_instances


def test_problema():
    problema1 = problema('1_23', 'suma numerelor prime mai mici decat 60', '12/08/2023 12:00:00')
    assert (problema1.getnr() == '1_23')
    assert (problema1.getdescriere() == 'suma numerelor prime mai mici decat 60')
    assert (problema1.getdeadline() == '12/08/2023 12:00:00')
    problema1.setnr('2_23')
    problema1.setdescriere('suma numerelor prime mai mici decat 50')
    problema1.setdeadline('12/09/2023 12:00:00')
    assert (problema1.getnr() == '2_23')
    assert (problema1.getdescriere() == 'suma numerelor prime mai mici decat 50')
    assert (problema1.getdeadline() == '12/09/2023 12:00:00')


test_problema()
