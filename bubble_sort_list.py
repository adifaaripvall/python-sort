def selection_sort(pemain):
    n = len(pemain)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if pemain[j][2] > pemain[min_index][2]:
                min_index = j
        pemain[i], pemain[min_index] = pemain[min_index], pemain[i]

#daftar pemain
pemain = [
    ["Kylian Mbappe", "Paris Saint Germain", "40"],
    ["Victor Osismhen", "Napoli", "28"],
    ["Robert Lewandowski", "Barcelona", "33"],
    ["Erling Haaland", "Manchester City", "52"],
    ["Christopher Nkuku", "RB Leipzig", "22"]
]

# Memanggil fungsi selection_sort untuk mengurutkan daftar pemain
selection_sort(pemain)

# Mencetak daftar pemain yang telah diurutkan
print("Hasil pengurutan secara descending : ", pemain)
