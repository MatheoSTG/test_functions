from numpy import arange
from decimal import *


def gen_dec():
    # stworzenie ciągu od 2.0 do 5.5
    table = arange(2.0, 5.5, 0.5)
    # zamiana danych do formatu Decimal, dla takich wartości nie straci dokładności
    data = map(Decimal, table)
    return data

