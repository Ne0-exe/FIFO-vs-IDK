# MODUŁ ZAWIERAJĄCY PROCES TWORZENIA I SERIALIZACJI DANYCH WEJŚCIOWYCH

import pickle
import random

list_of_lists = []
counter = 0
while counter < 100:
    var = []
    for i in range(100):
        var.append(random.randint(1,20))
    lst = []
    for i in range(100):
        lst.append(var[i])
    list_of_lists.append(lst)
    counter += 1
pickle.dump(list_of_lists, open("List_of_lists.p", "wb"))