text = input("Enter any String: ")
words = text.split()
smallest = min(words, key=len)
print("Smallest word:", smallest)