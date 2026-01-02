hey = "abcabcbb bbbbb pwwkew dvdf "
hey = "pwwkew"
counter = 0
letters = []
for x in range(len(hey)):
  if hey[x] not in letters:
    letters.append(hey[x])
    counter = len(letters)
    print(letters)
  else:
    if counter < len(letters):
      counter = len(letters)
    # letters = [hey[x]]
    letters.append(hey[x])
    letters = letters[1:]
    print("Second", letters)

print(counter)
print(letters)