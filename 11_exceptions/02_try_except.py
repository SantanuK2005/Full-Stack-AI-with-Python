chai_manu = {"masala": 10, "ginger": 5}

try:
    chai_manu["lemon"]
except KeyError:
    print("This tea is not available.")

print("Program continues...")