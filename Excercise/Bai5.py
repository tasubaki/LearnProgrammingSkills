import math

class Search:
    def __init__(self) -> None:
        self.array = []
        self.X = None

    # Hàm nhập mảng và số X
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

        # Nhập giá trị X
        while True:
            try:
                self.X = int(input("Nhập giá trị X: "))
                break
            except ValueError:
                print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số nguyên!")

    @staticmethod
    def is_prime(number):
        if number < 2:
            return False
        
        for i in range(2, int(math.sqrt(number)) + 1):
            if number%i==0:
                return False
        
        return True
    

    def find_closest_prime(self):
        closest_prime = None
        min_distance = float('inf')
        closest_index = -1

        for index, number in enumerate(self.array):
            if self.is_prime(number):
                distance = abs(number - self.X)
                
                if distance < min_distance:
                    min_distance = distance
                    closest_prime = number
                    closest_index = index

        return closest_prime, closest_index
    
    def print_result(self):
        closest_prime, closest_index = self.find_closest_prime()

        if closest_prime is not None:
            print(f"Số nguyên tố gần với {self.X} nhất là {closest_prime} tại vị trí {closest_index}.")
        else:
            print(f"Không có số nguyên tố nào trong mảng.")


if __name__ == "__main__":
    prime_finder = Search()
    prime_finder.input_array()
    prime_finder.print_result()