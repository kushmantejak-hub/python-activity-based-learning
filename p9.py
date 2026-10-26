expenses = [
    ["Hotel", 200, "USD"],
    ["Food", 100, "EUR"],
    ["Shopping", 150, "USD"],
    ["Transport", 5000, "INR"]
]

# Exchange rates to INR
rates = {
    "USD": 85,
    "EUR": 95,
    "INR": 1
}

budget = 40000
fee_percent = 2

total_spending = 0
category_costs = {}

print("----- TRAVEL EXPENSE REPORT -----")

for category, amount, currency in expenses:
    converted = amount * rates[currency]
    fee = converted * fee_percent / 100
    total = converted + fee

    category_costs[category] = total
    total_spending += total

    print(category, "-", currency, amount)
    print("Converted Amount: Rs.", round(converted, 2))
    print("Conversion Fee: Rs.", round(fee, 2))
    print("Total Cost: Rs.", round(total, 2))
    print()

largest = max(category_costs, key=category_costs.get)

print("---------------------------------")
print("Total Spending: Rs.", round(total_spending, 2))
print("Travel Budget: Rs.", budget)

if total_spending <= budget:
    print("Status: Within Budget")
else:
    print("Status: Budget Exceeded")

print("Largest Expense:", largest)
print("Expense Amount: Rs.", round(category_costs[largest], 2))