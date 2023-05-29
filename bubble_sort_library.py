def bubble_sort(buku):
    n = len(buku)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if int(buku[j][2]) > int(buku[j + 1][2]):
                buku[j], buku[j + 1] = buku[j + 1], buku[j]

#Daftar Buku (Judul,Penulis,Jumlah Halaman)
buku = [
    ["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "320"],
    ["To Kill a Mockingbird", "Harper Lee", "281"],
    ["The Great Gatsby", "F. Scott Fitzgerald", "180"],
    ["Pride and Prejudice", "Jane Austen", "432"],
    ["1984", "George Orwell", "328"]
]

#Memanggil fungsi bubble_sort untuk mengurutkan daftar buku
bubble_sort(buku)

#Mencetak hasil pengurutan
print("Hasil pengurutan berdasarkan jumlah halaman secara ascending:")
for item in buku:
    print(item)
