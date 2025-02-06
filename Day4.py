# write a program to print the index number and the element of a list

l = ['shiva', 'prasad', 'naroju', 'tkr', 15, 26, 29]
i = 0
end = len(l)-1

while i <= end:
    print((i, l[i]))
    i+=1

# output
# (0, 'shiva')
# (1, 'prasad')
# (2, 'naroju')
# (3, 'tkr')
# (4, 15)
# (5, 26)
# (6, 29)


# now write the same program that should give output like
# [(0, 'shiva'),(1, 'prasad'),(2, 'naroju'),(3, 'tkr'),(4, 15),(5, 26),(6, 29)]

l = ['shiva', 'prasad', 'naroju', 'tkr', 15, 26, 29]
i = 0
end = len(l)-1
list = []

while i <= end:
    list.append((i, l[i]))
    i+=1
print(list)

# output we got
# [(0, 'shiva'), (1, 'prasad'), (2, 'naroju'), (3, 'tkr'), (4, 15), (5, 26), (6, 29)]
# ---------------------------------------------------------------------------------------------

# write a program to print all the occurrences in a list

l = ['shiva', 'prasad', 'naroju', 'tkr', 15, 26, 29, 'shiva', 'shiva', 26, 'naroju', 26, 29,15, 29]
n = eval(input('enter the value :   '))
i = 0
end = len(l)-1

while i <= end:
    if n == l[i]:
        print(n)
    i+=1