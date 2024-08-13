import os
os.system("cls")
os.system("color 2")

class Market:
    def Bozor(self, products: dict, balans: float, name: str, address: str):
        self.products = products
        self.balans = balans
        self.name = name
        self.address = address
    def get_products_info(self):
        print(f"""
PRODUCTS            {self.products}
BALANS              {self.balans}
NAME                {self.name}
ADDRESS             {self.address}
""")
    def __init__(self, name: str, address: str) -> None:
        pass
    def get_products_info(self) -> str:
        pass
    def add_product(self, product: str, price: float, quantity: int) -> None:
        pass
    def remove_product(self, product: str) -> None:
        pass
    def add_money(self, amount: float):
        pass
    def sell(self, product: str, quantity: int) -> None:
        pass
    
        

Bozor = Market(name="Supermarket", address="Toshkent, O'zbekiston")
Bozor.add_product(product="Olma", price=5000, quantity=10)
Bozor.add_product(product="Banan", price=7000, quantity=5)
Bozor.get_products_info()
Bozor.sell(product="Olma", quantity=3)
Bozor.get_products_info()
Bozor.remove_product(product="Banan")
Bozor.get_products_info()

