patients = [
    ["Ravi", 500, 1000, 3000, True],
    ["Priya", 500, 500, 2000, False],
    ["Akhil", 500, 1500, 4000, True]
]

for p in patients:
    name, consultation, diagnostic, treatment, senior = p

    total = consultation + diagnostic + treatment

    
    if senior:
        concession = total * 0.10
    else:
        concession = 0

    bill = total - concession

    # Validate billing constraints
    if min(consultation, diagnostic, treatment) < 0:
        print(name, "- Invalid bill")
        continue

    if bill > 5000:
        category = "High Payment"
    elif bill >= 2000:
        category = "Medium Payment"
    else:
        category = "Low Payment"

    print("\nPatient:", name)
    print("Total Charges: Rs.", total)
    print("Concession: Rs.", concession)
    print("Final Bill: Rs.", bill)
    print("Classification:", category)