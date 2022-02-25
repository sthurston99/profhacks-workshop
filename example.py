'''
This is a Python file!
In case you didn't know, Python's a pretty popular programming language.
You probably already have the Python interpreter installed on your computer,
and you didn't even know it! That's how ubiquitous it is.

In fact, if you attended the earlier Intro to Programming workshop,
you should know a little bit about Python!

But if you didn't, and you don't, don't worry:
This is a simple Python script that just prints some words to the console.
It checks whether or not a variable is a certain vailue, and will print
one of two strings of text depending on whether it is, or isn't!

Feel free to tamper with it and make some changes, or add your own stuff!
It's not the most advanced code file in the world, but it's enough to show
how git will track your changes.
'''

num = 9

print("I'm going to check the num variable for the number 9.\n")

if num == 9:
	print("Hey! The num variable is 9! That's good news for some reason.")
else:
	print("Hmm, turns out that num was actually " + str(num) + ".")
