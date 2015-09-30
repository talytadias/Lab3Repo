# Lab3Repo - Palindrome

print "Type word: "
x = raw_input("")

y = x[::-1]

if x.upper() == y.lower():
	print x,"is a palindrome!"
else:
  print x,"is not a palindrome!"