def is_leap_year(year):
    """Checks if a year is a leap year.

    Args:
        year: The year to check.

    Returns:
        True if the year is a leap year, False otherwise.  Returns an appropriate message for invalid input.
    """
    if not isinstance(year, int):
        return "Invalid input. Please enter an integer year."
    if year <= 0:
        return "Invalid input. Please enter a positive integer year."
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False



year_input = int(input("Enter a year: "))
result = is_leap_year(year_input)
if isinstance(result, bool):
    if result:
        print(f"{year_input} is a leap year.")
    else:
        print(f"{year_input} is not a leap year.")
else:
    print(result)  
