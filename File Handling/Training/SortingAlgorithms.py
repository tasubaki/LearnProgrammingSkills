class FileHandler:
    def __init__(self, file_name: str, mode = "r") -> None:
        self.file_name = file_name
        self.mode = mode
    
    def read_data(self):
        with open(self.file_name, self.mode) as file:
            lines = file.readline()
            num_arrays = int(lines[0].strip())
            arrays = [list(map(int, lines.strip().split())) for line in lines[1:num_arrays + 1]]

        return arrays
    
    def write_data(self, sorted_arrays):
        with open(self.file_name, "w") as file:
            for array in sorted_arrays:
                file.write(" ".join(map(str, array)) + "\n")


class SortingAlgorithms:
    @staticmethod
    def bubble_sort():
        pass