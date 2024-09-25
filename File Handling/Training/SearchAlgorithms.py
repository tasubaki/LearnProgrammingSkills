class FileHandler:
    def __init__(self, file_name: str, mode = "r") -> None:
        self.file_name = file_name
        self.mode = mode
    
    def read_data(self):
        """Đọc số lượng mảng và dữ liệu từ file, trả về một danh sách các mảng."""
        with open(self.file_name, self.mode) as file:
            lines = file.readlines()
            num_arrays = int(lines[0].strip())  # Dòng đầu tiên là số lượng mảng
            arrays = []
            for i in range(1, num_arrays + 1):  # Đọc các mảng từ dòng thứ 2 trở đi
                arr = list(map(int, lines[i].strip().split()))  # Chuyển đổi các số thành int
                arrays.append(arr)
        return arrays

    def write_data(self, data):
        """Ghi dữ liệu vào file."""
        with open(self.file_name, self.mode) as file:
            for item in data:
                file.write(f"{item}\n")



class SearchAlgorithms:
    def __init__(self, arrays) -> None:
        self.arrays = arrays

    def linear_search(self, value):
        results = []
        for index, arr in enumerate(self.arrays):
            for i in range(len(arr)):
                if arr[i] == value:
                    results.append(f"Value {value} found in array {index + 1} at index {i}")
                    break
            else:
                results.append(f"Value {value} not found in array {index + 1}")
        return results
    
    def binarySearch(self, arr, value):
        """Thực hiện tìm kiếm nhị phân trong mảng đã được sắp xếp."""
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == value:
                return mid
            
            if arr[mid] < value:
                left = mid + 1
            else:
                right = mid - 1

        return -1


class SortAlgorithms:
    @staticmethod
    def bubbleSort(arr):
        n = len(arr)

        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  

        return arr
    

def main():
    file_handler = FileHandler("DATASEARCH.INP")

    arrays = file_handler.read_data()

    search = SearchAlgorithms(arrays)

    value = 40
    results = search.linear_search(value)

    with open("DATASEARCH.OUT", "w") as file:
        for result in results:
            file.write(result + "\n")

    sorted_array = SortAlgorithms.bubbleSort(arrays[0])  
    print("Sorted first array:", sorted_array)

    # Thực hiện tìm kiếm nhị phân trên mảng đã sắp xếp
    binary_result = search.binarySearch(sorted_array, value)
    if binary_result != -1:
        print("Binary search: Value", value, "found at index", binary_result)
    else:
        print("Binary search: Target not found in array.")


if __name__ == "__main__":
    main()
