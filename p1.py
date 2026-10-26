students = [
    ["kushman", 90, [85, 90, 88], 95, 50000],
    ["Ravi", 90, [80, 85, 90], 90, 40000],
    ["Priya", 85, [75, 80, 85], 92, 30000],
    ["Rani", 70, [65, 70, 75], 80, 20000]
]

eligible = []

for s in students:
    name, marks, subjects, attendance, income = s

    if (marks >= 75 and min(subjects) >= 60
            and attendance >= 75 and income <= 60000):
        eligible.append(s)

# Rank by aggregate marks, attendance, and lower income
eligible.sort(key=lambda s: (-s[1], -s[3], s[4]))

print("SCHOLARSHIP ELIGIBLE STUDENTS")
print("--------------------------------")

for rank, s in enumerate(eligible, 1):
    print(rank, s[0], "Marks:", s[1],
          "Attendance:", s[3], "Income:", s[4])

if not eligible:
    print("No eligible students found.")