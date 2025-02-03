# Program to sum up the digits present in a given string:

str1 = 'Shiva262916'

# Sum of digits using the while loop:
def sum_digits_using_while(str1):
    """Returns the sum of digits in the string using a while loop."""
    i = 0
    
    total_sum = 0
    while i < len(str1):
        if str1[i].isdigit():
            total_sum += int(str1[i])
        i += 1
    return total_sum


# Sum of digits using for loop:
def sum_digits_using_for(str1):
    """Returns the sum of digits in the string using a for loop."""
    return sum(int(char) for char in str1 if char.isdigit())



# Example usage
print("Sum using while loop:", sum_digits_using_while(str1))
print("Sum using for loop:", sum_digits_using_for(str1))
