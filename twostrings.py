stra = "hello"
strb = "78909"
isstr = False
for letter in strb:
  if letter in stra:
    isstr = True
    break
print(isstr)