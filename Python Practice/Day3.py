
# write a program to count the number of integers in the given string:

s = 'SHivaa15 PrasaD26 Ha29TEJIOANDFJ'
i = 0
end = len(s)-1
total_numbers = 0

while i <= end:
    if "0" <= s[i] <= "9":
        total_numbers+=1
    i+=1
print(total_numbers)
# -----------------------------------------------------------------------------------------

# Write a program to print the special characters in the given string:

s = '$hiva@@H@rTe)(#$)'   # 9 special characters are there in the string 's'
i = 0
end = len(s)-1
total_spc_char = 0

while i <= end:
    if not ("A" <= s[i] <= "Z" or "a" <= s[i] <= "z" or "0" <= s[i] <= "9"):  #with brackets
        total_spc_char += 1
    i+=1
print(total_spc_char)

# -----------------------------------------------------------------------------------------

# write a program to create a new string with only vowels:

s = 'apple is'
i = 0
end = len(s)-1
vowels = ""

while i <= end:
    if s[i] in 'AEIOUaeiou':
        vowels+=s[i]
    i+=1
print(vowels)

# -----------------------------------------------------------------------------------------

