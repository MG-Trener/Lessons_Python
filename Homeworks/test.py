
payments = [
    {"item": "Burger", "amount": 2500, "cat": "Food"},
    {"item": "Taxi", "amount": 1200, "cat": "Transport"},
    {"item": "Pizza", "amount": 3500, "cat": "Food"}
]

report = {}

for p in payments:
    category = p ["cat"]
    report.setdefault(category, {
        "total": 0,
        "items": []
    })
    # print(report)
    report[category]["total"] += p["amount"]
    report[category]["items"].append(p["item"])
# print(report)
for r in report.values():
    print(r)
print()
for r in report.items():
    print(r)