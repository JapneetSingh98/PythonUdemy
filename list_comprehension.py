temps = [221, 234, 340, 230]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)


even_newer_temps = [temp / 10 for temp in temps]
print(even_newer_temps)