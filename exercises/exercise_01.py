temp = float(input("Please enter the temperature: "))

if temp < 0:
    state = "solid"
elif temp < 100:
    state = "liquid"
else:
    state = "gas"


print(f"At {temp} °C water is {state}")
