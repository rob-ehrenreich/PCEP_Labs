def read_int(prompt, min, max):
    while True:
        try:
            userin = int(input(prompt))
            assert min <= userin <= max
            return userin
        except ValueError:
            print("Error: Wrong input")
        except AssertionError:
            print(f"Error: the value is not within permitted range ({min}..{max})")

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
