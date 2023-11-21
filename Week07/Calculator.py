"""
Tobin Cavanaugh
10/19/2023
Week 06 Assignment 2
CSC 106
"""


import math

mem1 = 0

while (True):
    # Get the equation from the user
    eq = input("Enter equation (m1 for memory): ").lower()

    # Replace pi with the actual pi value
    eq = eq.replace("pi", str(math.pi))
    eq = eq.replace("m1", str(mem1))

    # Replace instances of trig functions with their py counterparts.
    # TODO This should be changed to use regex to optionally add the open parenthesis
    eq = eq.replace("sin", "math.sin(")
    eq = eq.replace("cos", "math.cos(")
    eq = eq.replace("tan", "math.tan(")

    # Replace double parenthesis, this is so if the user puts parenthesis, the code above doesnt cause issues 
    eq = eq.replace("((", "(")

    # This adds a closed parenthesis if one doesnt exist, and if we are using a trig func
    if(not ")" in eq and("sin" in eq or "cos" in eq or "tan" in eq)):
        eq += ")"
    
    # We wrap this in a try except so that errors dont quit program execution
    try:
        # We use the built in eval function. This allows for ACE. This is an unsafe calculator. I dont care.
        result = eval(str(eq))
        
        # Print our transformed equation and the result
        print("m1 = " + eq + " = " + str(result))

        # Assign the memory
        mem1 = float(result)

    except:
        print("The equation is not valid. Ensure you typed it correctly: \'" + str(eq) + "\'")