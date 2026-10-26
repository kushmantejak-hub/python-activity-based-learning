products = [
    ["Shirt", 1000, 2, "Clothing"],
    ["Headphones", 2000, 1, "Electronics"],
    ["Shoes", 1500, 1, "Footwear"]
]

subtotal = 0
tax_total = 0

print("========== RETAIL INVOICE ==========")

for p in products:
    name, price, qty, category = p

    amount = price * qty

    # Category-specific tax
    if category == "Clothing":
        tax_rate = 5
    elif category == "Electronics":
        tax_rate = 18
    else:
        tax_rate = 12

    tax = amount * tax_rate / 100
    subtotal += amount
    tax_total += tax

    print(name, "Qty:", qty, "Amount: Rs.", amount,
          "Tax:", tax_rate, "% =", round(tax, 2))

# Threshold discount
if subtotal >= 5000:
    discount = subtotal * 0.10
elif subtotal >= 3000:
    discount = subtotal * 0.05
else:
    discount = 0

# Maximum concession limit
discount = min(discount, 500)

final_amount = subtotal + tax_total - discount

print("------------------------------------")
print("Subtotal       : Rs.", subtotal)
print("Total Tax      : Rs.", round(tax_total, 2))
print("Discount       : Rs.", round(discount, 2))
print("Final Bill     : Rs.", round(final_amount, 2))
print("====================================")