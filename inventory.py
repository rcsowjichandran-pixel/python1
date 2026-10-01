class Product:
    def __init__(self, name, price, quantity):
        self.__name = name          # Encapsulation (private attributes)
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def purchase(self, qty):
        if qty <= self.__quantity:
            self.__quantity -= qty
            return self.__price * qty
        else:
            print("Not enough stock!")
            return 0

    def __str__(self):
        return f"{self.__name} - Price: {self.__price}, Stock: {self.__quantity}"


class Inventory:
    def __init__(self):
        self.__products = []        # Encapsulation
        self.__earnings = 0

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.__products.append(product)

    def show_stock(self):
        print("\n--- Available Stock ---")
        for p in self.__products:
            print(p)

    def purchase_product(self, product_name, qty):
        for p in self.__products:
            if p.get_name() == product_name:
                cost = p.purchase(qty)   # Method overriding → updates stock
                self.__earnings += cost
                if cost > 0:
                    print(f"Purchased {qty} {product_name}(s) for {cost}")
                return
        print("Product not found!")

    def show_earnings(self):
        print(f"\nTotal Earnings: {self.__earnings}")
