phone_book = {
  "Anny": "9866655551",
  "Smirit": "9841526688",
  "simona": "9813003678",
  "ujjwol": "9955457845",
}

phone_book.update({"kalyan": "9855443322"}) 

for x, y in phone_book.items():
  print(x, y) 



print(phone_book["Anny"])
