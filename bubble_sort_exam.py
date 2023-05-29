def bubble_sort(nilai):
    n = len(nilai)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nilai[j] > nilai[j + 1]:
                nilai[j], nilai[j + 1] = nilai[j + 1], nilai[j]

# Daftar nilai ujian
nilai = [78, 65, 90, 82, 70]

# Memanggil fungsi bubble_sort untuk mengurutkan daftar nilai
bubble_sort(nilai)

# Mencetak daftar nilai yang telah diurutkan
print("Daftar nilai setelah diurutkan:", nilai)
