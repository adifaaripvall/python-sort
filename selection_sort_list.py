def selection_sort(angka):
    n = len(angka)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if angka[j] < angka[min_index]:
                min_index = j
        angka[i], angka[min_index] = angka[min_index], angka[i]

#Daftar angka
angka = [9, 5, 3, 8, 2]

# Memanggil fungsi selection_sort untuk mengurutkan daftar angka
selection_sort(angka)

# Mencetak daftar nilai yang telah diurutkan
print("Hasil pengurutan secara ascending : ", angka)
