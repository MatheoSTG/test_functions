def list_test(n, table):
    # stworzenie listy z wszystkimi wartosciami w zakresie od 1 do n
    perfect_table = range(1, n+1)
    # zwrocenie roznicy dwoch setow, czyli zostana wartosci ktorych brakuje w perfect_table
    return list(set(perfect_table)-set(table))
