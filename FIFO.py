import pickle
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

list_of_lists = pickle.load(open("List_of_lists.p", "rb"))
R = 3
counter = 1 # counter - wyliacza ciagi
average_missing = 0
for lists in list_of_lists: #lists - n-ty ciąg zawierajacy 100 losowo wybranych numerow stron
    needed = 0
    missing = 0 # missing - brakujacych stron w danym ciagu
    frame = []  # tablica ramki danego ciagu
    for i in range(len(lists)):
        is_missing = True
        if i == 0:
            frame.append(lists[i])
            missing += 1
        else:
            if len(frame) < R:
                for a in range(len(frame)):
                    if lists[i] == frame[a]:
                        is_missing = False
                        break
                if is_missing:
                    needed = lists[i]
                    missing += 1
                    frame.append(needed)
            else:
                for a in range(len(frame)):
                    if lists[i] == frame[a]:
                        is_missing = False
                        break
                if is_missing:
                    missing += 1
                    del frame[0]
                    needed = lists[i]
                    frame.append(needed)
    average_missing += missing
    print("Brakujacych stron w ciagu nr", counter, "=>", missing)
    counter += 1
    x.append(counter)
    y.append((missing))

print("Srednio brakujacych stron: ", average_missing/100)

# TWORZENIE GRAFU
y_mean = [np.mean(y)]*len(x)
fig, ax = plt.subplots()
mean_line = ax.plot(x, y_mean, label='Mean', linestyle='--')
plt.plot(x, y)
plt.xlabel("Nr ciągu")
plt.ylabel("Brakujących stron")
plt.title("FIFO - średnio brakujących stron w 100 ciągach")
plt.show()
print("Srednio brakujacych stron: ", average_missing/100)

# ----------------------------------------



