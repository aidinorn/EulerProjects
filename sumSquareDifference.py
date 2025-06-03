# Problem 6

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumOFSquares = sum(num ** 2 for num in range(1, 101)) # Sum Of The Squares Numbers Range Of 0 to 100
squareOfTheSum = sum(num for num in range(1, 101))**2 # Square Of The Sum Numbers Range Of 0 to 100
print(squareOfTheSum-sumOFSquares)
