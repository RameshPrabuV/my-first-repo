# cancating two strings
name1 = "Ramesh"
name2 = "Prabu"
result = name1 + " " + name2
print(result)

#length of the string
text = "Python is awesome"
length = len(text)
print("length of the text is", length)

#convert all strings into lowercase & uppercase
text1 = "PytHon is aweSome"
text2 = "python is super awesome"
lowercase = text1.lower()
uppercase = text2.upper()
print("lowercase:", lowercase)
print("uppercase:", uppercase)

#replacing text
line = "I am excited to study python in India"
new_line = line.replace("India", "Japan")
print("modified text:", new_line)

#splitting text
splittext = text.split()
print(splittext)

#stripped text
example = "   .,,,ttt      He is amazingt boy ,,,,ttt  "
stripped_text = example.strip(".,t ")
print("text is", stripped_text)

#substring
aaa = "he lied the statement"
substring = "is"
if substring in aaa:
    print(substring, "Found the text")
else:
    print(substring, "not found in text")

#basic arthimatic operations
x = 10
y = 7.5
Add = x + y
Sub = x - y
Mul = x * y
Div = x / y
print("Addition:", Add)
print("Subtraction:", Sub)
print("Multiplication:", Mul)
print("Division:", Div)

z = 3.1415678543
roundoff = round(z, 3)
print("Roundoff value is :", roundoff)

result1 = x // y
print("Answer without floating numbers:", result1)

result2 = x % y
print("The Remainder is:", result2)

result3 = abs(-7)
print("Absolute Value:", result3)
