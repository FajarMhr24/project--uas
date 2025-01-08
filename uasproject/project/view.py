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
