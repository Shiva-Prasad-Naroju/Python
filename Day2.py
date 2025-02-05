
# Program to count the number of uppercase characters in a given string

# Method 1: Using character comparison
str2 = 'SHivaa PrasaD'
i = 0
end = len(str2) - 1
total_upper_char = 0

while i <= end:
    if 'A' <= str2[i] <= 'Z':
        total_upper_char += 1
    i += 1

print(total_upper_char)

# Method 2: Using ASCII values
str3 = 'SHivaa PrasaD HarTEJIOANDFJ'
i = 0
end = len(str3) - 1
total_upper_char = 0

while i <= end:
    if 65 <= ord(str3[i]) <= 90:
        total_upper_char += 1
    i += 1

print(total_upper_char)

# -----------------------------------------------------------------------------------------

# Program to count the number of lowercase characters in a given string

# Method 1: Using ASCII values
str3 = 'SHivaa PrasaD HarTEJIOANDFJ'
i = 0
end = len(str3) - 1
total_lower_char = 0

while i <= end:
    if 97 <= ord(str3[i]) <= 122:
        total_lower_char += 1
    i += 1

print(total_lower_char)

# Method 2: Using character comparison
str3 = 'SHivaa PrasaD HarTEJIOANDFJ'
i = 0
end = len(str3) - 1
total_lower_char = 0

while i <= end:
    if "a" <= str3[i] <= "z":
        total_lower_char += 1
    i += 1

print(total_lower_char)

