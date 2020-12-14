from math import ceil
print("Перша константа", False)
print("Друга константа", True)

print(ceil(12.5), f"є рівним {ceil(12.5)}")

A = False
if A:	
	print("Not False")
else:
	print("Not True")

try:
  print(x)
except NameError:
  print("Змінна x не є оголошена")
except:
  print("Щось пішло не так")

with open("./text.txt", "r") as f:
    for line in f:
        print(line)

sum_lambda = lambda a, b:f"Добуток двох чисел {a*b}"
print("Це просто функція:", sum_lambda)
print("Це її виклик:", sum_lambda(4,2))