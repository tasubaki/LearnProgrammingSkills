from utils import input_list_book, input_list_reader
from library import BookManagement

def main():
    danh_sach_sach = input_list_book()
    print("\nDanh sách đầu sách đã có:")
    for sach in danh_sach_sach:
        print(sach)

    danh_sach_ban_doc = input_list_reader()
    print("\nDanh sách bạn đọc đã có:")
    for ban_doc in danh_sach_ban_doc:
        print(ban_doc)

    ql_muon_sach = BookManagement()
    ql_muon_sach.read_file("danh_sach_muon_sach.csv")
   
    for ban_doc in danh_sach_ban_doc:
        so_dau_sach_muon = int(input(f"\nNhập số đầu sách bạn đọc {ban_doc.name} muốn mượn: "))
        for _ in range(so_dau_sach_muon):
            ma_sach = int(input("Nhập mã sách bạn muốn mượn: "))
            sach_muon = next((sach for sach in danh_sach_sach if sach.id_book == ma_sach), None)
            if sach_muon:
                so_luong = int(input(f"Nhập số lượng sách '{sach_muon.book_title}' muốn mượn: "))
                tinh_trang = input("Nhập tình trạng sách: ")
                ql_muon_sach.loan_book(ban_doc, sach_muon, so_luong, tinh_trang)
            else:
                print("Mã sách không hợp lệ.")

        ql_muon_sach.print_list()

    ql_muon_sach.write_file("danh_sach_muon_sach.csv")

if __name__ == "__main__":
    main()