# Text analyzer

# Input text
text = input("Enter a text:\n")

# Three letters
print("\n.: First phase :. ")
a = input("Enter a first letter: ")
b = input("Enter a second letter: ")
c = input("Enter a third letter: ")

# Preparation
# Prepare the text transform it to lower case
text = text.lower()

# Analyze

# How many times each letter appears
print("\n.: Second phase :. ")
a_amount = text.count(a)
b_amount = text.count(b)
c_amount = text.count(c)

print(
    f"The letter {a} appears {a_amount} times\nThe letter {b} appears {b_amount}\n The letter {c} appears {c_amount}"
)

# How many word there are in the text
print("\n.: Third phase :. ")
words = text.split()
print(f"The text has {len(words)} words")

# First and last letter
print("\n.: Fourth phase :. ")
first_word = words[0]
last_word = words[len(words) - 1]
print(
    f"The first letter in the text is '{first_word[0]}' and the last is '{last_word[len(last_word)-1]}'"
)

# Words in reverse order
print("\n.: Fifth phase :. ")
words.reverse()
new_text = " ".join(words)
print(f"The text in reverse: {new_text}")
# appear Python word?
print("\n.: Sixth phase :. ")
python_appears = "python" in words
python = {True: "Yes, Python words appears", False: "No, Python word not appears"}
print(python[python_appears])
