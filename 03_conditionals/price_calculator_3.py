cup = input("Choose your cup size (small, medium, large): ").lower()
if cup == "small":
    print(f"Price is 10 rupees")
elif cup == "medium":
    print(f"Price is 15 rupees")
elif cup == "large":
    print(f"Price is 20 rupees")
else:
    print("Invalid cup size selected.")