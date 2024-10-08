class NumberArray:
    def __init__(self) -> None:
        self.array = []

    def linear_congruential_generator(self, seed, a=1664525, c=1013904223, m=2**32):
        return (a*seed+c) % m
    
    def create_random_array(self, n, lower_bound, upper_bound, seed=1):
        for _ in range(n):
            seed = self.linear_congruential_generator(seed)
            random_number = lower_bound + (seed % (upper_bound-lower_bound+1))
            self.array.append(random_number)

    
    def selection_sort(self):
        for i in range(len(self.array)):
            min_idx = i 
            
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j

            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]

        return self.array
    

class UniqueArray:
    def __init__(self, number_array) -> None:
        self.number_array = number_array

    def remove_duplicates(self):
        self.number_array = sorted(list(set(self.number_array)))

    def __str__(self):
        return f"Mảng sau khi loại bỏ trùng lặp: {self.number_array}"

class ArrayPrinter:
    @staticmethod
    def print_array(message, array):
        print(f"{message}: {array}")


def main():
    number_array = NumberArray()

    # Tạo mảng ngẫu nhiên
    number_array.create_random_array(18, 1, 20, seed=5)
    ArrayPrinter.print_array("Mảng ngẫu nhiên", number_array.array)

    # Sắp xếp mảng tăng dần
    number_array.selection_sort()
    ArrayPrinter.print_array("Mảng sau khi sắp xếp tăng dần", number_array.array)

    # Loại bỏ phần tử trùng lặp
    unique_array = UniqueArray(number_array.array)
    unique_array.remove_duplicates()
    ArrayPrinter.print_array("Mảng không trùng lặp:", unique_array.number_array)
    #print(unique_array)


if __name__ == "__main__":
    main()