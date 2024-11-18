numbers = [x for x in range(1, 101)]
print(numbers)

even_numbers = [x for x in range(1, 101) if x % 2 == 0]
print(even_numbers)

names = ["anna", "gio", "nika", "mari"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)

squares = [x**2 for x in range(1, 11)]
print(squares)
