import numpy as np
import matplotlib.pyplot as plt

#zbieram dane z plików i kontrolnie zapiusje je do innego pliku
text = np.loadtxt("1.txt", delimiter=";", dtype=float, skiprows=9)
file_path = r"C:\Users\Doge\AppData\Local\Programs\Python\Python38-32\cos.txt"
with open(file_path, 'w') as file:
    for element in text:
        file.write(str(element) + '\n')

#zbieram dane z całego array danych z badania
naprezenie = text[:, 0] / (0.98 * 2.1)
odleg = text[:, 4] / 5

#usuwam odległości i naprężenia aż do rozciągania elastycznego i skaluje arraye

dim_odl = odleg.size
dim_naprezenie = naprezenie.size
skal= dim_naprezenie - dim_odl
naprezenie = naprezenie[skal:]
zmiana = np.gradient(naprezenie, odleg)

scaled_zmiana = (zmiana - np.min(zmiana)) / (np.max(zmiana) - np.min(zmiana)) * 200 - 100
#robie wykres rozciogania
plt.plot(odleg, naprezenie)
plt.plot(odleg, scaled_zmiana)
plt.xlabel('sila')
plt.ylabel('moc')
plt.title('sds')
plt.show()

print(text[1, 0])
print(dim_naprezenie)
print(dim_odl)

odleg=odleg[odleg >= 0.085]
print(odleg.size)
print("SDSD")
print(text[:, 0])