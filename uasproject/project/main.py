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

       