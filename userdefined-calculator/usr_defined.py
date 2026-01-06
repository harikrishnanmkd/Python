import calc

x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))

print(f"Add {x}+{y}: {calc.add(x, y)}")
print(f"Subtract {x}-{y}: {calc.subtract(x, y)}")
print(f"Multiply {x}*{y}: {calc.multiply(x, y)}")
print(f"Divide:{x}/{y}, {calc.divide(x, y)}")
