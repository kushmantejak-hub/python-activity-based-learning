# Campus Event Financial Planning

venue = 10000
equipment = 5000
catering_per_person = 200
transport = 3000
certificate_per_person = 50

sponsorship = 10000
registration_fee = 300
participants = 100

# Calculate fixed costs
fixed_cost = venue + equipment + transport

# Calculate variable costs
variable_cost = participants * (catering_per_person + certificate_per_person)

total_cost = fixed_cost + variable_cost
registration_income = participants * registration_fee
total_income = registration_income + sponsorship

# Sponsorship shortfall
shortfall = max(0, total_cost - sponsorship)

# Minimum registrations to break even
contribution_per_person = registration_fee - catering_per_person - certificate_per_person

if contribution_per_person > 0:
    minimum_registrations = max(
        0, (fixed_cost - sponsorship + contribution_per_person - 1)
        // contribution_per_person
    )
else:
    minimum_registrations = "Not possible with this registration fee"

print("----- CAMPUS EVENT BUDGET -----")
print("Venue Cost: Rs.", venue)
print("Equipment Cost: Rs.", equipment)
print("Transport Cost: Rs.", transport)
print("Catering Cost: Rs.", participants * catering_per_person)
print("Certificate Cost: Rs.", participants * certificate_per_person)
print("Total Cost: Rs.", total_cost)
print("Registration Income: Rs.", registration_income)
print("Sponsorship: Rs.", sponsorship)
print("Total Income: Rs.", total_income)
print("Sponsorship Shortfall: Rs.", shortfall)
print("Minimum Registrations to Break Even:", minimum_registrations)

if total_income >= total_cost:
    print("Status: Event is Profitable")
else:
    print("Status: Event is Running at a Loss")