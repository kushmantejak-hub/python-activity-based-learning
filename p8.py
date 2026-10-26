products = [
    ["Table", 10, 500, 200, 5, 100, 1000],
    ["Chair", 20, 200, 100, 10, 50, 500],
    ["Desk", 5, 800, 300, 8, 150, 1500]
]

target_profit = 20  # 20% profit target

for p in products:
    name, qty, material, labour, wastage, machine, price = p

    material_cost = qty * material
    labour_cost = qty * labour
    wastage_cost = material_cost * wastage / 100
    machine_cost = qty * machine

    total_cost = material_cost + labour_cost + wastage_cost + machine_cost
    total_sales = qty * price
    profit = total_sales - total_cost
    profit_percent = (profit / total_cost) * 100

    print("\n--- Manufacturing Report ---")
    print("Product:", name)
    print("Material Cost: Rs.", material_cost)
    print("Labour Cost: Rs.", labour_cost)
    print("Wastage Cost: Rs.", round(wastage_cost, 2))
    print("Machine Cost: Rs.", machine_cost)
    print("Total Cost: Rs.", round(total_cost, 2))
    print("Selling Amount: Rs.", total_sales)
    print("Profit: Rs.", round(profit, 2))
    print("Profit Percentage:", round(profit_percent, 2), "%")

    if profit_percent >= target_profit:
        print("Status: Profit Target Achieved")
    else:
        print("Status: Profit Target Not Achieved")