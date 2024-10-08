class NumberArray:
    def __init__(self) -> None:
        self.array = []


    def input_array(self):
        while True:
            try:
                n = int(input("Nhap n(n <= 1000): "))

                if n<=0 or n>1000:
                    print("n trong khoang 1 den 1000.")
                    continue

                self.array = list(map(int, input(f"Nhap {n} phan tu cach nhau bang khoang trang: ").split()))

                if len(self.array) != n:
                    print(f"Nhap dung so luong {n}")
                    continue

                break

            except ValueError:
                print("Gia tri khong hop le!")

    def find_longest_road(self):
        max_length = 0
        current_length = 1
        start_index = 0
        best_index = 0

        for i in range(1, len(self.array)):
            if self.array[i] >= self.array[i-1]:
                current_length += 1
            else:
                if current_length > max_length:
                    max_length = current_length
                    best_index = start_index

                current_length = 1
                start_index = i

        if current_length > max_length:
            max_length = current_length
            best_index = start_index

        return best_index, max_length
        
    def print_result(self):
        start_index, length = self.find_longest_road()
        print(f"Đường chạy dài nhất bắt đầu từ vị trí {start_index} với độ dài {length}.")
        print("Bao gồm:", ' '.join(map(str, self.array[start_index:start_index + length])))



def main():
    longest_subseq = NumberArray()
    longest_subseq.input_array()
    longest_subseq.print_result()

if __name__ == "__main__":
    main()
