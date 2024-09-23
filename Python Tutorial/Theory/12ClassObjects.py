class Item():
    def __init__(self, name: str, price: float, quantity = 0) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

        # Assign the data type section
        assert price>=0
        assert quantity>=0

    # The string representation of an object WITH the __str__() function:
    def __str__(self) -> str:       
        return f"name is {self.name}, price = {self.price} and quantity = {self.quantity}" 

    def print_method(self):
        print(f"Hello my item name is {self.name}")

    # Using "pass"
    def change(self):
        pass

    def sum_price(self):
        return self.price * self.quantity

    # Static method
    @staticmethod
    def check_price(prices):
        if prices<=500:
            return "Cheap"
        else:
            return "Expensive"


def main():
    item1 = Item("Phone", 1000, 3)
    item2 = Item("Pot", 100, 30)

    print(item1)    # Result: name is Phone, price = 1000 and quantity = 3
    item1.print_method()    # Result: Hello my item is Phone
    print(f"This is name item2 {item2.name}")   # Result: This is name item2 Pot


    # Modify Object Properties
    item2.price = 1

    print(item2.price)  # Result: 1


    # Delete Object Properties or Object
    del item2.quantity
    del item2

    # Static
    item3 = Item("Glove","10000",2) # After assigning this line style will error
    
    print(item1.check_price(1000))
    print(Item.check_price(100))

    print(item3.sum_price())    # Result: 1000010000. 
    # Means the string is printed twice so we need to assign the data type to correct the problem.
    
if __name__ == '__main__':
    main()