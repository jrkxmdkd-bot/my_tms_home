from HOMEWORK_DB.data_provider import DataProvider


ACTION_ITEMS = """
Choose action item from the list:
    1. add author
    2. add book
    3. add genre
    4. add book genre
    5. get book by genre
    6. get book by author and year
    7. exit
"""


class ConsoleDbApp:
    def __init__(self, raw_data_provider, orm_data_provider):
        self.data_provider: DataProvider | None = None
        self.raw_data_provider = raw_data_provider
        self.orm_data_provider = orm_data_provider

    def start_app(self):
        choose = int(input('Choose data provider for initialization: 1 - raw  2 - orm: '))
        self.data_provider = self.raw_data_provider if choose == 1 else self.orm_data_provider

        print('Starting ConsoleApp ...')
        self.data_provider.create_tables()

        while True:
            action_item = int(input(ACTION_ITEMS))

            match action_item:
                case 1:
                    author_name = input('Enter author name ')
                    author_id = self.data_provider.add_author(author_name)
                    print(f"Author added id: {author_id}")
                case 2:
                    book_name = input('Enter book name ')
                    publication_year = input('Enter publication year ')
                    author_id = input('Enter author id ')
                    book_id = self.data_provider.add_book(book_name, publication_year, author_id)
                    print(f"Book added id: {book_id}")

