class Laptop:
    Storage_type = "ssd"        # class Attribute

    def __init__(self, RAM, Storage):
        self.RAM = RAM                      # instance Attribute
        self.storage = Storage

    @classmethod                                # Decorators
    def get_storage_type(cls):
        print(f"The storage type is {cls.Storage_type}")

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM and {self.storage} {self.Storage_type}")

    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (discount*price / 100)
        print(f"Price of laptop after discount is {final_price}")

L1 = Laptop("16gb","256gb")

print(L1.RAM, L1.storage)
L1.get_info()
L1.get_storage_type()
L1.calc_discount(40_000, 10)