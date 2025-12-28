'''
Design & create an online store for Products (name, price).
Track total products being created.
Create a static method to calculate discount on each product based on a % parameter.
'''

class Store:
    count=0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        Store.count += 1

    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")

    @classmethod
    def product_count(cls):
        print(f"Total number of products are {cls.count}")

    @staticmethod
    def calc_disc(price,discount):
        final_price = price - (discount*price / 100)
        print(f"final price is {final_price}")

pen = Store("LINC",10)
pencil = Store("apsara",5)
eraser = Store("nataraj",7)

Store.product_count()