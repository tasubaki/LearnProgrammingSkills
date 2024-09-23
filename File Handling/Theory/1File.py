# Working with files in Python is the open() function.
class FileHandler:
    def __init__(self, file_name, mode='r'):
        self.file_name = file_name
        self.mode = mode
        #self.file = None

    # Open and read file contents.    
    def read_content(self):
        """ if self.file:
            try:
                content = self.file.read()
                print("File Content: ")
                print(content)
            except Exception as e:
                print(f"Error reading file: {e}")
        else:
            print("file not opened") """
        
        # Use with to ensure the file is always closed properly, instead of having to use try: except: and finally to close it manually.
        with open(self.file_name, self.mode) as file:
            content = file.read()

            print("File Content:")
            print(content)
    
    # Open and write data to file
    def write_content(self, content):
        with open(self.file_name, self.mode) as file:
            file.write(content)

            print(f"Successfully wrote to file '{self.file_name}'.")

            
def main():
    # Write content to file
    file_handler = FileHandler("demofile.txt", "w")
    file_handler.write_content("This is a sample text using class and main function.\n")

    file_handler = FileHandler("example.txt", "w")
    file_handler.write_content("Hello! Welcome to example.txt \nThis file is for testing purposes.\nGood Luck!")


    # Read file
    file_handler = FileHandler("example.txt")
    file_handler.read_content()


if __name__ == '__main__':
    main()
