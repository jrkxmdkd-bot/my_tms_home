from classes import Book, Library, InvalidValueError

if __name__ == "__main__":
    try:
        lib = Library()

        b1 = Book(pages=320, year=2005, author="Толстой", price=550)
        b2 = Book(pages=210, year=1999, author="Достоевский", price=400)
        b3 = Book(pages=150, year=2010, author="Пушкин", price=350)

        lib.add_book(b1)
        lib.add_book(b2)
        lib.add_book(b3)

        print("Все книги в библиотеке:")
        print(lib)

        print("\nПоиск книг Пушкина:")
        for book in lib.find_by_author("Пушкин"):
            print(book)

        print("\nСравнение по цене:")
        print(f"Дороже ли Толстой, чем Достоевский? {b1 > b2}")

    except InvalidValueError as e:
        print("Ошибка при создании книги:", e)
