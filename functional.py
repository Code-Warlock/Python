# LEGB ====> Local,Enclosing Function call,Global and Built-ins

def palin(w):
    if w == w[::-1]:
        return "Word is a palindrome!"
    else:
        return "Word is not a a palindrome!"


word = input("Enter the word : ").strip().lower()
print(palin(word))
