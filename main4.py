import inventory

store = inventory.Inventory()

# Add products
store.add_product("Laptop", 50000, 10)
store.add_product("Phone", 20000, 15)
store.add_product("Headphones", 2000, 30)

# Show stock
store.show_stock()

# Purchase products
store.purchase_product("Laptop", 2)
store.purchase_product("Headphones", 5)

# Show updated stock and earnings
store.show_stock()
store.show_earnings()
