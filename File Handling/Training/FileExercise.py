"""
Viết chương trình tính tổng : S= 1 + 1/(2)^2 + ... + 1/n^2

- Dữ liệu đầu vào từ file TONG.INP
- Dòng đầu tiên ghi số tự nhiên n
(Nâng cấp 1: tính nhiều giá trị n
 Nâng cấp 2: kiểm tra nếu người dùng muốn nhập giá trị mới thì cho nhập, không thì dùng giá trị cũ đã có sẵn)
- kết quả ra file TONG.OUT dùng dấu , để ngăn cách phần nguyên và phần thập phân
"""

class SumCalculator:
    def __init__(self, file_name: str, mode = "r") -> None:
        self.file_name = file_name
        self.mode = mode
    
    def open_file(self):
        return open(self.file_name, self.mode)

    def input_data(self):
        quantity = int(input("Enter quantity to calculate: "))

        with self.open_file() as file:
            for number in range(quantity):
                n = int(input("Enter value n: "))

                file.write(f"{n}\n")

        print(f"Wrote {quantity} values to {self.file_name} file.")

    """Read multiple n values ​​from input file"""
    def read_inputs(self) -> list:
        with self.open_file() as file:
            numbers = [int(line.strip()) for line in file.readlines()]

        return numbers

    """Calculate the sum S according to the given formula for each n"""
    def calculate_sum(self, n: int) -> float:
        total_sum = 0

        for i in range(1, n + 1):
            total_sum += 1 / (i ** 2)
        return total_sum
        
    def write_outputs(self, results: list) -> None:
        with self.open_file() as file:
            for result in results:
                change = str(round(result, 3))
                change = change.replace(".", ",")

                file.write(f"{change} ")

        print(f"Successfully wrote output data to {self.file_name} file.")

    """Check if the user wants to enter new or use old data"""
    def check_input_method(self):
        choice = input("Do you want to enter a new value? (y/n): ").strip().lower()
        
        if choice == 'y' or choice == 'Y':
            self.input_data()
        else:
            print("Use old data in file.")


def main():
    """ # Bước 1: Người dùng nhập nhiều giá trị và ghi vào file TONG.INP
    calculator = SumCalculator("TONG.INP", "w")
    calculator.input_data()

    # Bước 2: Đọc file TONG.INP để lấy nhiều giá trị n
    calculator = SumCalculator("TONG.INP", "r")
    numbers = calculator.read_inputs() """

    # Khởi tạo đối tượng để thao tác r,w với file TONG.INP
    calculator = SumCalculator("TONG.INP", "r+")

    # Kiểm tra nếu người dùng muốn nhập dữ liệu mới hoặc sử dụng dữ liệu cũ
    calculator.check_input_method()

    # Đọc các giá trị n từ file TONG.INP
    numbers = calculator.read_inputs()

    # Bước 3: Tính toán kết quả cho từng giá trị n
    results = [calculator.calculate_sum(n) for n in numbers]

    # Bước 4: Ghi kết quả ra file TONG.OUT
    calculator = SumCalculator("TONG.OUT", "w")
    calculator.write_outputs(results)

if __name__ == "__main__":
    main()
    