import pickle
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
list_of_lists = pickle.load(open("List_of_lists.p", "rb"))
print(list_of_lists)
R = 3
counter = 1  # counter - wyliacza ciagi
average_missing = 0
for lists in list_of_lists:  # lists - n-ty ciąg zawierajacy 100 losowo wybranych numerow stron
    needed = 0
    missing = 0  # missing - brakujacych stron w danym ciagu
    frame = []  # tablica ramki danego ciagu
    used = {}
    for c in range(20):
        used[c+1] = 0 # tablica użyć stron
    for i in range(len(lists)):
        is_missing = True
        if i == 0:
            frame.append(lists[i])
            missing += 1
            used[lists[i]] += 1
            #print("dodalem 1 do strony numer", lists[i])
        else:
            if len(frame) < R:
                for a in range(len(frame)):
                    if lists[i] == frame[a]:
                        is_missing = False
                        used[lists[i]] += 1
                        #print("dodalem 1 do strony numer", lists[i])
                        break
                if is_missing:
                    needed = lists[i]
                    missing += 1
                    used[needed] += 1
                    #print("dodalem 1 do strony numer", needed)
                    frame.append(needed)
            else:
                for a in range(len(frame)):
                    if lists[i] == frame[a]:
                        is_missing = False
                        used[lists[i]] += 1
                        #print("dodalem 1 do strony numer", lists[i])
                        break
                if is_missing:
                    missing += 1
                    most = frame[0]
                    index = 0
                    for b in range(1, len(frame)):
                        if frame[b] >= most:
                            most = frame[b]
                            index = b
                        else:
                            continue
                    frame.insert(index, most)
                    used[most] += 1
                    #print("dodalem 1 do strony numer", most)
                    needed = lists[i]
                    frame.append(needed)
    average_missing += missing
    print("Brakujacych stron w ciagu nr", counter, "=>", missing)
    x.append(counter)
    y.append((missing))
    counter += 1



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

