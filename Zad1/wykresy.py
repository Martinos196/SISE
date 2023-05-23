import matplotlib.pyplot as plt
import numpy as np

def average_species(data, attr, number, search, strategy):
    avg = 0
    dlen = 0
    for i in data:
        if i[0] == number:
            if i[2] == search:
                if i[3] == strategy:
                    if i[4] != -1:
                        avg += i[attr]
                        dlen += 1
    return round(avg/dlen, 2)

file= open("data.csv", "r")
fulldata = file.read()
file.close()
data = []
for line in fulldata.split('\n'):
    data_row = []
    if line == '':
        continue
    for row in line.split(' '):
        if row == 'astr' or row == 'hamm' or row == 'manh' or row == 'bfs' or row == 'dfs' or row == 'rdul' or row == 'rdlu' or row == 'drul' or row == 'drlu' or row == 'ludr' or row == 'lurd' or row == 'uldr' or row == 'ulrd':
            data_row.append(str(row))
        elif row != '':
            data_row.append(float(row))
    data.append(data_row)

bar_width = 0.1
#dfs 1
#"""
diagrams_rdul = np.array([average_species(data, 4, 1, 'dfs', 'rdul'), average_species(data, 4, 2, 'dfs', 'rdul'), average_species(data, 4, 3, 'dfs', 'rdul'), average_species(data, 4, 4, 'dfs', 'rdul'), average_species(data, 4, 5, 'dfs', 'rdul'), average_species(data, 4, 6, 'dfs', 'rdul'), average_species(data, 4, 7, 'dfs', 'rdul')])
diagrams_rdlu = np.array([average_species(data, 4, 1, 'dfs', 'rdlu'), average_species(data, 4, 2, 'dfs', 'rdlu'), average_species(data, 4, 3, 'dfs', 'rdlu'), average_species(data, 4, 4, 'dfs', 'rdlu'), average_species(data, 4, 5, 'dfs', 'rdlu'), average_species(data, 4, 6, 'dfs', 'rdlu'), average_species(data, 4, 7, 'dfs', 'rdlu')])
diagrams_drul = np.array([average_species(data, 4, 1, 'dfs', 'drul'), average_species(data, 4, 2, 'dfs', 'drul'), average_species(data, 4, 3, 'dfs', 'drul'), average_species(data, 4, 4, 'dfs', 'drul'), average_species(data, 4, 5, 'dfs', 'drul'), average_species(data, 4, 6, 'dfs', 'drul'), average_species(data, 4, 7, 'dfs', 'drul')])
diagrams_drlu = np.array([average_species(data, 4, 1, 'dfs', 'drlu'), average_species(data, 4, 2, 'dfs', 'drlu'), average_species(data, 4, 3, 'dfs', 'drlu'), average_species(data, 4, 4, 'dfs', 'drlu'), average_species(data, 4, 5, 'dfs', 'drlu'), average_species(data, 4, 6, 'dfs', 'drlu'), average_species(data, 4, 7, 'dfs', 'drlu')])
diagrams_ludr = np.array([average_species(data, 4, 1, 'dfs', 'ludr'), average_species(data, 4, 2, 'dfs', 'ludr'), average_species(data, 4, 3, 'dfs', 'ludr'), average_species(data, 4, 4, 'dfs', 'ludr'), average_species(data, 4, 5, 'dfs', 'ludr'), average_species(data, 4, 6, 'dfs', 'ludr'), average_species(data, 4, 7, 'dfs', 'ludr')])
diagrams_lurd = np.array([average_species(data, 4, 1, 'dfs', 'lurd'), average_species(data, 4, 2, 'dfs', 'lurd'), average_species(data, 4, 3, 'dfs', 'lurd'), average_species(data, 4, 4, 'dfs', 'lurd'), average_species(data, 4, 5, 'dfs', 'lurd'), average_species(data, 4, 6, 'dfs', 'lurd'), average_species(data, 4, 7, 'dfs', 'lurd')])
diagrams_uldr = np.array([average_species(data, 4, 1, 'dfs', 'uldr'), average_species(data, 4, 2, 'dfs', 'uldr'), average_species(data, 4, 3, 'dfs', 'uldr'), average_species(data, 4, 4, 'dfs', 'uldr'), average_species(data, 4, 5, 'dfs', 'uldr'), average_species(data, 4, 6, 'dfs', 'uldr'), average_species(data, 4, 7, 'dfs', 'uldr')])
diagrams_ulrd = np.array([average_species(data, 4, 1, 'dfs', 'ulrd'), average_species(data, 4, 2, 'dfs', 'ulrd'), average_species(data, 4, 3, 'dfs', 'ulrd'), average_species(data, 4, 4, 'dfs', 'ulrd'), average_species(data, 4, 5, 'dfs', 'ulrd'), average_species(data, 4, 6, 'dfs', 'ulrd'), average_species(data, 4, 7, 'dfs', 'ulrd')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_rdul))
br2 = [x + bar_width for x in br1]
br3 = [x + bar_width for x in br2]
br4 = [x + bar_width for x in br3]
br5 = [x + bar_width for x in br4]
br6 = [x + bar_width for x in br5]
br7 = [x + bar_width for x in br6]
br8 = [x + bar_width for x in br7]
plt.bar(br1, diagrams_rdul, color = 'blue', width=bar_width, label='rdul')
plt.bar(br2, diagrams_rdlu, color = 'orange', width=bar_width, label='rdlu')
plt.bar(br3, diagrams_drul, color = 'green', width=bar_width, label='drul')
plt.bar(br4, diagrams_drlu, color = 'red', width=bar_width, label='drlu')
plt.bar(br5, diagrams_ludr, color = 'purple', width=bar_width, label='ludr')
plt.bar(br6 , diagrams_lurd, color = 'k', width=bar_width, label='lurd')
plt.bar(br7, diagrams_uldr, color = 'gray', width=bar_width, label='uldr')
plt.bar(br8, diagrams_ulrd, color = 'cornflowerblue', width=bar_width, label='ulrd')
plt.xticks([r + 3.5*bar_width for r in range(len(diagrams_rdul))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend(loc='center right', bbox_to_anchor=(1.14, 0.5))
plt.ylabel('Średnia długość rozwiązania')
plt.title('Średnia długość rozwiązania DFS')
plt.ylim(0, 30)
plt.show()



#dfs 2
diagrams_rdul = np.array([average_species(data, 5, 1, 'dfs', 'rdul'), average_species(data, 5, 2, 'dfs', 'rdul'), average_species(data, 5, 3, 'dfs', 'rdul'), average_species(data, 5, 4, 'dfs', 'rdul'), average_species(data, 5, 5, 'dfs', 'rdul'), average_species(data, 5, 6, 'dfs', 'rdul'), average_species(data, 5, 7, 'dfs', 'rdul')])
diagrams_rdlu = np.array([average_species(data, 5, 1, 'dfs', 'rdlu'), average_species(data, 5, 2, 'dfs', 'rdlu'), average_species(data, 5, 3, 'dfs', 'rdlu'), average_species(data, 5, 4, 'dfs', 'rdlu'), average_species(data, 5, 5, 'dfs', 'rdlu'), average_species(data, 5, 6, 'dfs', 'rdlu'), average_species(data, 5, 7, 'dfs', 'rdlu')])
diagrams_drul = np.array([average_species(data, 5, 1, 'dfs', 'drul'), average_species(data, 5, 2, 'dfs', 'drul'), average_species(data, 5, 3, 'dfs', 'drul'), average_species(data, 5, 4, 'dfs', 'drul'), average_species(data, 5, 5, 'dfs', 'drul'), average_species(data, 5, 6, 'dfs', 'drul'), average_species(data, 5, 7, 'dfs', 'drul')])
diagrams_drlu = np.array([average_species(data, 5, 1, 'dfs', 'drlu'), average_species(data, 5, 2, 'dfs', 'drlu'), average_species(data, 5, 3, 'dfs', 'drlu'), average_species(data, 5, 4, 'dfs', 'drlu'), average_species(data, 5, 5, 'dfs', 'drlu'), average_species(data, 5, 6, 'dfs', 'drlu'), average_species(data, 5, 7, 'dfs', 'drlu')])
diagrams_ludr = np.array([average_species(data, 5, 1, 'dfs', 'ludr'), average_species(data, 5, 2, 'dfs', 'ludr'), average_species(data, 5, 3, 'dfs', 'ludr'), average_species(data, 5, 4, 'dfs', 'ludr'), average_species(data, 5, 5, 'dfs', 'ludr'), average_species(data, 5, 6, 'dfs', 'ludr'), average_species(data, 5, 7, 'dfs', 'ludr')])
diagrams_lurd = np.array([average_species(data, 5, 1, 'dfs', 'lurd'), average_species(data, 5, 2, 'dfs', 'lurd'), average_species(data, 5, 3, 'dfs', 'lurd'), average_species(data, 5, 4, 'dfs', 'lurd'), average_species(data, 5, 5, 'dfs', 'lurd'), average_species(data, 5, 6, 'dfs', 'lurd'), average_species(data, 5, 7, 'dfs', 'lurd')])
diagrams_uldr = np.array([average_species(data, 5, 1, 'dfs', 'uldr'), average_species(data, 5, 2, 'dfs', 'uldr'), average_species(data, 5, 3, 'dfs', 'uldr'), average_species(data, 5, 4, 'dfs', 'uldr'), average_species(data, 5, 5, 'dfs', 'uldr'), average_species(data, 5, 6, 'dfs', 'uldr'), average_species(data, 5, 7, 'dfs', 'uldr')])
diagrams_ulrd = np.array([average_species(data, 5, 1, 'dfs', 'ulrd'), average_species(data, 5, 2, 'dfs', 'ulrd'), average_species(data, 5, 3, 'dfs', 'ulrd'), average_species(data, 5, 4, 'dfs', 'ulrd'), average_species(data, 5, 5, 'dfs', 'ulrd'), average_species(data, 5, 6, 'dfs', 'ulrd'), average_species(data, 5, 7, 'dfs', 'ulrd')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_rdul))
br2 = [x + bar_width for x in br1]
br3 = [x + bar_width for x in br2]
br4 = [x + bar_width for x in br3]
br5 = [x + bar_width for x in br4]
br6 = [x + bar_width for x in br5]
br7 = [x + bar_width for x in br6]
br8 = [x + bar_width for x in br7]
plt.bar(br1, diagrams_rdul, color = 'blue', width=bar_width, label='rdul')
plt.bar(br2, diagrams_rdlu, color = 'orange', width=bar_width, label='rdlu')
plt.bar(br3, diagrams_drul, color = 'green', width=bar_width, label='drul')
plt.bar(br4, diagrams_drlu, color = 'red', width=bar_width, label='drlu')
plt.bar(br5, diagrams_ludr, color = 'purple', width=bar_width, label='ludr')
plt.bar(br6 , diagrams_lurd, color = 'k', width=bar_width, label='lurd')
plt.bar(br7, diagrams_uldr, color = 'gray', width=bar_width, label='uldr')
plt.bar(br8, diagrams_ulrd, color = 'cornflowerblue', width=bar_width, label='ulrd')
plt.xticks([r + 3.5*bar_width for r in range(len(diagrams_rdul))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend(loc='center right', bbox_to_anchor=(1.14, 0.5))
plt.ylabel('Średnia liczba odwiedzonych stanów')
plt.title('Średnia liczba odwiedzonych stanów DFS')
plt.yticks([0, 10, 100, 1000, 10000, 100000, 1000000])
plt.yscale('log')
plt.show()

#dfs 3
diagrams_rdul = np.array([average_species(data, 6, 1, 'dfs', 'rdul'), average_species(data, 6, 2, 'dfs', 'rdul'), average_species(data, 6, 3, 'dfs', 'rdul'), average_species(data, 6, 4, 'dfs', 'rdul'), average_species(data, 6, 5, 'dfs', 'rdul'), average_species(data, 6, 6, 'dfs', 'rdul'), average_species(data, 6, 7, 'dfs', 'rdul')])
diagrams_rdlu = np.array([average_species(data, 6, 1, 'dfs', 'rdlu'), average_species(data, 6, 2, 'dfs', 'rdlu'), average_species(data, 6, 3, 'dfs', 'rdlu'), average_species(data, 6, 4, 'dfs', 'rdlu'), average_species(data, 6, 5, 'dfs', 'rdlu'), average_species(data, 6, 6, 'dfs', 'rdlu'), average_species(data, 6, 7, 'dfs', 'rdlu')])
diagrams_drul = np.array([average_species(data, 6, 1, 'dfs', 'drul'), average_species(data, 6, 2, 'dfs', 'drul'), average_species(data, 6, 3, 'dfs', 'drul'), average_species(data, 6, 4, 'dfs', 'drul'), average_species(data, 6, 5, 'dfs', 'drul'), average_species(data, 6, 6, 'dfs', 'drul'), average_species(data, 6, 7, 'dfs', 'drul')])
diagrams_drlu = np.array([average_species(data, 6, 1, 'dfs', 'drlu'), average_species(data, 6, 2, 'dfs', 'drlu'), average_species(data, 6, 3, 'dfs', 'drlu'), average_species(data, 6, 4, 'dfs', 'drlu'), average_species(data, 6, 5, 'dfs', 'drlu'), average_species(data, 6, 6, 'dfs', 'drlu'), average_species(data, 6, 7, 'dfs', 'drlu')])
diagrams_ludr = np.array([average_species(data, 6, 1, 'dfs', 'ludr'), average_species(data, 6, 2, 'dfs', 'ludr'), average_species(data, 6, 3, 'dfs', 'ludr'), average_species(data, 6, 4, 'dfs', 'ludr'), average_species(data, 6, 5, 'dfs', 'ludr'), average_species(data, 6, 6, 'dfs', 'ludr'), average_species(data, 6, 7, 'dfs', 'ludr')])
diagrams_lurd = np.array([average_species(data, 6, 1, 'dfs', 'lurd'), average_species(data, 6, 2, 'dfs', 'lurd'), average_species(data, 6, 3, 'dfs', 'lurd'), average_species(data, 6, 4, 'dfs', 'lurd'), average_species(data, 6, 5, 'dfs', 'lurd'), average_species(data, 6, 6, 'dfs', 'lurd'), average_species(data, 6, 7, 'dfs', 'lurd')])
diagrams_uldr = np.array([average_species(data, 6, 1, 'dfs', 'uldr'), average_species(data, 6, 2, 'dfs', 'uldr'), average_species(data, 6, 3, 'dfs', 'uldr'), average_species(data, 6, 4, 'dfs', 'uldr'), average_species(data, 6, 5, 'dfs', 'uldr'), average_species(data, 6, 6, 'dfs', 'uldr'), average_species(data, 6, 7, 'dfs', 'uldr')])
diagrams_ulrd = np.array([average_species(data, 6, 1, 'dfs', 'ulrd'), average_species(data, 6, 2, 'dfs', 'ulrd'), average_species(data, 6, 3, 'dfs', 'ulrd'), average_species(data, 6, 4, 'dfs', 'ulrd'), average_species(data, 6, 5, 'dfs', 'ulrd'), average_species(data, 6, 6, 'dfs', 'ulrd'), average_species(data, 6, 7, 'dfs', 'ulrd')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_rdul))
br2 = [x + bar_width for x in br1]
br3 = [x + bar_width for x in br2]
br4 = [x + bar_width for x in br3]
br5 = [x + bar_width for x in br4]
br6 = [x + bar_width for x in br5]
br7 = [x + bar_width for x in br6]
br8 = [x + bar_width for x in br7]
plt.bar(br1, diagrams_rdul, color = 'blue', width=bar_width, label='rdul')
plt.bar(br2, diagrams_rdlu, color = 'orange', width=bar_width, label='rdlu')
plt.bar(br3, diagrams_drul, color = 'green', width=bar_width, label='drul')
plt.bar(br4, diagrams_drlu, color = 'red', width=bar_width, label='drlu')
plt.bar(br5, diagrams_ludr, color = 'purple', width=bar_width, label='ludr')
plt.bar(br6 , diagrams_lurd, color = 'k', width=bar_width, label='lurd')
plt.bar(br7, diagrams_uldr, color = 'gray', width=bar_width, label='uldr')
plt.bar(br8, diagrams_ulrd, color = 'cornflowerblue', width=bar_width, label='ulrd')
plt.xticks([r + 3.5*bar_width for r in range(len(diagrams_rdul))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend(loc='center right', bbox_to_anchor=(1.14, 0.5))
plt.ylabel('Średnia liczba przetworzonych stanów')
plt.title('Średnia liczba przetworzonych stanów DFS')
plt.yticks([0, 10, 100, 1000, 10000, 100000, 1000000])
plt.yscale('log')
plt.show()

#dfs 4
diagrams_rdul = np.array([average_species(data, 7, 1, 'dfs', 'rdul'), average_species(data, 7, 2, 'dfs', 'rdul'), average_species(data, 7, 3, 'dfs', 'rdul'), average_species(data, 7, 4, 'dfs', 'rdul'), average_species(data, 7, 5, 'dfs', 'rdul'), average_species(data, 7, 6, 'dfs', 'rdul'), average_species(data, 7, 7, 'dfs', 'rdul')])
diagrams_rdlu = np.array([average_species(data, 7, 1, 'dfs', 'rdlu'), average_species(data, 7, 2, 'dfs', 'rdlu'), average_species(data, 7, 3, 'dfs', 'rdlu'), average_species(data, 7, 4, 'dfs', 'rdlu'), average_species(data, 7, 5, 'dfs', 'rdlu'), average_species(data, 7, 6, 'dfs', 'rdlu'), average_species(data, 7, 7, 'dfs', 'rdlu')])
diagrams_drul = np.array([average_species(data, 7, 1, 'dfs', 'drul'), average_species(data, 7, 2, 'dfs', 'drul'), average_species(data, 7, 3, 'dfs', 'drul'), average_species(data, 7, 4, 'dfs', 'drul'), average_species(data, 7, 5, 'dfs', 'drul'), average_species(data, 7, 6, 'dfs', 'drul'), average_species(data, 7, 7, 'dfs', 'drul')])
diagrams_drlu = np.array([average_species(data, 7, 1, 'dfs', 'drlu'), average_species(data, 7, 2, 'dfs', 'drlu'), average_species(data, 7, 3, 'dfs', 'drlu'), average_species(data, 7, 4, 'dfs', 'drlu'), average_species(data, 7, 5, 'dfs', 'drlu'), average_species(data, 7, 6, 'dfs', 'drlu'), average_species(data, 7, 7, 'dfs', 'drlu')])
diagrams_ludr = np.array([average_species(data, 7, 1, 'dfs', 'ludr'), average_species(data, 7, 2, 'dfs', 'ludr'), average_species(data, 7, 3, 'dfs', 'ludr'), average_species(data, 7, 4, 'dfs', 'ludr'), average_species(data, 7, 5, 'dfs', 'ludr'), average_species(data, 7, 6, 'dfs', 'ludr'), average_species(data, 7, 7, 'dfs', 'ludr')])
diagrams_lurd = np.array([average_species(data, 7, 1, 'dfs', 'lurd'), average_species(data, 7, 2, 'dfs', 'lurd'), average_species(data, 7, 3, 'dfs', 'lurd'), average_species(data, 7, 4, 'dfs', 'lurd'), average_species(data, 7, 5, 'dfs', 'lurd'), average_species(data, 7, 6, 'dfs', 'lurd'), average_species(data, 7, 7, 'dfs', 'lurd')])
diagrams_uldr = np.array([average_species(data, 7, 1, 'dfs', 'uldr'), average_species(data, 7, 2, 'dfs', 'uldr'), average_species(data, 7, 3, 'dfs', 'uldr'), average_species(data, 7, 4, 'dfs', 'uldr'), average_species(data, 7, 5, 'dfs', 'uldr'), average_species(data, 7, 6, 'dfs', 'uldr'), average_species(data, 7, 7, 'dfs', 'uldr')])
diagrams_ulrd = np.array([average_species(data, 7, 1, 'dfs', 'ulrd'), average_species(data, 7, 2, 'dfs', 'ulrd'), average_species(data, 7, 3, 'dfs', 'ulrd'), average_species(data, 7, 4, 'dfs', 'ulrd'), average_species(data, 7, 5, 'dfs', 'ulrd'), average_species(data, 7, 6, 'dfs', 'ulrd'), average_species(data, 7, 7, 'dfs', 'ulrd')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_rdul))
br2 = [x + bar_width for x in br1]
br3 = [x + bar_width for x in br2]
br4 = [x + bar_width for x in br3]
br5 = [x + bar_width for x in br4]
br6 = [x + bar_width for x in br5]
br7 = [x + bar_width for x in br6]
br8 = [x + bar_width for x in br7]
plt.bar(br1, diagrams_rdul, color = 'blue', width=bar_width, label='rdul')
plt.bar(br2, diagrams_rdlu, color = 'orange', width=bar_width, label='rdlu')
plt.bar(br3, diagrams_drul, color = 'green', width=bar_width, label='drul')
plt.bar(br4, diagrams_drlu, color = 'red', width=bar_width, label='drlu')
plt.bar(br5, diagrams_ludr, color = 'purple', width=bar_width, label='ludr')
plt.bar(br6 , diagrams_lurd, color = 'k', width=bar_width, label='lurd')
plt.bar(br7, diagrams_uldr, color = 'gray', width=bar_width, label='uldr')
plt.bar(br8, diagrams_ulrd, color = 'cornflowerblue', width=bar_width, label='ulrd')
plt.xticks([r + 3.5*bar_width for r in range(len(diagrams_rdul))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend(loc='center right', bbox_to_anchor=(1.14, 0.5))
plt.ylabel('Średni maksymalny poziom rekursji')
plt.title('Średni maksymalny poziom rekursji DFS')
plt.ylim(0, 25)
plt.show()

#dfs 5
diagrams_rdul = np.array([average_species(data, 8, 1, 'dfs', 'rdul'), average_species(data, 8, 2, 'dfs', 'rdul'), average_species(data, 8, 3, 'dfs', 'rdul'), average_species(data, 8, 4, 'dfs', 'rdul'), average_species(data, 8, 5, 'dfs', 'rdul'), average_species(data, 8, 6, 'dfs', 'rdul'), average_species(data, 8, 7, 'dfs', 'rdul')])
diagrams_rdlu = np.array([average_species(data, 8, 1, 'dfs', 'rdlu'), average_species(data, 8, 2, 'dfs', 'rdlu'), average_species(data, 8, 3, 'dfs', 'rdlu'), average_species(data, 8, 4, 'dfs', 'rdlu'), average_species(data, 8, 5, 'dfs', 'rdlu'), average_species(data, 8, 6, 'dfs', 'rdlu'), average_species(data, 8, 7, 'dfs', 'rdlu')])
diagrams_drul = np.array([average_species(data, 8, 1, 'dfs', 'drul'), average_species(data, 8, 2, 'dfs', 'drul'), average_species(data, 8, 3, 'dfs', 'drul'), average_species(data, 8, 4, 'dfs', 'drul'), average_species(data, 8, 5, 'dfs', 'drul'), average_species(data, 8, 6, 'dfs', 'drul'), average_species(data, 8, 7, 'dfs', 'drul')])
diagrams_drlu = np.array([average_species(data, 8, 1, 'dfs', 'drlu'), average_species(data, 8, 2, 'dfs', 'drlu'), average_species(data, 8, 3, 'dfs', 'drlu'), average_species(data, 8, 4, 'dfs', 'drlu'), average_species(data, 8, 5, 'dfs', 'drlu'), average_species(data, 8, 6, 'dfs', 'drlu'), average_species(data, 8, 7, 'dfs', 'drlu')])
diagrams_ludr = np.array([average_species(data, 8, 1, 'dfs', 'ludr'), average_species(data, 8, 2, 'dfs', 'ludr'), average_species(data, 8, 3, 'dfs', 'ludr'), average_species(data, 8, 4, 'dfs', 'ludr'), average_species(data, 8, 5, 'dfs', 'ludr'), average_species(data, 8, 6, 'dfs', 'ludr'), average_species(data, 8, 7, 'dfs', 'ludr')])
diagrams_lurd = np.array([average_species(data, 8, 1, 'dfs', 'lurd'), average_species(data, 8, 2, 'dfs', 'lurd'), average_species(data, 8, 3, 'dfs', 'lurd'), average_species(data, 8, 4, 'dfs', 'lurd'), average_species(data, 8, 5, 'dfs', 'lurd'), average_species(data, 8, 6, 'dfs', 'lurd'), average_species(data, 8, 7, 'dfs', 'lurd')])
diagrams_uldr = np.array([average_species(data, 8, 1, 'dfs', 'uldr'), average_species(data, 8, 2, 'dfs', 'uldr'), average_species(data, 8, 3, 'dfs', 'uldr'), average_species(data, 8, 4, 'dfs', 'uldr'), average_species(data, 8, 5, 'dfs', 'uldr'), average_species(data, 8, 6, 'dfs', 'uldr'), average_species(data, 8, 7, 'dfs', 'uldr')])
diagrams_ulrd = np.array([average_species(data, 8, 1, 'dfs', 'ulrd'), average_species(data, 8, 2, 'dfs', 'ulrd'), average_species(data, 8, 3, 'dfs', 'ulrd'), average_species(data, 8, 4, 'dfs', 'ulrd'), average_species(data, 8, 5, 'dfs', 'ulrd'), average_species(data, 8, 6, 'dfs', 'ulrd'), average_species(data, 8, 7, 'dfs', 'ulrd')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_rdul))
br2 = [x + bar_width for x in br1]
br3 = [x + bar_width for x in br2]
br4 = [x + bar_width for x in br3]
br5 = [x + bar_width for x in br4]
br6 = [x + bar_width for x in br5]
br7 = [x + bar_width for x in br6]
br8 = [x + bar_width for x in br7]
plt.bar(br1, diagrams_rdul, color = 'blue', width=bar_width, label='rdul')
plt.bar(br2, diagrams_rdlu, color = 'orange', width=bar_width, label='rdlu')
plt.bar(br3, diagrams_drul, color = 'green', width=bar_width, label='drul')
plt.bar(br4, diagrams_drlu, color = 'red', width=bar_width, label='drlu')
plt.bar(br5, diagrams_ludr, color = 'purple', width=bar_width, label='ludr')
plt.bar(br6 , diagrams_lurd, color = 'k', width=bar_width, label='lurd')
plt.bar(br7, diagrams_uldr, color = 'gray', width=bar_width, label='uldr')
plt.bar(br8, diagrams_ulrd, color = 'cornflowerblue', width=bar_width, label='ulrd')
plt.xticks([r + 3.5*bar_width for r in range(len(diagrams_rdul))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend(loc='center right', bbox_to_anchor=(1.14, 0.5))
plt.ylabel('Średni czas rozwiązania')
plt.title('Średni czas rozwiązania DFS')
plt.ylim(0, 6000)
plt.show()

#"""







'''
#bfs 1
diagrams_rdul = np.array([average_species(data, 4, 1, 'bfs', 'rdul'), average_species(data, 4, 2, 'bfs', 'rdul'), average_species(data, 4, 3, 'bfs', 'rdul'), average_species(data, 4, 4, 'bfs', 'rdul'), average_species(data, 4, 5, 'bfs', 'rdul'), average_species(data, 4, 6, 'bfs', 'rdul'), average_species(data, 4, 7, 'bfs', 'rdul')])
diagrams_rdlu = np.array([average_species(data, 4, 1, 'bfs', 'rdlu'), average_species(data, 4, 2, 'bfs', 'rdlu'), average_species(data, 4, 3, 'bfs', 'rdlu'), average_species(data, 4, 4, 'bfs', 'rdlu'), average_species(data, 4, 5, 'bfs', 'rdlu'), average_species(data, 4, 6, 'bfs', 'rdlu'), average_species(data, 4, 7, 'bfs', 'rdlu')])
diagrams_drul = np.array([average_species(data, 4, 1, 'bfs', 'drul'), average_species(data, 4, 2, 'bfs', 'drul'), average_species(data, 4, 3, 'bfs', 'drul'), average_species(data, 4, 4, 'bfs', 'drul'), average_species(data, 4, 5, 'bfs', 'drul'), average_species(data, 4, 6, 'bfs', 'drul'), average_species(data, 4, 7, 'bfs', 'drul')])
diagrams_drlu = np.array([average_species(data, 4, 1, 'bfs', 'drlu'), average_species(data, 4, 2, 'bfs', 'drlu'), average_species(data, 4, 3, 'bfs', 'drlu'), average_species(data, 4, 4, 'bfs', 'drlu'), average_species(data, 4, 5, 'bfs', 'drlu'), average_species(data, 4, 6, 'bfs', 'drlu'), average_species(data, 4, 7, 'bfs', 'drlu')])
diagrams_ludr = np.array([average_species(data, 4, 1, 'bfs', 'ludr'), average_species(data, 4, 2, 'bfs', 'ludr'), average_species(data, 4, 3, 'bfs', 'ludr'), average_species(data, 4, 4, 'bfs', 'ludr'), average_species(data, 4, 5, 'bfs', 'ludr'), average_species(data, 4, 6, 'bfs', 'ludr'), average_species(data, 4, 7, 'bfs', 'ludr')])
diagrams_lurd = np.array([average_species(data, 4, 1, 'bfs', 'lurd'), average_species(data, 4, 2, 'bfs', 'lurd'), average_species(data, 4, 3, 'bfs', 'lurd'), average_species(data, 4, 4, 'bfs', 'lurd'), average_species(data, 4, 5, 'bfs', 'lurd'), average_species(data, 4, 6, 'bfs', 'lurd'), average_species(data, 4, 7, 'bfs', 'lurd')])
diagrams_uldr = np.array([average_species(data, 4, 1, 'bfs', 'uldr'), average_species(data, 4, 2, 'bfs', 'uldr'), average_species(data, 4, 3, 'bfs', 'uldr'), average_species(data, 4, 4, 'bfs', 'uldr'), average_species(data, 4, 5, 'bfs', 'uldr'), average_species(data, 4, 6, 'bfs', 'uldr'), average_species(data, 4, 7, 'bfs', 'uldr')])
diagrams_ulrd = np.array([average_species(data, 4, 1, 'bfs', 'ulrd'), average_species(data, 4, 2, 'bfs', 'ulrd'), average_species(data, 4, 3, 'bfs', 'ulrd'), average_species(data, 4, 4, 'bfs', 'ulrd'), average_species(data, 4, 5, 'bfs', 'ulrd'), average_species(data, 4, 6, 'bfs', 'ulrd'), average_species(data, 4, 7, 'bfs', 'ulrd')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_rdul))
br2 = [x + bar_width for x in br1]
br3 = [x + bar_width for x in br2]
br4 = [x + bar_width for x in br3]
br5 = [x + bar_width for x in br4]
br6 = [x + bar_width for x in br5]
br7 = [x + bar_width for x in br6]
br8 = [x + bar_width for x in br7]
plt.bar(br1, diagrams_rdul, color = 'blue', width=bar_width, label='rdul')
plt.bar(br2, diagrams_rdlu, color = 'orange', width=bar_width, label='rdlu')
plt.bar(br3, diagrams_drul, color = 'green', width=bar_width, label='drul')
plt.bar(br4, diagrams_drlu, color = 'red', width=bar_width, label='drlu')
plt.bar(br5, diagrams_ludr, color = 'purple', width=bar_width, label='ludr')
plt.bar(br6 , diagrams_lurd, color = 'k', width=bar_width, label='lurd')
plt.bar(br7, diagrams_uldr, color = 'gray', width=bar_width, label='uldr')
plt.bar(br8, diagrams_ulrd, color = 'cornflowerblue', width=bar_width, label='ulrd')
plt.xticks([r + 3.5*bar_width for r in range(len(diagrams_rdul))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend(loc='center right', bbox_to_anchor=(1.14, 0.5))
plt.ylabel('Średnia długość rozwiązania')
plt.title('Średnia długość rozwiązania BFS')
plt.ylim(0, 8)
plt.show()



#bfs 2
diagrams_rdul = np.array([average_species(data, 5, 1, 'bfs', 'rdul'), average_species(data, 5, 2, 'bfs', 'rdul'), average_species(data, 5, 3, 'bfs', 'rdul'), average_species(data, 5, 4, 'bfs', 'rdul'), average_species(data, 5, 5, 'bfs', 'rdul'), average_species(data, 5, 6, 'bfs', 'rdul'), average_species(data, 5, 7, 'bfs', 'rdul')])
diagrams_rdlu = np.array([average_species(data, 5, 1, 'bfs', 'rdlu'), average_species(data, 5, 2, 'bfs', 'rdlu'), average_species(data, 5, 3, 'bfs', 'rdlu'), average_species(data, 5, 4, 'bfs', 'rdlu'), average_species(data, 5, 5, 'bfs', 'rdlu'), average_species(data, 5, 6, 'bfs', 'rdlu'), average_species(data, 5, 7, 'bfs', 'rdlu')])
diagrams_drul = np.array([average_species(data, 5, 1, 'bfs', 'drul'), average_species(data, 5, 2, 'bfs', 'drul'), average_species(data, 5, 3, 'bfs', 'drul'), average_species(data, 5, 4, 'bfs', 'drul'), average_species(data, 5, 5, 'bfs', 'drul'), average_species(data, 5, 6, 'bfs', 'drul'), average_species(data, 5, 7, 'bfs', 'drul')])
diagrams_drlu = np.array([average_species(data, 5, 1, 'bfs', 'drlu'), average_species(data, 5, 2, 'bfs', 'drlu'), average_species(data, 5, 3, 'bfs', 'drlu'), average_species(data, 5, 4, 'bfs', 'drlu'), average_species(data, 5, 5, 'bfs', 'drlu'), average_species(data, 5, 6, 'bfs', 'drlu'), average_species(data, 5, 7, 'bfs', 'drlu')])
diagrams_ludr = np.array([average_species(data, 5, 1, 'bfs', 'ludr'), average_species(data, 5, 2, 'bfs', 'ludr'), average_species(data, 5, 3, 'bfs', 'ludr'), average_species(data, 5, 4, 'bfs', 'ludr'), average_species(data, 5, 5, 'bfs', 'ludr'), average_species(data, 5, 6, 'bfs', 'ludr'), average_species(data, 5, 7, 'bfs', 'ludr')])
diagrams_lurd = np.array([average_species(data, 5, 1, 'bfs', 'lurd'), average_species(data, 5, 2, 'bfs', 'lurd'), average_species(data, 5, 3, 'bfs', 'lurd'), average_species(data, 5, 4, 'bfs', 'lurd'), average_species(data, 5, 5, 'bfs', 'lurd'), average_species(data, 5, 6, 'bfs', 'lurd'), average_species(data, 5, 7, 'bfs', 'lurd')])
diagrams_uldr = np.array([average_species(data, 5, 1, 'bfs', 'uldr'), average_species(data, 5, 2, 'bfs', 'uldr'), average_species(data, 5, 3, 'bfs', 'uldr'), average_species(data, 5, 4, 'bfs', 'uldr'), average_species(data, 5, 5, 'bfs', 'uldr'), average_species(data, 5, 6, 'bfs', 'uldr'), average_species(data, 5, 7, 'bfs', 'uldr')])
diagrams_ulrd = np.array([average_species(data, 5, 1, 'bfs', 'ulrd'), average_species(data, 5, 2, 'bfs', 'ulrd'), average_species(data, 5, 3, 'bfs', 'ulrd'), average_species(data, 5, 4, 'bfs', 'ulrd'), average_species(data, 5, 5, 'bfs', 'ulrd'), average_species(data, 5, 6, 'bfs', 'ulrd'), average_species(data, 5, 7, 'bfs', 'ulrd')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_rdul))
br2 = [x + bar_width for x in br1]
br3 = [x + bar_width for x in br2]
br4 = [x + bar_width for x in br3]
br5 = [x + bar_width for x in br4]
br6 = [x + bar_width for x in br5]
br7 = [x + bar_width for x in br6]
br8 = [x + bar_width for x in br7]
plt.bar(br1, diagrams_rdul, color = 'blue', width=bar_width, label='rdul')
plt.bar(br2, diagrams_rdlu, color = 'orange', width=bar_width, label='rdlu')
plt.bar(br3, diagrams_drul, color = 'green', width=bar_width, label='drul')
plt.bar(br4, diagrams_drlu, color = 'red', width=bar_width, label='drlu')
plt.bar(br5, diagrams_ludr, color = 'purple', width=bar_width, label='ludr')
plt.bar(br6 , diagrams_lurd, color = 'k', width=bar_width, label='lurd')
plt.bar(br7, diagrams_uldr, color = 'gray', width=bar_width, label='uldr')
plt.bar(br8, diagrams_ulrd, color = 'cornflowerblue', width=bar_width, label='ulrd')
plt.xticks([r + 3.5*bar_width for r in range(len(diagrams_rdul))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend(loc='center right', bbox_to_anchor=(1.14, 0.5))
plt.ylabel('Średnia liczba odwiedzonych stanów')
plt.title('Średnia liczba odwiedzonych stanów BFS')
plt.ylim(0, 500)
plt.show()

#bfs 3
diagrams_rdul = np.array([average_species(data, 6, 1, 'bfs', 'rdul'), average_species(data, 6, 2, 'bfs', 'rdul'), average_species(data, 6, 3, 'bfs', 'rdul'), average_species(data, 6, 4, 'bfs', 'rdul'), average_species(data, 6, 5, 'bfs', 'rdul'), average_species(data, 6, 6, 'bfs', 'rdul'), average_species(data, 6, 7, 'bfs', 'rdul')])
diagrams_rdlu = np.array([average_species(data, 6, 1, 'bfs', 'rdlu'), average_species(data, 6, 2, 'bfs', 'rdlu'), average_species(data, 6, 3, 'bfs', 'rdlu'), average_species(data, 6, 4, 'bfs', 'rdlu'), average_species(data, 6, 5, 'bfs', 'rdlu'), average_species(data, 6, 6, 'bfs', 'rdlu'), average_species(data, 6, 7, 'bfs', 'rdlu')])
diagrams_drul = np.array([average_species(data, 6, 1, 'bfs', 'drul'), average_species(data, 6, 2, 'bfs', 'drul'), average_species(data, 6, 3, 'bfs', 'drul'), average_species(data, 6, 4, 'bfs', 'drul'), average_species(data, 6, 5, 'bfs', 'drul'), average_species(data, 6, 6, 'bfs', 'drul'), average_species(data, 6, 7, 'bfs', 'drul')])
diagrams_drlu = np.array([average_species(data, 6, 1, 'bfs', 'drlu'), average_species(data, 6, 2, 'bfs', 'drlu'), average_species(data, 6, 3, 'bfs', 'drlu'), average_species(data, 6, 4, 'bfs', 'drlu'), average_species(data, 6, 5, 'bfs', 'drlu'), average_species(data, 6, 6, 'bfs', 'drlu'), average_species(data, 6, 7, 'bfs', 'drlu')])
diagrams_ludr = np.array([average_species(data, 6, 1, 'bfs', 'ludr'), average_species(data, 6, 2, 'bfs', 'ludr'), average_species(data, 6, 3, 'bfs', 'ludr'), average_species(data, 6, 4, 'bfs', 'ludr'), average_species(data, 6, 5, 'bfs', 'ludr'), average_species(data, 6, 6, 'bfs', 'ludr'), average_species(data, 6, 7, 'bfs', 'ludr')])
diagrams_lurd = np.array([average_species(data, 6, 1, 'bfs', 'lurd'), average_species(data, 6, 2, 'bfs', 'lurd'), average_species(data, 6, 3, 'bfs', 'lurd'), average_species(data, 6, 4, 'bfs', 'lurd'), average_species(data, 6, 5, 'bfs', 'lurd'), average_species(data, 6, 6, 'bfs', 'lurd'), average_species(data, 6, 7, 'bfs', 'lurd')])
diagrams_uldr = np.array([average_species(data, 6, 1, 'bfs', 'uldr'), average_species(data, 6, 2, 'bfs', 'uldr'), average_species(data, 6, 3, 'bfs', 'uldr'), average_species(data, 6, 4, 'bfs', 'uldr'), average_species(data, 6, 5, 'bfs', 'uldr'), average_species(data, 6, 6, 'bfs', 'uldr'), average_species(data, 6, 7, 'bfs', 'uldr')])
diagrams_ulrd = np.array([average_species(data, 6, 1, 'bfs', 'ulrd'), average_species(data, 6, 2, 'bfs', 'ulrd'), average_species(data, 6, 3, 'bfs', 'ulrd'), average_species(data, 6, 4, 'bfs', 'ulrd'), average_species(data, 6, 5, 'bfs', 'ulrd'), average_species(data, 6, 6, 'bfs', 'ulrd'), average_species(data, 6, 7, 'bfs', 'ulrd')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_rdul))
br2 = [x + bar_width for x in br1]
br3 = [x + bar_width for x in br2]
br4 = [x + bar_width for x in br3]
br5 = [x + bar_width for x in br4]
br6 = [x + bar_width for x in br5]
br7 = [x + bar_width for x in br6]
br8 = [x + bar_width for x in br7]
plt.bar(br1, diagrams_rdul, color = 'blue', width=bar_width, label='rdul')
plt.bar(br2, diagrams_rdlu, color = 'orange', width=bar_width, label='rdlu')
plt.bar(br3, diagrams_drul, color = 'green', width=bar_width, label='drul')
plt.bar(br4, diagrams_drlu, color = 'red', width=bar_width, label='drlu')
plt.bar(br5, diagrams_ludr, color = 'purple', width=bar_width, label='ludr')
plt.bar(br6 , diagrams_lurd, color = 'k', width=bar_width, label='lurd')
plt.bar(br7, diagrams_uldr, color = 'gray', width=bar_width, label='uldr')
plt.bar(br8, diagrams_ulrd, color = 'cornflowerblue', width=bar_width, label='ulrd')
plt.xticks([r + 3.5*bar_width for r in range(len(diagrams_rdul))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend(loc='center right', bbox_to_anchor=(1.14, 0.5))
plt.ylabel('Średnia liczba przetworzonych stanów')
plt.title('Średnia liczba przetworzonych stanów BFS')
plt.ylim(0, 1000)
plt.show()

#bfs 4
diagrams_rdul = np.array([average_species(data, 7, 1, 'bfs', 'rdul'), average_species(data, 7, 2, 'bfs', 'rdul'), average_species(data, 7, 3, 'bfs', 'rdul'), average_species(data, 7, 4, 'bfs', 'rdul'), average_species(data, 7, 5, 'bfs', 'rdul'), average_species(data, 7, 6, 'bfs', 'rdul'), average_species(data, 7, 7, 'bfs', 'rdul')])
diagrams_rdlu = np.array([average_species(data, 7, 1, 'bfs', 'rdlu'), average_species(data, 7, 2, 'bfs', 'rdlu'), average_species(data, 7, 3, 'bfs', 'rdlu'), average_species(data, 7, 4, 'bfs', 'rdlu'), average_species(data, 7, 5, 'bfs', 'rdlu'), average_species(data, 7, 6, 'bfs', 'rdlu'), average_species(data, 7, 7, 'bfs', 'rdlu')])
diagrams_drul = np.array([average_species(data, 7, 1, 'bfs', 'drul'), average_species(data, 7, 2, 'bfs', 'drul'), average_species(data, 7, 3, 'bfs', 'drul'), average_species(data, 7, 4, 'bfs', 'drul'), average_species(data, 7, 5, 'bfs', 'drul'), average_species(data, 7, 6, 'bfs', 'drul'), average_species(data, 7, 7, 'bfs', 'drul')])
diagrams_drlu = np.array([average_species(data, 7, 1, 'bfs', 'drlu'), average_species(data, 7, 2, 'bfs', 'drlu'), average_species(data, 7, 3, 'bfs', 'drlu'), average_species(data, 7, 4, 'bfs', 'drlu'), average_species(data, 7, 5, 'bfs', 'drlu'), average_species(data, 7, 6, 'bfs', 'drlu'), average_species(data, 7, 7, 'bfs', 'drlu')])
diagrams_ludr = np.array([average_species(data, 7, 1, 'bfs', 'ludr'), average_species(data, 7, 2, 'bfs', 'ludr'), average_species(data, 7, 3, 'bfs', 'ludr'), average_species(data, 7, 4, 'bfs', 'ludr'), average_species(data, 7, 5, 'bfs', 'ludr'), average_species(data, 7, 6, 'bfs', 'ludr'), average_species(data, 7, 7, 'bfs', 'ludr')])
diagrams_lurd = np.array([average_species(data, 7, 1, 'bfs', 'lurd'), average_species(data, 7, 2, 'bfs', 'lurd'), average_species(data, 7, 3, 'bfs', 'lurd'), average_species(data, 7, 4, 'bfs', 'lurd'), average_species(data, 7, 5, 'bfs', 'lurd'), average_species(data, 7, 6, 'bfs', 'lurd'), average_species(data, 7, 7, 'bfs', 'lurd')])
diagrams_uldr = np.array([average_species(data, 7, 1, 'bfs', 'uldr'), average_species(data, 7, 2, 'bfs', 'uldr'), average_species(data, 7, 3, 'bfs', 'uldr'), average_species(data, 7, 4, 'bfs', 'uldr'), average_species(data, 7, 5, 'bfs', 'uldr'), average_species(data, 7, 6, 'bfs', 'uldr'), average_species(data, 7, 7, 'bfs', 'uldr')])
diagrams_ulrd = np.array([average_species(data, 7, 1, 'bfs', 'ulrd'), average_species(data, 7, 2, 'bfs', 'ulrd'), average_species(data, 7, 3, 'bfs', 'ulrd'), average_species(data, 7, 4, 'bfs', 'ulrd'), average_species(data, 7, 5, 'bfs', 'ulrd'), average_species(data, 7, 6, 'bfs', 'ulrd'), average_species(data, 7, 7, 'bfs', 'ulrd')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_rdul))
br2 = [x + bar_width for x in br1]
br3 = [x + bar_width for x in br2]
br4 = [x + bar_width for x in br3]
br5 = [x + bar_width for x in br4]
br6 = [x + bar_width for x in br5]
br7 = [x + bar_width for x in br6]
br8 = [x + bar_width for x in br7]
plt.bar(br1, diagrams_rdul, color = 'blue', width=bar_width, label='rdul')
plt.bar(br2, diagrams_rdlu, color = 'orange', width=bar_width, label='rdlu')
plt.bar(br3, diagrams_drul, color = 'green', width=bar_width, label='drul')
plt.bar(br4, diagrams_drlu, color = 'red', width=bar_width, label='drlu')
plt.bar(br5, diagrams_ludr, color = 'purple', width=bar_width, label='ludr')
plt.bar(br6 , diagrams_lurd, color = 'k', width=bar_width, label='lurd')
plt.bar(br7, diagrams_uldr, color = 'gray', width=bar_width, label='uldr')
plt.bar(br8, diagrams_ulrd, color = 'cornflowerblue', width=bar_width, label='ulrd')
plt.xticks([r + 3.5*bar_width for r in range(len(diagrams_rdul))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend(loc='center right', bbox_to_anchor=(1.14, 0.5))
plt.ylabel('Średni maksymalny poziom rekursji')
plt.title('Średni maksymalny poziom rekursji BFS')
plt.ylim(0, 8)
plt.show()

#bfs 5
diagrams_rdul = np.array([average_species(data, 8, 1, 'bfs', 'rdul'), average_species(data, 8, 2, 'bfs', 'rdul'), average_species(data, 8, 3, 'bfs', 'rdul'), average_species(data, 8, 4, 'bfs', 'rdul'), average_species(data, 8, 5, 'bfs', 'rdul'), average_species(data, 8, 6, 'bfs', 'rdul'), average_species(data, 8, 7, 'bfs', 'rdul')])
diagrams_rdlu = np.array([average_species(data, 8, 1, 'bfs', 'rdlu'), average_species(data, 8, 2, 'bfs', 'rdlu'), average_species(data, 8, 3, 'bfs', 'rdlu'), average_species(data, 8, 4, 'bfs', 'rdlu'), average_species(data, 8, 5, 'bfs', 'rdlu'), average_species(data, 8, 6, 'bfs', 'rdlu'), average_species(data, 8, 7, 'bfs', 'rdlu')])
diagrams_drul = np.array([average_species(data, 8, 1, 'bfs', 'drul'), average_species(data, 8, 2, 'bfs', 'drul'), average_species(data, 8, 3, 'bfs', 'drul'), average_species(data, 8, 4, 'bfs', 'drul'), average_species(data, 8, 5, 'bfs', 'drul'), average_species(data, 8, 6, 'bfs', 'drul'), average_species(data, 8, 7, 'bfs', 'drul')])
diagrams_drlu = np.array([average_species(data, 8, 1, 'bfs', 'drlu'), average_species(data, 8, 2, 'bfs', 'drlu'), average_species(data, 8, 3, 'bfs', 'drlu'), average_species(data, 8, 4, 'bfs', 'drlu'), average_species(data, 8, 5, 'bfs', 'drlu'), average_species(data, 8, 6, 'bfs', 'drlu'), average_species(data, 8, 7, 'bfs', 'drlu')])
diagrams_ludr = np.array([average_species(data, 8, 1, 'bfs', 'ludr'), average_species(data, 8, 2, 'bfs', 'ludr'), average_species(data, 8, 3, 'bfs', 'ludr'), average_species(data, 8, 4, 'bfs', 'ludr'), average_species(data, 8, 5, 'bfs', 'ludr'), average_species(data, 8, 6, 'bfs', 'ludr'), average_species(data, 8, 7, 'bfs', 'ludr')])
diagrams_lurd = np.array([average_species(data, 8, 1, 'bfs', 'lurd'), average_species(data, 8, 2, 'bfs', 'lurd'), average_species(data, 8, 3, 'bfs', 'lurd'), average_species(data, 8, 4, 'bfs', 'lurd'), average_species(data, 8, 5, 'bfs', 'lurd'), average_species(data, 8, 6, 'bfs', 'lurd'), average_species(data, 8, 7, 'bfs', 'lurd')])
diagrams_uldr = np.array([average_species(data, 8, 1, 'bfs', 'uldr'), average_species(data, 8, 2, 'bfs', 'uldr'), average_species(data, 8, 3, 'bfs', 'uldr'), average_species(data, 8, 4, 'bfs', 'uldr'), average_species(data, 8, 5, 'bfs', 'uldr'), average_species(data, 8, 6, 'bfs', 'uldr'), average_species(data, 8, 7, 'bfs', 'uldr')])
diagrams_ulrd = np.array([average_species(data, 8, 1, 'bfs', 'ulrd'), average_species(data, 8, 2, 'bfs', 'ulrd'), average_species(data, 8, 3, 'bfs', 'ulrd'), average_species(data, 8, 4, 'bfs', 'ulrd'), average_species(data, 8, 5, 'bfs', 'ulrd'), average_species(data, 8, 6, 'bfs', 'ulrd'), average_species(data, 8, 7, 'bfs', 'ulrd')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_rdul))
br2 = [x + bar_width for x in br1]
br3 = [x + bar_width for x in br2]
br4 = [x + bar_width for x in br3]
br5 = [x + bar_width for x in br4]
br6 = [x + bar_width for x in br5]
br7 = [x + bar_width for x in br6]
br8 = [x + bar_width for x in br7]
plt.bar(br1, diagrams_rdul, color = 'blue', width=bar_width, label='rdul')
plt.bar(br2, diagrams_rdlu, color = 'orange', width=bar_width, label='rdlu')
plt.bar(br3, diagrams_drul, color = 'green', width=bar_width, label='drul')
plt.bar(br4, diagrams_drlu, color = 'red', width=bar_width, label='drlu')
plt.bar(br5, diagrams_ludr, color = 'purple', width=bar_width, label='ludr')
plt.bar(br6 , diagrams_lurd, color = 'k', width=bar_width, label='lurd')
plt.bar(br7, diagrams_uldr, color = 'gray', width=bar_width, label='uldr')
plt.bar(br8, diagrams_ulrd, color = 'cornflowerblue', width=bar_width, label='ulrd')
plt.xticks([r + 3.5*bar_width for r in range(len(diagrams_rdul))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend(loc='center right', bbox_to_anchor=(1.14, 0.5))
plt.ylabel('Średni czas rozwiązania')
plt.title('Średni czas rozwiązania BFS')
plt.show()
'''









'''
bar_width = 0.3
#astr 1
diagrams_hamm = np.array([average_species(data, 4, 1, 'astr', 'hamm'), average_species(data, 4, 2, 'astr', 'hamm'), average_species(data, 4, 3, 'astr', 'hamm'), average_species(data, 4, 4, 'astr', 'hamm'), average_species(data, 4, 5, 'astr', 'hamm'), average_species(data, 4, 6, 'astr', 'hamm'), average_species(data, 4, 7, 'astr', 'hamm')])
diagrams_manh = np.array([average_species(data, 4, 1, 'astr', 'manh'), average_species(data, 4, 2, 'astr', 'manh'), average_species(data, 4, 3, 'astr', 'manh'), average_species(data, 4, 4, 'astr', 'manh'), average_species(data, 4, 5, 'astr', 'manh'), average_species(data, 4, 6, 'astr', 'manh'), average_species(data, 4, 7, 'astr', 'manh')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_hamm))
br2 = [x + bar_width for x in br1]

plt.bar(br1, diagrams_hamm, color = 'blue', width=bar_width, label='hamm')
plt.bar(br2, diagrams_manh, color = 'orange', width=bar_width, label='manh')

plt.xticks([r + bar_width/2 for r in range(len(diagrams_hamm))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend()
plt.ylabel('Średnia długość rozwiązania')
plt.title('Średnia długość rozwiązania ASTR')
plt.ylim(0, 10)
plt.show()



#astr 2
diagrams_hamm = np.array([average_species(data, 5, 1, 'astr', 'hamm'), average_species(data, 5, 2, 'astr', 'hamm'), average_species(data, 5, 3, 'astr', 'hamm'), average_species(data, 5, 4, 'astr', 'hamm'), average_species(data, 5, 5, 'astr', 'hamm'), average_species(data, 5, 6, 'astr', 'hamm'), average_species(data, 5, 7, 'astr', 'hamm')])
diagrams_manh = np.array([average_species(data, 5, 1, 'astr', 'manh'), average_species(data, 5, 2, 'astr', 'manh'), average_species(data, 5, 3, 'astr', 'manh'), average_species(data, 5, 4, 'astr', 'manh'), average_species(data, 5, 5, 'astr', 'manh'), average_species(data, 5, 6, 'astr', 'manh'), average_species(data, 5, 7, 'astr', 'manh')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_hamm))
br2 = [x + bar_width for x in br1]

plt.bar(br1, diagrams_hamm, color = 'blue', width=bar_width, label='hamm')
plt.bar(br2, diagrams_manh, color = 'orange', width=bar_width, label='manh')

plt.xticks([r + bar_width/2 for r in range(len(diagrams_hamm))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend()
plt.ylabel('Średnia liczba odwiedzonych stanów')
plt.title('Średnia liczba odwiedzonych stanów ASTR')

plt.show()

#astr 3
diagrams_hamm = np.array([average_species(data, 6, 1, 'astr', 'hamm'), average_species(data, 6, 2, 'astr', 'hamm'), average_species(data, 6, 3, 'astr', 'hamm'), average_species(data, 6, 4, 'astr', 'hamm'), average_species(data, 6, 5, 'astr', 'hamm'), average_species(data, 6, 6, 'astr', 'hamm'), average_species(data, 6, 7, 'astr', 'hamm')])
diagrams_manh = np.array([average_species(data, 6, 1, 'astr', 'manh'), average_species(data, 6, 2, 'astr', 'manh'), average_species(data, 6, 3, 'astr', 'manh'), average_species(data, 6, 4, 'astr', 'manh'), average_species(data, 6, 5, 'astr', 'manh'), average_species(data, 6, 6, 'astr', 'manh'), average_species(data, 6, 7, 'astr', 'manh')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_hamm))
br2 = [x + bar_width for x in br1]

plt.bar(br1, diagrams_hamm, color = 'blue', width=bar_width, label='hamm')
plt.bar(br2, diagrams_manh, color = 'orange', width=bar_width, label='manh')

plt.xticks([r + bar_width/2 for r in range(len(diagrams_hamm))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend()
plt.ylabel('Średnia liczba przetworzonych stanów')
plt.title('Średnia liczba przetworzonych stanów ASTR')
plt.ylim(0, 25)
plt.show()

#astr 4
diagrams_hamm = np.array([average_species(data, 7, 1, 'astr', 'hamm'), average_species(data, 7, 2, 'astr', 'hamm'), average_species(data, 7, 3, 'astr', 'hamm'), average_species(data, 7, 4, 'astr', 'hamm'), average_species(data, 7, 5, 'astr', 'hamm'), average_species(data, 7, 6, 'astr', 'hamm'), average_species(data, 7, 7, 'astr', 'hamm')])
diagrams_manh = np.array([average_species(data, 7, 1, 'astr', 'manh'), average_species(data, 7, 2, 'astr', 'manh'), average_species(data, 7, 3, 'astr', 'manh'), average_species(data, 7, 4, 'astr', 'manh'), average_species(data, 7, 5, 'astr', 'manh'), average_species(data, 7, 6, 'astr', 'manh'), average_species(data, 7, 7, 'astr', 'manh')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_hamm))
br2 = [x + bar_width for x in br1]

plt.bar(br1, diagrams_hamm, color = 'blue', width=bar_width, label='hamm')
plt.bar(br2, diagrams_manh, color = 'orange', width=bar_width, label='manh')

plt.xticks([r + bar_width/2 for r in range(len(diagrams_hamm))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend()
plt.ylabel('Średni maksymalny poziom rekursji')
plt.title('Średni maksymalny poziom rekursji ASTR')
plt.ylim(0, 10)
plt.show()

#astr 5
diagrams_hamm = np.array([average_species(data, 8, 1, 'astr', 'hamm'), average_species(data, 8, 2, 'astr', 'hamm'), average_species(data, 8, 3, 'astr', 'hamm'), average_species(data, 8, 4, 'astr', 'hamm'), average_species(data, 8, 5, 'astr', 'hamm'), average_species(data, 8, 6, 'astr', 'hamm'), average_species(data, 8, 7, 'astr', 'hamm')])
diagrams_manh = np.array([average_species(data, 8, 1, 'astr', 'manh'), average_species(data, 8, 2, 'astr', 'manh'), average_species(data, 8, 3, 'astr', 'manh'), average_species(data, 8, 4, 'astr', 'manh'), average_species(data, 8, 5, 'astr', 'manh'), average_species(data, 8, 6, 'astr', 'manh'), average_species(data, 8, 7, 'astr', 'manh')])

qw = ["1", "2", "3", "4", "5", "6", "7"]
br1 = np.arange(len(diagrams_hamm))
br2 = [x + bar_width for x in br1]

plt.bar(br1, diagrams_hamm, color = 'blue', width=bar_width, label='hamm')
plt.bar(br2, diagrams_manh, color = 'orange', width=bar_width, label='manh')

plt.xticks([r + bar_width/2 for r in range(len(diagrams_hamm))],
        ["1", "2", "3", "4", "5", "6", "7"])

plt.legend()
plt.ylabel('Średni czas rozwiązania')
plt.title('Średni czas rozwiązania ASTR')
plt.show()
'''