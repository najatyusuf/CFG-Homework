# Homework Week 1
# Task 1

class CashRegister:

    discount = 0.9
    total_price = 0

    def __init__(self):
        self.total_items = []  # {'item': 'price'}

    def add_item(self, item_name, item_price, quantity):
        for i in list(range(quantity)):
            self.total_items.append({'item': item_name, 'price': item_price})

    def remove_item(self, item):
        item_list = self.total_items

        for i in item_list:
            if i['item'] == item:
                item_list.remove(i)

    def get_total(self):

        item_list = self.total_items
        list_price = [i['price'] for i in item_list]
        total_price = self.total_price

        for price in list_price:
            total_price += price

        round_tot = round(total_price, 2)

        return 'Total price before discount: £{}'.format(round_tot)

    def apply_discount(self):

        item_list = self.total_items
        list_price = [i['price'] for i in item_list]
        total_price = self.total_price

        for price in list_price:
            total_price += price

        discounted_total = total_price * self.discount
        discounted_tot = round(discounted_total, 2)

        return 'Discount applied, the total price is now: £{}'.format(discounted_tot)

    def show_items(self):
        return 'Shopping cart: ' + str(self.total_items)

    def reset_register(self):
        self.total_items.clear()
        self.total_price = 0
        self.discount = 0
        return 'Total items: {}\nTotal price: £{}'.format(self.total_items, self.total_price)


shop = CashRegister()

# Example 1, adding items (2 croissants, 1 water and 1 coffee)
print('Adding items: ')
shop.add_item('Croissant', 1.20, 2)
shop.add_item('Coffee', 2.50, 1)
shop.add_item('Water', 0.90, 1)
print(shop.show_items())

# Example 2, getting total
print('\nGetting the total: ')
print(shop.show_items())
print(shop.get_total())

# Example 3, applying discount of 10%
print('\nApplying the discount: ')
print(shop.show_items())
print(shop.get_total())
print(shop.apply_discount())

# # Example 4, removing items (Removing the water)
print('\nRemoving item: ')
shop.remove_item('Water')
print(shop.show_items())

# Example 5, resetting the register
print('\nResetting the register: ')
print(shop.reset_register())
