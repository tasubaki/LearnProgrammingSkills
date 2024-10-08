class XapXep:
    def __init__(self) -> None:
        self.array = []

    
    def input_array(self):
        while True:
            try:
                n = int(input("Nhập số phần tử của mảng: "))
                if n <= 0:
                    print("Số phần tử phải là số nguyên dương. Vui lòng nhập lại!")
                    continue  # Yêu cầu nhập lại

                # Nhập từng phần tử và kiểm tra
                self.array = []
                for i in range(n):
                    while True:
                        try:
                            element = int(input(f"Nhập phần tử thứ {i+1}: "))
                            self.array.append(element)
                            break  # Thoát khỏi vòng lặp khi nhập hợp lệ
                        except ValueError:
                            print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số nguyên!")

                break  # Thoát vòng lặp chính khi mảng đã được nhập đúng
            except ValueError:
                print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số nguyên!")


    def sort_array(self):
        self.array.sort()


    # Hàm in mảng
    def print_array(self):
        print("Mảng sau khi sắp xếp: ", self.array)

def main():
    mang_sap_xep = XapXep()
    mang_sap_xep.input_array()
    mang_sap_xep.sort_array()
    mang_sap_xep.print_array()


if __name__ == "__main__":
    main()