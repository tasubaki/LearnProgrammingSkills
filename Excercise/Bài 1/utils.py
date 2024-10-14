from reader import Reader
from book import Book

def input_list_book():
    list_book = []
    quantity_book = int(input("Nhập số lượng sách: "))

    for _ in range(quantity_book):
        book_title = input("Nhập tên sách: ")
        author = input("Nhập tác giả: ")
        major = input("Nhập chuyên ngành (Khoa học tự nhiên, Văn học - Nghệ thuật, Điện tử Viễn thông, Công nghệ thông tin): ")
        year_public = int(input("Nhập năm xuất bản: "))
        book = Book(book_title, author, major, year_public)

        list_book.append(book)

    return list_book

def input_list_reader():
    list_reader = []
    quantity_reader = int(input("Nhập số lượng bạn đọc: "))

    for _ in range(quantity_reader):
        name_reader = input("Nhập họ tên bạn đọc: ")
        address = input("Nhập địa chỉ: ")
        sdt = input("Nhập số điện thoại: ")
        type_reader = input("Nhập loại bạn đọc (Sinh viên, Học viên cao học, Giáo viên): ")
        reader = Reader(name_reader, address, sdt, type_reader)

        list_reader.append(reader)

    return list_reader


"""
import csv
from models import Book, Reader

def input_list_book(file_name):
    danh_sach_sach = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Tạo đối tượng sách từ dữ liệu CSV
                book = Book(
                    id_book=int(row['id_book']),
                    book_title=row['book_title'],
                    author=row['author'],
                    publisher=row['publisher']
                )
                danh_sach_sach.append(book)
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc file sách: {str(e)}")
    return danh_sach_sach

def input_list_reader(file_name):
    danh_sach_ban_doc = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Tạo đối tượng bạn đọc từ dữ liệu CSV
                reader_obj = Reader(
                    id_reader=int(row['id_reader']),
                    name=row['name'],
                    address=row['address']
                )
                danh_sach_ban_doc.append(reader_obj)
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc file bạn đọc: {str(e)}")
    return danh_sach_ban_doc

"""