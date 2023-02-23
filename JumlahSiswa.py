# l = int(input("Jumlah siswa laki-laki: "))
# p = int(input("Jumlah siswa perempuan: "))
# ll = int(l / 10)
# pp = int(p / 10)
# print("Laki-laki: ", ("*" * ll), "(", l ,")" )
# print("Perempuan: ", ("*" * pp), "(", p ,")" )



# alternate solution
# module
import matplotlib.pyplot as plt

# input
l = int(input("Jumlah siswa laki-laki: "))
p = int(input("Jumlah siswa perempuan: "))

# diagram
y = ['perempuan', 'laki-laki']
x = [p, l]
plt.barh(y,x)

plt.ylabel("jenis kelamin")
plt.xlabel("jumlah")
plt.title("Grafik jumlah siswa")
plt.show()