from sys import argv

script, filename = argv

txt = open(filename)

print ("Here's your file %r: " % filename )

#Readtext
print (f"{txt.read()}")

print("Trype filename again:")

file_again = input(">")

# open the file
text_again = open(file_again)

print(f"{text_again.read()}")

