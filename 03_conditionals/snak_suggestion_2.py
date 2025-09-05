snack = input("What snack do you want: ").lower()

# print(f"User said :{snack}")

if snack == "cookies" or snack == "cake":
    print(f"You selected a sweet snack! {snack}")
else:
    print(f"Sorry, we only serve cookies and cake! {snack}")