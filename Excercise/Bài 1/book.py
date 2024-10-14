class Book:
    _id_book = 10000

    def __init__(self, book_title, author, major, year_public) -> None:
        self.id_book = Book._id_book    
        Book._id_book += 1
        self.book_title = book_title
        self.author = author
        self.major = major
        self.year_public = year_public

    def __str__(self) -> str:
        return f"Mã sách: {self.id_book}, Tên sách: {self.book_title}, Tác giả: {self.author}, Chuyên ngành: {self.major}, Năm xuất bản: {self.year_public}"