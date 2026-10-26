text = "Python is easy. Python is powerful!".lower()
freq = {}

for word in text.split():
    word = word.strip(".,!?")
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(f"{word} : {count}")

print("Word frequencies calculated successfully.")
