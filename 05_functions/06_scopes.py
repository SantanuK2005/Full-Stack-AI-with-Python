def serve_chai():
    chai_type = "Masala"
    print(f"Instand function {chai_type}") 


chai_type = "lemon"
serve_chai()
print(f"outside function: {chai_type}")

def chai_counter():
    chai_order = "Lemon"
    def print_order():
        chai_order = "Ginger"
        print("Inner:", chai_orde)
    print_order()
    print("order:", chai_order)

chai_orer = "tulsi"
chai_counter()
print("Global :", chai_order)