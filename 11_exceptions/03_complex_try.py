def serve_chai(flavor):
    try:
        print(f"Serving {flavor} chai.")
        if flavor == "unknown":
            raise ValueError("Unknown flavor requested!")
    except ValueError as e:
        print("Error:", e)
    else:
        print(f"{flavor} chai served successfully.")

    finally:
        print("Thank you for visiting our chai shop!")

serve_chai("masala")
serve_chai("unknown")
