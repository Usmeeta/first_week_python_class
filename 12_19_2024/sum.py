def sum(*args):
    result = 0
    for number in args:
        result += number
        return result


def mul(*args):
    result = 0
    for number in args:
        result *= number
        return result

def exponential():
    pass

def print_name(name="ASMITA"):
    print(f"Hello {name}")

print(sum(1,2,3,4,5,6,7,8))
print(mul(1,2,3,4,5,6,7,8))