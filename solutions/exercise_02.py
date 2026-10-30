x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x <= y and y <= z:
    print(True)
else:
    print(False)

# A comparison is already a True/False value, so the if is not needed
print(x <= y and y <= z)
