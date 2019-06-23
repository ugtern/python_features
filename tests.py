from first_file import DateEquals
import numpy as np


def test_first_file():
    test = DateEquals()
    a = np.array([])

    while len(a) < 1000:
        a = np.append(a, test.date_eq())

    a = a.sum()/len(a)
    print(a)


test_first_file()
