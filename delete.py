from keyboard import Layout

a = Layout()
b = Layout()

print(a)
print(b)
child = Layout.crossover(a, b)

print(child)
