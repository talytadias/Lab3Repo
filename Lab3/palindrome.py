# Lab3Repo - Palindrome

print "Enter word: "
x = raw_input("")

y = x[::-1]

if x.upper() == y.upper():
	print x,"is a palindrome!"
else:
  print x,"is not a palindrome!"