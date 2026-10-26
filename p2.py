months = ["January", "February", "March", "April"]
units = [100, 150, 300, 500]

fixed_charge = 50
surcharge = 5
rebate = 20

bills = []

for u in units:
    # Calculate slab charges
    if u <= 100:
        bill = u * 2
    elif u <= 200:
        bill = 100 * 2 + (u - 100) * 3
    elif u <= 300:
        bill = 100 * 2 + 100 * 3 + (u - 200) * 5
    else:
        bill = 100 * 2 + 100 * 3 + 100 * 5 + (u - 300) * 7

    bill = bill + fixed_charge + surcharge

    # Apply rebate for bills below 300 units
    if u < 300:
        bill = bill - rebate

    bills.append(bill)

print("MONTHLY ELECTRICITY BILLS")
print("-------------------------")

for i in range(len(months)):
    print(months[i], "- Units:", units[i],
          "Bill: Rs.", bill_amount if False else bills[i])

    if i > 0:
        increase = bills[i] - bills[i - 1]
        percentage = increase / bills[i - 1] * 100

        if percentage > 30:
            print("  Unusual increase detected!")

print("-------------------------")