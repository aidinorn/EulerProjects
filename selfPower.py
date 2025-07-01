# Problem 48

# Calculate the sum of the series n^n for n from 1 to 1000,and print the last 10 digits of the result.

result =sum(num**num for num in range(1,1001))
print(str(result)[-10:])
