

def count_vowels(s):

    s = s.lower()

    vowels = "aeiou"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    print("Total vowels:", count)


text = input("Enter a string: ")

count_vowels(text)