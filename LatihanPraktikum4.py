# Buat list dengan 5 elemen
my_list = [10, 20, 30, 40, 50]

# Akses list
# Tampilkan elemen ke 3
print("Elemen ke 3:", my_list[2])

# Ambil nilai elemen ke 2 sampai elemen ke 4
subset = my_list[1:4]
print("Elemen ke 2 sampai ke 4:", subset)

# Ambil elemen terakhir
last_element = my_list[-1]
print("Elemen terakhir:", last_element)

# Ubah elemen list
# Ubah elemen ke 4 dengan nilai lainnya
my_list[3] = 45
print("List setelah mengubah elemen ke 4:", my_list)

# Ubah elemen ke 4 sampai dengan elemen terakhir
my_list[3:] = [50, 60, 70]
print("List setelah mengubah elemen ke 4 sampai dengan elemen terakhir:", my_list)

# Tambah elemen list
# Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
list_A = my_list[:2]
list_B = list_A.copy()

# Tambah list B dengan nilai string
list_B.append("hello")

# Tambah list B dengan 3 nilai
list_B.extend([3, 6, 9])

# Gabungkan list B dengan list A
combined_list = list_B + list_A

# Tampilkan hasil
print("List A:", list_A)
print("List B:", list_B)
print("Gabungan List B dengan List A:", combined_list)