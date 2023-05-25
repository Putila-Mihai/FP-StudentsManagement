def BubbleSort(lista,cheie):
    """
    sorteaza crestacator lista
    :param lista: lista
    :return:lista ordonata
    """
    for i in range(len(lista)):
        ok = False
        for j in range(0, len(lista) - i - 1):
            if cheie(lista[i]) > cheie(lista[i + 1]):
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
                ok =True
        if not ok:
            break
    return lista

def ShellSort(lista,cheie):
    """
    sorteaza crescator lista
    :param lista: lista
    :param cheie: cheia
    :return: lista ordonata
    """
    interval = len(lista) // 2
    while interval > 0 :
        for i in range(interval,len(lista)):
            temp = lista[i]
            j = i
            while j >= interval and cheie(lista[j-interval]) > cheie(temp):
                lista[j]= lista [j-interval]
                j-= interval

            lista[j] = temp

        interval =interval // 2
    return lista





