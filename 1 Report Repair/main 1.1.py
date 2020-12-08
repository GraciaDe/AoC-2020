report = open("Expense Report", "r")

def product_2020(entries):
    # Makes entries into a list of integers
    expenses = [int(entry.replace("\n", "")) for entry in entries.readlines()]

    for num in range(1, (len(expenses))):
        for i in expenses:
            if i + expenses[num] == 2020:
                ans = i*expenses[num]
                print(f"Values are {i} and {expenses[num]}")
                print(f"Answer is: {ans}")
                print(f"Expenses length: {len(expenses)}")
                return ans


product_2020(report)