"""
Tobin Cavanaugh
Due 11/10/2023
Week 09 Revision
"""

# -----------------------------------------------------------------#

# Question 1:
# int
intVal = 1

# float
floatVal = 1.0

# char
charVal = 'A'

# boolean
boolVal = True

# string primitiveness depends on language
stringVal = "Abc"

# -----------------------------------------------------------------#

# Question 2:
# Tuple:
tupleVal = (1, "Abc", 52.3, True)

# Set
setVal = {1, "Abc", 123.5, True}

# Dictionary
dictVal = {0: 1, 1: "Abc", 2: 123.4, 3: True}

# List
listVal = [1, "Abc", 123.4, True]

# -----------------------------------------------------------------#

# Question 3
# I use lists which is not ideal. In a better language, there
# would be a fixed size mutable construct (array) so we could prevent
# jagged matrices from ever being a possibility
matrix3x4 = [[0.0, 1.0, 2.0, 2.0],
             [3.0, 4.0, 5.0, 3.0],
             [6.0, 7.0, 8.0, 4.0]]

# -----------------------------------------------------------------#

# Question 4

for a in tupleVal:
    print(a)

for a in setVal:
    print(a)

for a in dictVal:
    print(a)

for a in listVal:
    print(a)

# -----------------------------------------------------------------#
