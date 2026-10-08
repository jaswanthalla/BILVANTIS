customers = int(input("Enter no of customers:"))

dict = {}

for i in range(customers):
    customer = input("Enter the customer name:")

    while True:
        units = int(input("Enter the no of units consumed by the customer:"))
        if units < 0:
            print("Invalid units")

        else:
            break

    if units <= 100:
        energy_charge = units * 5
    elif units <= 200:
        energy_charge = (100 * 5) + (units - 100) * 7
    else:
        energy_charge = (100 * 5) + (100 * 7) + (units - 200) * 10

    fixed = 50

    if energy_charge > 1000:
        sur_charge = energy_charge * 0.05

    else:
        sur_charge = 0

    total = energy_charge + fixed + sur_charge

    dict[customer] = {
        "Units": units,
        "Energy_charge": energy_charge,
        "Sur_charge": sur_charge,
        "Total": total,
    }


for k, v in dict.items():
    print(k, v)

highest = max(dict, key=lambda x: dict[x]["Total"])
print(highest)
