flavors = ["Ginger", "Out of stock", "Lemon", "Discontinued", "Tulsi"]


for flavor in flavors:
    if flavor == "Out of stock":
        continue
    if flavor == "Discontinued":
        break
    print(f"{flavor} item found:")

print(f"Out of loop:")