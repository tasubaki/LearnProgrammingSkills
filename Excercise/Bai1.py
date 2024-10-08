class KiemTraDoiXung:
    def __init__(self, array) -> None:
        self.array = array

    def ktdoixung(self):
        n = len(self.array)

        for i in range(n//2):
            if self.array[i] != self.array[n-i-1]:
                return False
            
        return True
    

def nhap():
    n = int(input("Nhập số phần tử của mảng: "))
    array = list(map(int, input(f"Nhập {n} số nguyên dương, cách nhau bởi dấu cách: ").split()))
    return array






def main():
    a = nhap()

    doixung = KiemTraDoiXung(a)

    if doixung.ktdoixung():
        print("Mảng đối xứng.")
    else:
        print("Mảng không đối xứng.")


if __name__ == "__main__":
    main()
