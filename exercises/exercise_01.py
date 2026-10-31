"""Water state exercise.

Ask for a temperature and print whether water is solid, liquid or gas at that
temperature.
"""

temp_text = input("Please enter the temperature: ")
temp = float(temp_text)

if temp < 0:
    state = "solid"
elif temp <= 100:
    state = "liquid"
else:
    state = "gas"


print(f"At {temp_text} °C water is {state}")
