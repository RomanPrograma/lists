
words = input("enter words:  ").split()

words.sort(key=len)

print("Words are sorted by increasing length: ")
print(words)