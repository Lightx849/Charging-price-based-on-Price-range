#Charging price based on Price range

Cafes = ["Dunkin" , "Costa Coffe" , "On and off" , "Starbucks"]

price_range = ["1-20", "20-60" , "40-80" , "80-100"]

price_charge = 90

print("="*35)
for cafe, price in zip(Cafes, price_range):
    print(f"{cafe} has the price range of {price}")
    # then calculate your charges directly here!

    if price == "1-20":
        charge_per_nfc = price_charge * 1.5
        print(f"For {cafe} we will charge: Sar{charge_per_nfc}")

        print()

    elif price == "20-60":
        charge_per_nfc = price_charge * 2
        print(f"For {cafe} we will charge: Sar{charge_per_nfc}")

        print()

    elif price == "40-80":
        charge_per_nfc = price_charge * 2.5
        print(f"For {cafe} we will charge: Sar{charge_per_nfc}")

        print()

    elif price == "80-100":
        charge_per_nfc = price_charge * 3
        print(f"For {cafe} we will charge: Sar{charge_per_nfc}")

        print()
print("="*35)









    
