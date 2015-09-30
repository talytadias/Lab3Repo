a = 1 #f1
b = 1 #f2
r = 2 #f3
while (len(str(b))) < 1000: # while size of b is less than 1000
    a, b = b, a + b # a equals to b and b equals to a + current value of b
    r = r + 1 # add 1 to current value of r

print("The first term in the Fibonacci sequence to contain 1000 digits is:")
print(r)

#print("And the 1000 digit number is:")
#print(b)
