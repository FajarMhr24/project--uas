# project--uas

Nama : Fajar Maher Habibillah

NIM : 312410549

Kelas : TI.24.A5

Mata Kuliah : Bahasa Pemograman

Dosen Pengampu : Agung Nugroho, S.Kom., M.Kom.

## link proses kode
https://youtu.be/i2PeAKHTCW4?si=MXU8T3_7Inf5thCf

## penjelas kode program

### ```Class book(Data.py)```

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
```
`__init__ Method`
Konstruktor untuk menginisialisasi atribut `title,` `author`, dan `year` saat objek dibuat.

`__str__ Method`
Mengembalikan representasi string dari objek buku dalam format:
"`Title by Author (Year)"`.

### ```Class bookmanager(proses.py)```

```python
from data import Book

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)

    def get_books(self):
        return self.books
```
`self.books`

- Menyimpan daftar buku sebagai list kosong.

`add_book(title, author, year)`

- Menambahkan buku baru ke dalam `self.books` menggunakan kelas `Book`.

`get_books()`

- Mengembalikan daftar buku yang tersimpan.

### ```Class bookview(view.py)```
```python
class BookView:
    @staticmethod
    def display_books(books):
        if not books:
            print("Daftar buku kosong.")
        else:
            print("\nDaftar Buku:")
            for index, book in enumerate(books, start=1):
                print(f"{index}. {book}")

    @staticmethod
    def get_book_input():
        title = input("Masukkan judul buku: ")
        author = input("Masukkan nama pengarang: ")
        year = input("Masukkan tahun terbit: ")
        return title, author, year

    @staticmethod
    def show_message(message):
        print(message)
```
`display_books(books)`

- Menampilkan daftar buku.
- Jika kosong, mencetak: "Daftar buku kosong."

`get_book_input()`

- Meminta input pengguna: judul, pengarang, dan tahun terbit.
- Mengembalikan data dalam bentuk `(title, author, year)`.

`show_message(message)`

- Menampilkan pesan ke layar.

### ```main.py```

```python

from view import BookView
from process import BookManager

def main():
    book_manager = BookManager()
    view = BookView()

    while True:
        print("\nMenu:")
        print("1. Tambahkan Buku")
        print("2. Lihat Daftar Buku")
        print("3. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            title, author, year = view.get_book_input()
            book_manager.add_book(title, author, year)
            view.show_message("Buku berhasil ditambahkan!")
        elif pilihan == "2":
            books = book_manager.get_books()
            view.display_books(books)
        elif pilihan == "3":
            view.show_message("Terima kasih telah menggunakan program ini!")
            break
        else:
            view.show_message("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
```

1. Import`class`

- `BookView` (untuk tampilan).

- `BookManager` (untuk pengelolaan buku).

2. Fungsi `main()`

- Menampilkan menu dengan opsi:

  - 1: Tambah Buku (menggunakan `add_book)`.
  
  - 2: Lihat Daftar Buku (menggunakan `display_books`).
  
  - 3: Keluar program.

3. Eksekusi Program

- `if __name__ == "__main__"`: menjalankan `main()` saat file di-eksekusi.


## output
![foto](https://github.com/FajarMhr24/foto/blob/55b582ae82adf2bb7d2c8fec1ca404a38332bcc4/Screenshot_20250116_061058.png) 

