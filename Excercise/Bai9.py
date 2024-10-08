class NumberArray:
    def __init__(self) -> None:
        self.array = []
        self.X = None

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

        while True:
            try:
                self.X = float(input("Nhap gia tri X: "))
                break
            except ValueError:
                print("Nhap 1 so thuc!")

    def insert_value(self):
        position = self.find_insert_position(self.X)
        self.array.insert(position, self.X)

    def find_insert_position(self, x):
        for index, value in enumerate(self.array):
            if value >= x:
                return index
            
        return len(self.array)
    
    def __str__(self) -> str:
        return ' '.join(map(str, self.array))


def main():
    number_array = NumberArray()
    number_array.input_array()

    number_array.insert_value()

    print(f"Mang sau khi chen gia tri {number_array.X} : {number_array.array}")

if __name__ == "__main__":
    main()