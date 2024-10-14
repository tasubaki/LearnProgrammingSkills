class Reader():
    _id_reader = 10000

    def __init__(self, name, address, sdt, type_reader) -> None:
        self.id_reader = Reader._id_reader
        Reader._id_reader += 1
        self.name = name
        self.address = address
        self.sdt = sdt
        self.type_reader = type_reader

    def __str__(self) -> str:
        return f"Mã bạn đọc: {self.id_reader}, Họ tên: {self.name}, Địa chỉ: {self.address}, SDT: {self.sdt}, Loại bạn đọc: {self.type_reader}"
    
