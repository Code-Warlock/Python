import string
"""Pangram Program"""
word = input(": ").lower()
listed = list(word)
ref = []
for each in listed:
    if each not in f"{string.punctuation} ":
        ref.append(each)
ref = set(ref)
ref = list(ref)
ref.sort()
ref = "".join(ref)
if ref == string.ascii_lowercase:
    print(f"{word} is a pangram")
else:
    print(f"{word} is not a pangram")
