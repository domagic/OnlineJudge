quantity_electric_charge = int(input())
if quantity_electric_charge < 0:
    print("Invalid Value!")
else:
    print("cost = {0:.2f}".format(
        quantity_electric_charge * 0.53 if quantity_electric_charge <= 50 else (
                50 * 0.53 + (quantity_electric_charge - 50) * (0.53 + 0.05))))
