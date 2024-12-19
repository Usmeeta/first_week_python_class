def print_full_name(**kwargs):
    print(kwargs)
    print(f"My full name is {kwargs['first_name']} {kwargs['last_name']}")

print_full_name(first_name="ASMITA", last_name="RAJAK", middle_name="None")

def print_result(*args, **kwargs):
    result = 0
    for number in args:
        result += number
    print(f"My full name is {kwargs['first_name']} {kwargs['last_name']} and total marks = {result}")

print_result(10, 20, 30, 40, 50, first_name="ASMITA", last_name="RAJAK")