#file = open("order.txt", "w")
#try:
#    file.write("First Order")
#finally:
#    file.close()


with open("order.txt", "w") as file:
    file.write("Good Tea - 4 cups")