import evenodd from evenodd 
import positive_negative from posneg

print("Hello, World!")
print("This is a sample Python script.")

try:
    user_input = input("Enter a Number: ")
except EOFError:
    user_input = "0"
    print("No input provided. Using 0.")

x = int(user_input)
print(evenodd(x))
print(positive_negative(x))
print("You entered:", x)