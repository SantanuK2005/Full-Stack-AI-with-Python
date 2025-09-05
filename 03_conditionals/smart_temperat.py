device_status = "active"
temperature = 38  # Example temperature value

if device_status == "active":
    if temperature > 35:
        print("Device is active and temperature is high.")
    else:
        print("Device is active and temperature is normal.")
else:
    print("Device is inactive")