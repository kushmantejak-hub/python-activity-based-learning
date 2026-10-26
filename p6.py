passengers = [
    ["Ravi", 30, 200, "Sleeper", False],
    ["Priya", 65, 200, "AC", False],
    ["Akhil", 10, 100, "Sleeper", True]
]

for p in passengers:
    name, age, distance, travel_class, cancel = p

    # Distance-based fare
    if distance <= 100:
        rate = 1
    elif distance <= 300:
        rate = 2
    else:
        rate = 3

    fare = distance * rate

    # Travel class charges
    if travel_class == "AC":
        fare = fare * 2

    # Age-based concession
    if age >= 60:
        fare = fare * 0.80
    elif age <= 12:
        fare = fare * 0.50

    reservation_fee = 50
    total = fare + reservation_fee

    # Cancellation penalty
    if cancel:
        penalty = total * 0.25
        refund = total - penalty
    else:
        penalty = 0
        refund = total

    print("\n--- Railway Ticket ---")
    print("Passenger:", name)
    print("Age:", age)
    print("Distance:", distance, "km")
    print("Class:", travel_class)
    print("Ticket Fare: Rs.", round(fare, 2))
    print("Reservation Fee: Rs.", reservation_fee)
    print("Total Fare: Rs.", round(total, 2))
    print("Cancellation Penalty: Rs.", round(penalty, 2))
    print("Refund Amount: Rs.", round(refund, 2))