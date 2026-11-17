def class_average(students, passing=40):
    total = 0
    passed = 0
    for s in students:
        # BUG 1: "total = ..." replaced the total each time instead of adding to it.
        # How pdb showed me: p total after each student showed 88, 92, 79, 40
        # (just that student's marks) instead of a growing sum.
        total += s["marks"]
        # BUG 2: ">" did not count a student who scored exactly the pass mark.
        # How pdb showed me: for Dev, p s["marks"] > passing gave False,
        # but 40 is the pass mark, so he should pass.
        if s["marks"] >= passing:
            passed += 1
    average = total / len(students)
    pass_rate = passed / len(students) * 100
    return average, pass_rate

data = [
    {"name": "asha", "marks": 88},
    {"name": "ravi", "marks": 92},
    {"name": "meera", "marks": 79},
    {"name": "dev", "marks": 40},
]
avg, rate = class_average(data)
print(f"average: {avg}")
print(f"pass rate: {rate}%")