
# Write a program to add the numbers present inside the string which are along with characters

# Given string:
s = 'SHIVA2629'

# Logic:

# Using while loop:
i = 0
end = len(s)-1
total_sum = 0

while i <= end:
    if "0" <= s[i] <= "9":
        total_sum+= int(s[i])
    i+=1
print(total_sum)

# Using for loop:
# total_sum_of_nums = 0
# for i in s:
#     if i.isdigit():
#         total_sum_of_nums = total_sum_of_nums + int(i)
#     else:
#         ...
# print(total_sum_of_nums)