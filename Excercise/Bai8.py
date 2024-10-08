class NumberArray:
    def __init__(self) -> None:
        self.array = []

    def input_array(self):
        while True:
            try:
                n = int(input("Nhap n: "))

                if n<=0:
                    print("Nhap so nguyen lon hon 0: ")
                    continue

                self.array = []

                for i in range(n):
                    while True:
                        try:
                            element = int(input(f"Nhap phan tu thu {i+1}: "))
                            self.array.append(element)
                            break
                        except ValueError:
                            print("Gia tri khong hop le!")

                break

            except ValueError:
                print("Gia tri khong hop le!")

    # Phương thức chèn mảng khác vào vị trí p
    def insert_array(self, other_array, position):
        self.array = self.array[:position] + other_array + self.array[position:]

    # Phương thức in ra mảng dưới dạng chuỗi
    def __str__(self) -> str:
        return ' '.join(map(str, self.array))


class ArrayManager:
    def __init__(self):
        self.array_a = NumberArray()
        self.array_b = NumberArray()

    # Phương thức kiểm tra vị trí chèn
    def validate_position(self):
        while True:
            try:
                p = int(input(f"Nhap vi tri chen (0 ≤ p ≤ {len(self.array_a.array)}): "))
                if 0 <= p <= len(self.array_a.array):
                    return p
                else:
                    print(f"Nhap vi tri tu 0 den {len(self.array_a.array)}.")
            except ValueError:
                print("Gia tri khong hop le!")

    # Phương thức thực hiện chèn mảng b vào a
    def insert_array_b_into_a(self, p):
        if 0 <= p <= len(self.array_a.array):
            self.array_a.insert_array(self.array_b.array, p)
        else:
            print("Vi tri khong hop le!")

    def print_result(self):
        print(f"Mang sau khi chen: {self.array_a}")


def main():
    array_manager = ArrayManager()

    # Nhập mảng a và b
    print("Mang a:")
    array_manager.array_a.input_array()

    print("Mang b:")
    array_manager.array_b.input_array()

    # Kiểm tra và lấy vị trí p
    p = array_manager.validate_position()

    # Thực hiện chèn mảng b vào a
    array_manager.insert_array_b_into_a(p)

    # In kết quả
    array_manager.print_result()

if __name__ == "__main__":
    main()