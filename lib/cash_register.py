#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0.0  

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity  
        for _ in range(quantity):
            self.items.append(title)
        return self.total

    def apply_discount(self):
        if self.total > 0:
            discount_amount = self.total * self.discount / 100
            rounded_discount = round(discount_amount)
            self.total -= rounded_discount
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.last_transaction  #
            self.total -= last_item_price
            self.last_transaction = 0.0  
        else:
            print("No items to void.")
    
    def reset_register_totals(self):
        self.total = 0
        self.items = []
        self.last_transaction = 0.0  


erick = CashRegister(20)
erick.add_item("macbook air", 1000)
erick.apply_discount()

# Add another item
erick.add_item("iphone", 800)

# Void the last transaction
erick.void_last_transaction()

# Reset the register totals
erick.reset_register_totals()

print(f"Total after resetting the register: ${erick.total}")