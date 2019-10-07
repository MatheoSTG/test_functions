def gen_code(c1, c2):
    """Program generuje kody pocztowe, które znajdują sie pomiędzy kodami podanymi w parametrach c1 i c2.
    Parametry c1 i c2 powinny być przekazane w formacie 'XX-XXX', gdzie X to kolejne cyfry kodu pocztowego."""
    beg1 = int(c1[0:2])
    end1 = int(c1[3::])

    beg2 = int(c2[0:2])
    end2 = int(c2[3::])

    # Sprawdzenie czy kody zostały podane w odpowiedniej kolejności
    if beg1 > beg2:
        beg1, beg2 = beg2, beg1
        end1, end2 = end2, end1
    elif beg1 == beg2:
        if end1 > end2:
            end1, end2 = end2, end1

    code1 = 1000 * beg1 + end1
    code2 = 1000 * beg2 + end2

    list_code = []
    # stworzenie brakujacych kodow pocztowych
    for x in range(code1+1, code2):
        buff1 = str(x//1000)
        buff2 = x % 1000
        if buff2 < 10:
            buff2 = "00" + str(buff2)
        elif buff2 < 100:
            buff2 = "0" + str(buff2)
        else:
            buff2 = str(buff2)
        buff = buff1 + "-" + buff2
        list_code.append(buff)

    return list_code
