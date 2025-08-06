# main.py

from cart_utils import add_item, calculate_subtotal, apply_business_rules

def main():
    cart = []

    # Step 1: Add items
    add_item(cart, {"name": "Phone", "price": 499, "quantity": 1})
    add_item(cart, {"name": "Charger", "price": 25, "quantity": 2})

    # Step 2: Calculate subtotal
    subtotal = calculate_subtotal(cart)

    # Step 3: Apply business rules
    result = apply_business_rules(subtotal)

    # Step 4: Print invoice
    print("--- Invoice Summary ---")
    print(f"Subtotal: ${result['subtotal']:.2f}")
    print(f"Discount: ${result['discount']:.2f}")
    print(f"Tax: ${result['tax']:.2f}")
    print(f"Total: ${result['total']:.2f}")

# Run the main function
if __name__ == "__main__":
    main()
