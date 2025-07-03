# Simple Python program to find ASCII code of a character

# Prompt user for input
char = input("Enter a single character: ")

# Ensure user entered exactly one character
if len(char) == 1:
    ascii_code = ord(char)
    print(f"The ASCII (or Unicode code point) of '{char}' is: {ascii_code}")
else:
    print("Please enter exactly one character.")
