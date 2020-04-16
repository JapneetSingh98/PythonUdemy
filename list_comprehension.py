temps = [221, 234, 340, -9999, 231]

new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)