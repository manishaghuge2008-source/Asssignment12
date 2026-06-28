def analyze_string(s):
    if s == "":
        print("Empty string entered!")
        return

    print("Length:", len(s))


    print("Reverse string:", s[::-1])

    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    print("Number of vowels:", count)

    print("\nCharacters with index:")
    for i in range(len(s)):
        print("Positive index:", i, "->", s[i], " | Negative index:", i - len(s), "->", s[i - len(s)])



text = input("Enter a string: ")
analyze_string(text)