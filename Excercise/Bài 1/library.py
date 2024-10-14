import csv
import os
from book import Book
from reader import Reader


class BookManagement:
    def __init__(self) -> None:
        self.book_loan_list = []
    
    def loan_book(self, reader, book, quantity, status):
        # Kiểm tra xem đã có bản ghi cho bạn đọc này và sách này chưa
        for loan in self.book_loan_list:
            if loan['reader'].id_reader == reader.id_reader and loan['book'].id_book == book.id_book:
                print(f"Bạn đọc {reader.name} đã mượn sách '{book.book_title}' trước đó.")
                return
            
        self.book_loan_list.append({
            'reader': reader,
            'book': book,
            'quantity': quantity,
            'status': status
        })

        print(f"Bạn đọc {reader.name} đã mượn {quantity} cuốn sách '{book.book_title}' với tình trạng: {status}.")
        
    def print_list(self):
        print("Danh sách mượn sách:")
        for loan in self.book_loan_list:
            print(f"Bạn đọc: {loan['reader'].name}, Sách: {loan['book'].book_title}, Số lượng: {loan['quantity']}, Tình trạng: {loan['status']}")
            
    def sort_name_reader(self):
        self.book_loan_list.sort(key=lambda x: x['reader'].name)
        print("Đã sắp xếp theo tên bạn đọc.")   

    def sort_quantity_book(self):
        self.book_loan_list.sort(key=lambda x: x['quantity'], reverse=True)
        print("Đã sắp xếp theo số lượng sách (giảm dần).")

    def search_name_reader(self, name_reader):
        results = [loan for loan in self.book_loan_list if loan['reader'].name.lower()==name_reader.lower()]

        if results:
            for loan in results:
                print(f"Bạn đọc: {loan['reader'].name}, Sách: {loan['book'].book_title}, Số lượng: {loan['quantity']}, Tình trạng: {loan['status']}")
            else:
                print(f"Không tìm thấy bạn đọc tên '{name_reader}'.")

    def write_file(self, file_name):
        try:
            file_is_empty = not os.path.exists(file_name) or os.stat(file_name).st_size == 0

            with open(file_name, 'a', newline='', encoding='utf-8') as file:
                writers = csv.writer(file)

                if file_is_empty:
                    writers.writerow(['Mã bạn đọc', 'Họ tên', 'Mã sách', 'Tên sách', 'Số lượng','Tình trạng'])

                for loan in self.book_loan_list:
                        writers.writerow([
                            loan['reader'].id_reader,
                            loan['reader'].name,
                            loan['book'].id_book,
                            loan['book'].book_title,
                            loan['quantity'],
                            loan['status']
                        ])
            print(f"Đã ghi danh sách mượn sách vào file CSV: {file_name}.")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi ghi file CSV: {str(e)}")

    def read_file(self, file_name):
        try:
            with open(file_name, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Bỏ qua dòng tiêu đề

                for row in reader:
                    id_readers, names, id_books, book_titles, quantitys, statuss = row

                    readers = Reader(names, "", "", "")
                    readers.id_reader = id_readers

                    books = Book(book_titles, "", "", "")
                    books.id_book = id_books

                    self.book_loan_list.append({
                        'reader': readers,
                        'book': books,
                        'quantity': int(quantitys),
                        'status': statuss
                    })
            print(f"Đã đọc dữ liệu từ file CSV: {file_name}.")

        except Exception as e:
            print(f"Đã xảy ra lỗi khi đọc file CSV: {str(e)}")


