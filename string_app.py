class Word:
    def __init__(self, text):
        self.text = text

    def __eq__(self, other):
        return self.text == other.text

    def __add__(self, other):
        return Word(self.text + other.text)

    def __str__(self):
        return self.text

input1 = input("Enter first string: ")
input2 = input("Enter second string: ")

w1 = Word(input1)
w2 = Word(input2)


if w1 == w2:
    print("The strings are equal.")
else:
    print("The strings are not equal.")


w3 = w1 + w2
print("Concatenated string:", w3)
