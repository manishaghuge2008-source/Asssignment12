import math

try:

    sentence = input("Enter a sentence: ")

    if sentence.strip() == "":
        print("Empty sentence entered!")
    else:

        words = sentence.lower().split()
        unique_words = set(words)

    
        sorted_words = sorted(unique_words)

        print("\n Unique words:", unique_words)
        print("Sorted unique words:", sorted_words)
  
        count = len(unique_words)

        result = math.pow(count, 2)

        print("Total unique words:", count)
        print("Square of unique words count:", result)

except Exception as e:
    print("Error occurred:", e)