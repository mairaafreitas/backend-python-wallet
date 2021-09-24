def calculate_total(products):
    total_products = 0
    for product in products:
        value_data = product['value']
        qty_data = product['qty']
        total_products += value_data * qty_data
    return total_products
