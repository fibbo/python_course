"""Water state exercise.

Ask for a temperature and print whether water is solid, liquid or gas at that
temperature.
"""

temp = float(input("Please enter the temperature: "))

if temp < 0:
    state = "solid"
elif temp < 100:
    state = "liquid"
else:
    state = "gas"


print(f"At {temp} °C water is {state}")
