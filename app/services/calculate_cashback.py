from decimal import Decimal


def calculate_cashback(total: Decimal) -> Decimal:
    cashback_value = total * Decimal('0.1')
    return round(cashback_value, 2)
