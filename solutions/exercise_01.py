temperature_text = input("Temperature in degrees Celsius: ")
temperature = float(temperature_text)

# Let's assume water is liquid between 0 and 100 degrees Celsius, solid below 0, and gas above 100.
if temperature < 0:
    state = "solid"
elif temperature <= 100:
    state = "liquid"
else:
    state = "gas"

print(f"At {temperature_text} °C water is {state}")
