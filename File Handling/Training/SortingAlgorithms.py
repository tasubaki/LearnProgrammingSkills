class FileHandler:
    def __init__(self, file_name: str, mode = "r") -> None:
        self.file_name = file_name
        self.mode = mode
    
    def read_data(self):
        with open(self.file_name, self.mode) as file:
            lines = file.readlines()
            num_arrays = int(lines[0].strip())
            arrays = [list(map(int, line.strip().split())) for line in lines[1:num_arrays + 1]]

        return arrays
    
    def write_data(self, sorted_arrays):
        with open(self.file_name, "w") as file:
            for array in sorted_arrays:
                file.write(" ".join(map(str, array)) + "\n")


class SortingAlgorithms:
    @staticmethod
    def bubble_sort(array):
        n = len(array)

        for i in range(n-1):
            swapped = False
            for j in range(n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]

                    swapped = True

            if not swapped:
                break

        return array
    
    @staticmethod
    def selection_sort(array):
        for i in range(len(array)):
            min_index = i

            for j in range(i+1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j

            array[i], array[min_index] = array[min_index], array[i]

        return array
    
    @staticmethod
    def partition(array, low, high):
        pilot = array[high]
        i = low -1

        for j in range(low, high):
            if array[j] <= pilot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i+1], array[high] = array[high], array[i+1]

        return i+1



def main():
    file_data = FileHandler("DATASORTING.INP", "r")

    arrays = file_data.read_data()
    print("Mảng trước khi sắp xếp:", arrays)  # Thử in ra các mảng đã đọc để kiểm tra
    
    sorted_arrays = [SortingAlgorithms.bubble_sort(arr) for arr in arrays]

    file_data = FileHandler("DATASORTING.OUT", "w")
    file_data.write_data(sorted_arrays)


if __name__ == "__main__":
    main()
