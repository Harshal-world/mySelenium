import json
f_path = r"C:\Users\harsh\Desktop\mySelenium\Sample.json"
a = False
b = json.dumps(a)
print(b)
d = {'a':12, 'b': 65}
with open(f_path, "w") as jsonfile:
    json.dump(d, jsonfile)

with open(f_path) as read:
    data = json.load(read)
    print(data)