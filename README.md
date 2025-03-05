# Python  

*In this README, I will share Python concepts through exercises from the book Learn Python the Hard Way. The exercises are designed to take you from a beginner level to an intermediate level, making it a journey of discovering what the Python programming language is all about.*

---

<img src="/images/7LIp.png" width="auto" hight="auto"/>

---

## exercise_1.py

**What is exercise_1.py ?**

- <File_name>.<file_extension> python source code file use the `.py` extension. These files contain the actual Python code and can be executed by the Python interpreter.

**What the best Practices in python file name?**

- Good:`data_visualization.py, user_authentication.py`
- Bad: `DataVis.py, auth.py`

**What the Print?**

- The print() is function prints the specified message to the screen, or other standard output device.

## exercise_2.py 

**What is # ?**

- `#` is way to write a comment

**What is the comment?**

- Comments can be used to explain Python code.
- Comments can be placed at the end of a line, and Python will ignore the rest of the line.
- Comments can be used to prevent execution when testing code

There's severl ways to writ a commnet in python script such

- Using Hash `#`
- Using `(''' hello ''' or """ hello """ or 'hello')`

## exercise_3.py

**Python Operators.**

- `+` Plus
- `-` Minus
- `/` Slash
- `*` asterisk
- `%` Percent
- `<` less-than
- `>` greater-than
- `<=` Less-than-equal
- `>=` greater-than-equal

## exercise_4.py

**Variables and Names.**

- A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
- Variable names are case-sensitive (age, Age and AGE are three different variables)

*There are several techniques you can use to make them more readable:*

- Camel Case `myVariableName = "John"`
- Pascal Case `MyVariableName = "John"`
- Snake Case `my_variable_name = "John"`

## exercise_5.py

**String formatting.**

- String formatting is essential in python for creating dynamic and well-structuerd text by inserting values into strings.
- Tools of String Formatting
- F-string
- str.format()
- modulo operator(%)

````python
name = "A"
f"Hello , {name}"
````

## exercise_6.py

**Python input() Function.**

- The input() function allows user input.

**Syntax.**

- input(prompt)

````python
x = input('Enter your name:')
print('Hello, ' + x)
````

## exercise_7.py

**Parameters, Unpacking, Variables.**

- Parameters is variables placeholders for the actual values the function needs.
- Unpacking in Python refers to the process of taking elements from iterable objects like tuples, lists, or dictionaries and assigning them to variables. This feature simplifies the handling of compound data structures and enhances code readability.
- Variables are containers for storing data values.

**Syntax.**

````python
# Tuple with three elements

my_tuple = (1,2,3)

x,y,z = my_tuple

print(x,y,z)

````

````python
# Unpacking Iterables
data = [100, 200, 300]
a, b, c = data
print(a, b, c)

````

````python
# Packing with * Operators
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))

````

- The asterisk (*), known as the star operator, is used in Python to pack arguments into a tuple. This allows functions to accept an arbitrary number of arguments, providing flexibility in function calls. The star operator can be used in function definitions to signify that the function can receive any number of positional arguments.

- An import statement in Python is used to call a Python module or library that provides a specific functionality. This allows your code to use the functions, classes, or variables defined in that module.

````python
import math
print(math.pi)
````

## exercise_9.py & exercise_10.py

**Files.**

 ``r``   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+``  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w``   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+``  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.
 ``a``   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+``  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.

The truncate() method resizes the file to the given number of bytes.

## Operators Precedence

<img src="/images/Python-operator-precedence-1.webp" width="auto" hight="auto"/>


