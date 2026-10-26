employees = [
    ["Ravi", 20000, 5000, 2000, 3000],
    ["Priya", 30000, 7000, 3000, 5000],
    ["Akhil", 40000, 10000, 4000, 6000]
]

for e in employees:
    name, basic, allowance, overtime, incentive = e

    gross = basic + allowance + overtime + incentive

    # Progressive deductions
    if gross <= 25000:
        deduction = gross * 0.05
    elif gross <= 40000:
        deduction = 25000 * 0.05 + (gross - 25000) * 0.10
    else:
        deduction = 25000 * 0.05 + 15000 * 0.10 + (gross - 40000) * 0.15

    net_salary = gross - deduction

    print("\n------ SALARY STATEMENT ------")
    print("Employee Name :", name)
    print("Basic Pay     : Rs.", basic)
    print("Allowances    : Rs.", allowance)
    print("Overtime      : Rs.", overtime)
    print("Incentives    : Rs.", incentive)
    print("Gross Salary  : Rs.", gross)
    print("Deduction     : Rs.", round(deduction, 2))
    print("Net Salary    : Rs.", round(net_salary, 2))
    print("-----------------------------")