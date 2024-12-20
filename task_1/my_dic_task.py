my_dict = {
  "name": "Jhon",
  "age": 25,
  "city": "New York",
}
my_dict["job"] = "Engineer"
my_dict.update({"age": 26})
my_dict.pop("city")

x = my_dict.keys()
print(x)


for index, values in enumerate(my_dict):
    print(f'Item position: {index} and value: {values}')

print(my_dict)