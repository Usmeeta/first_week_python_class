def print_multiplication_table(number):
    """Prints the multiplication table of a number up to 10.

    Args:
        number: The number for which to print the table.
    """
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")


num = int(input("Enter a number: "))
print_multiplication_table(num)
