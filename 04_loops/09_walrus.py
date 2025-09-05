# value = 20

# remainder = value % 5

# if remainder:
    # print(f"Not divisible by 5, remainder is {remainder}")

value = 13
if remainder := value % 5:
    print(f"Not divisible by 5, remainder is {remainder}")
    

# available_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter a size: ")) in available_sizes:
#     print(f"Serving {requested_size} Chai")

# else:
#    print(f"size is not available-{requested_size}")



flavors = ["Masala Tea", "Ginger Tea", "Cardamom Tea", "Saffron Tea"]

print("Available flavors:", flavors)

while (flavor := input("Choose a flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")
print(f"You chose {flavor} flavor")