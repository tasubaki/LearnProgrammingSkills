class NumberCounter:
    def __init__(self):
        self.array = []
        self.counts = {}

    # Hàm nhập mảng
    def input_array(self):
        while True:
            try:
                n = int(input("Nhập số phần tử của mảng: "))
                if n <= 0:
                    print("Số phần tử phải là số nguyên dương. Vui lòng nhập lại!")
                    continue

                self.array = []
                for i in range(n):
                    while True:
                        try:
                            element = int(input(f"Nhập phần tử thứ {i + 1}: "))
                            self.array.append(element)
                            break  # Thoát vòng lặp khi nhập hợp lệ
                        except ValueError:
                            print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số nguyên!")
                break  # Thoát vòng lặp chính khi mảng đã được nhập đúng
            except ValueError:
                print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số nguyên!")

    # Hàm đếm số lần xuất hiện của từng phần tử
    def count_occurrences(self):
        for number in self.array:
            if number in self.counts:
                self.counts[number] += 1
            else:
                self.counts[number] = 1

    # Hàm tìm phần tử xuất hiện nhiều nhất
    def find_most_frequent(self):
        if not self.counts:
            return None
        
        most_frequent = None
        max_count = 0

        for number, count in self.counts.items():
            if count > max_count:
                max_count = count
                most_frequent = number

        return most_frequent, max_count

    # Hàm in kết quả
    def print_result(self):
        most_frequent, count = self.find_most_frequent()
        if most_frequent is not None:
            print(f"Phần tử xuất hiện nhiều nhất là: {most_frequent} với {count} lần xuất hiện.")
        else:
            print("Không có phần tử nào trong mảng.")


def main():
    counter = NumberCounter()
    counter.input_array()
    counter.count_occurrences()
    counter.print_result()


if __name__ == "__main__":
    main()

