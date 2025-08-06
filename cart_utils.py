# cart_utils.py

TAX_RATE = 0.08
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1

def add_item(cart, item):
    cart.append(item)

def calculate_subtotal(cart):
    return sum(item["price"] * item["quantity"] for item in cart)

def apply_business_rules(subtotal):
    discount = subtotal * DISCOUNT_RATE if subtotal > DISCOUNT_THRESHOLD else 0
    tax = (subtotal - discount) * TAX_RATE
    total = subtotal - discount + tax
    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total
    }
