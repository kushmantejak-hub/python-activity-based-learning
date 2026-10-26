plans = [
    ["Plan A", 199, 1, 2, 28],
    ["Plan B", 299, 2, 1, 28],
    ["Plan C", 399, 3, 0, 56]
]

data_needed = 2       # GB per day
validity_needed = 28  # Days
budget = 350          # Rupees

eligible = []

for p in plans:
    name, price, daily_data, excess_rate, validity = p

    excess_data = max(0, data_needed - daily_data)
    excess_charge = excess_data * excess_rate * validity
    total_cost = price + excess_charge

    print("\nPlan:", name)
    print("Plan Price: Rs.", price)
    print("Excess Charges: Rs.", excess_charge)
    print("Total Cost: Rs.", total_cost)

    if validity >= validity_needed and total_cost <= budget:
        eligible.append([name, total_cost])

if eligible:
    eligible.sort(key=lambda x: x[1])
    print("\nMost Economical Eligible Plan:")
    print(eligible[0][0], "- Rs.", eligible[0][1])
else:
    print("\nNo plan satisfies the budget and validity constraints.")