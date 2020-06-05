# Jose Soto
# Chapter 5 Assignment

# Write a program that requests a number from the user.  Have the program
# print "Even" or "Odd" depending on whetehr they entered an even or
# odd number.  Extend the program above to repeatedly ask that question as long 
# as the user enters a nonzero number.  But if they enter 0, it should then stop
# asking and say goodbye.

print("----------Welcome to the Even/Odd Program!----------")
print()

num_text = input("Please input a number: ")
num = int(num_text)
remainder = num % 2

if remainder == 0:
    print(f"The number {num} that you entered is EVEN!")
else:
    print(f"The number {num} that you entered is ODD!")

while num != 0:
    num_text = input("Please input another number besides 0: ")
    num = int(num_text)
    remainder = num % 2
    
    if num == 0:
        break
    if remainder == 0:
        print(f"The number {num} that you entered is EVEN!")
    else:
        print(f"The number {num} that you entered is ODD!")

print("You have entered 0, exiting program. Goodbye!")
