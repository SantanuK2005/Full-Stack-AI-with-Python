staff = [("John", "Manager"), ("Jane", "Developer"), ("Doe", "Designer")]


for name, role in staff:
    if role == "Developer":
        print(f"Found the Developer: {name}")
        break
else:
    print("No Developer found.")