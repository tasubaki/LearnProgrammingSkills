class NumberArray:
    def __init__(self) -> None:
        self.array = []

    def linear_congruential_generator(self, seed, a=1664525, c=1013904223, m=2**32):
        return (a * seed + c) % m
    
    # Tạo mảng ngẫu nhiên dựa vào LCG
    def create_random_array(self, n, lower_bound, upper_bound, seed=1):
        for _ in range(n):
            seed = self.linear_congruential_generator(seed)  # Tạo số ngẫu nhiên mới
            random_number = lower_bound + (seed % (upper_bound - lower_bound + 1))  # Giới hạn số ngẫu nhiên trong khoảng
            self.array.append(random_number)  # Thêm số vào mảng


    def __str__(self) -> str:
        return f"Mảng ban đầu: {self.array}"
    

class UniqueNumbers:
    def __init__(self, number_array) -> None:
        self.number_array = number_array

    """ def print_unique_numbers(self):
        unique_numbers = set(self.number_array)

        print(f"Các số khác nhau trong mảng: {sorted(unique_numbers)}") """
    
    def print_unique_numbers(self):
        # Đếm số lần xuất hiện của từng phần tử
        counts = {}
        for number in self.number_array:
            if number in counts:
                counts[number] += 1
            else:
                counts[number] = 1

        # In ra các số chỉ xuất hiện một lần
        unique_numbers = [num for num, count in counts.items() if count == 1]
        
        print(f"Các số khác nhau trong mảng (không trùng lặp): {sorted(unique_numbers)}")



def main(): 
    number_array = NumberArray()

    number_array.create_random_array(15, 1, 19, seed=5)  

    print(number_array)

    arrays = UniqueNumbers(number_array.array)

    arrays.print_unique_numbers()

if __name__ == "__main__":
    main()