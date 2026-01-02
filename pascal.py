def factorial(x):
  y = 1
  for i in range(x):
    y*=(i+1)
  return y

# print(factorial(4)/(factorial(2) * factorial(2)))

for n in range(4):
  val = []
  for r in range(n+1):
    val.append(str(round(factorial(n)/(factorial(r)*factorial(n-r)))))
  print(" ".join(val))