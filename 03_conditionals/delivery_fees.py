order_amount = int(input("Enter the order amount: "))

# print(f"Order Amount: {type(order_amount)}")

delivery_fee = 0

# delivery_fee = 0 if order_amount < 300 else 30

if order_amount < 300:
    delivery_fee = 0
elif order_amount > 300:
    delivery_fee = 30

print(f"Delivery Fee: {delivery_fee}")