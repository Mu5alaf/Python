from sys import argv

script, user_name = argv
prompt = '>'
#using %s for string formatting
print("Hi Im %s %s Script" % (user_name,script))
print("i would like to aske you few questions")

print("Do you Know %s ?" % (user_name))
yes = input(prompt)

print("Where do you live %s ?" % (user_name))
lives = input(prompt)

print("what kind of computer do you have ?")
computer = input(prompt)

#using Raw string %s
print("""
    Alrgith, sp you said %r about knowing me
    you live in %r and you have %r and it's nice pc
    """ %(yes,lives,computer))