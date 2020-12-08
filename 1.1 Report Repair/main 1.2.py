report = open(r"/1.1 Report Repair/Expense Report", "r")

def trio_product_2020(entries):
    # Makes entries into a list of integers
    expenses = [int(entry.replace("\n", "")) for entry in entries.readlines()]

    for x in range(0, len(expenses)):
        for y in range(1, len(expenses)):
            for z in range(2, len(expenses)):
                if expenses[x] + expenses[y] + expenses[z] == 2020:
                    ans = expenses[x] * expenses[y] * expenses[z]
                    print(f"Values are {expenses[x]}, {expenses[y]} and {expenses[z]}")
                    print(f"Answer is: {ans}")
                    return ans


trio_product_2020(report)