from sys import argv

script , filename = argv

print("we're  going to erase %r." % filename)
print("if you want to stop the operation it CTRL-C")
print("if you  want that Hit yes")

user_input = input(">>>")

if user_input == "yes":
    print("Opening file....")
    target = open(filename,'w')

    print("Truncating the File. Done")
    target.truncate()

    print("Now im goinig to ask for three Lines")

    line_1 = input("Line 1 : ") 
    line_2 = input("Line 2 : ") 
    line_3 = input("Line 3 : ") 

    print("Im going to Write these to the file.")

    target.write(line_1)
    target.write("\n")
    target.write(line_2)
    target.write("\n")
    target.write(line_3)
    target.write("\n")

    print("Done")

    target.close()
else:
    print("Good Bye")
    exit
