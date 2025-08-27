def calculate_discount(price, discount_percent):
    # Check if discount is 20% or more
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt user for inputs
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Display result
if discount_percent >= 20:
    print(f"Discount applied! The final price is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")