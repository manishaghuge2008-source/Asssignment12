try:
  
    square = lambda x: x * x

    squares = []

  
    for i in range(1, 21):
        squares.append(square(i))

    print("All squares:", squares)

    even_squares = [num for num in squares if num % 2 == 0]

    print("Even squares:", even_squares)

except Exception as e:
    print("Error occurred:", e)

    