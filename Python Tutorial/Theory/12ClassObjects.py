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

#instantiate the class "Phone" as a child class with the parent class "Item".
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, type_phone="4G") -> None:
        super().__init__(name, price, quantity)
        self.type_phone = type_phone


# Encapsulation Topic
class Bank():
    def __init__(self, name: str, id_card: int) -> None:
        self.name = name
        self.id_card = id_card

class Staff(Bank):
    def __init__(self, name: str, id_card: int) -> None:
        super().__init__(name, id_card)
        #self.salary = 5000  # Public type
        self.__salary = 5000  # Private type

    # Admin change salary
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        self.__salary = new_salary


# Polymorphism topic
class ForeignStudents():
    def __init__(self, name, id, contry) -> None:
        self.name = name
        self.id = id
        self.contry = contry

    def hello(self):
        print("Hello")

class VietStudents():
    def __init__(self, name, id, contry) -> None:
        self.name = name
        self.id = id
        self.contry = contry

    def hello(self):
        print("Chào")

# Use generic functions to apply polymorphic 
def hello_common(ForeignStudents):
    ForeignStudents.hello()


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
    #item3 = Item("Glove","10000",2) # After assigning this line style will error
    
    print(item1.check_price(1000))
    print(Item.check_price(100))

    #print(item3.sum_price())    # Result: 1000010000. 
    # Means the string is printed twice so we need to assign the data type to correct the problem.


    # Inheritance topic
    phone1 = Phone("Samsung note 20", 18000, 8, "5G")
    phone2 = Phone("Samsung note 22", 18000, 4)

    print(f"{phone1.name} has price {phone1.price}.")
    print(f"{phone2.name} is {phone2.type_phone} type phone.")


    # Encapsulation Topic
    staff1 = Staff("Nam",13245645)
    staff2 = Staff("Chung", 9876543)

    """ staff2.salary = 100000      # Result: 100000
    
    print(staff2.salary)
    print(dir(staff2))
Result:
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'id_card', 'name', 'salary']

    """    
    print(dir(staff1))
    """
    Result:
    ['_Staff__salary', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
    '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'id_card', 'name']
    """
    staff2.set_salary(1000000000000)
    print(f"{staff2.name} new salary is {staff2.get_salary()}")


    # Polymorphism topic
    student1 = ForeignStudents("Jack", 123456, "UK")
    student2 = VietStudents("Hoa", 123456, "Việt Nam")

    # Normally will point to the method of each class
    student1.hello()    # Result: Hello
    student2.hello()    # Result: Chào

    # After applying polymorphism
    hello_common(student1)  # Result: Hello
    hello_common(student2)  # Result: Chào


if __name__ == '__main__':
    main()