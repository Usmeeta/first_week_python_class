for x in "banana":
   print(x)
a = "Hello world!"
print (len(a))

life = "life is full of happiness"
print("happiness" in life)

b = "Hello world !"
print(b[2:5])

print(b[:3])

print(b[-5:-3])

print(b.upper())
print(b.capitalize())
print(b.lower())

b = "hello    "
print(b.strip())


b = "Hello world"
print(b.replace("world", "asmita"))


z = b.split(",")
print(z)

name = input("Enter your name")

print("you have entered your name =" + name)   # String concatenation (Basic, but less efficient)
print(f"you have entered your name = {name}")   # f-string formatting (Modern and Recommended)
print("you have entered your name, %s" % {name})   # Formatted print with the % operator (Older method, generally not recommended)
