from secrets import token_hex


def iterable(item):
    return type(item) in (list, tuple, set)


class BookCollection:
    def __init__(self):
        self.books = []

    def add(self, *books):
        for item in books:
            if not iterable(item):
                self.books.append(item)
                continue
            self.books.extend(item)

    def remove(self, book_title):
        self.books.remove(book_title)

    def __iter__(self):
        return iter(self.books)

    def __repr__(self):
        return f'<BookColl: {self.books!r}>'


class Book:
    def __init__(self, title=None) -> None:
        if title is None:
            self.title = token_hex(3)
            return
        self.title = title

    def __repr__(self):
        return f'<Book: {self.title!r}>'

    def __eq__(self, other) -> bool:
        return self.title == other.title

    def __ne__(self, other) -> bool:
        return self.title != other.title

    def __hash__(self) -> int:  # So can add to set()
        return hash(self.title)


b1 = Book('1')
b2 = Book('2')
b3 = Book('2')
bA = Book('A')
b4 = Book()
b5 = Book()
b6 = Book()

bc1 = BookCollection()


def iter_coll(coll: BookCollection) -> None:
    iter1 = iter(coll)
    while True:
        try:
            book = next(iter1)
            print(book)
        except StopIteration:
            break
