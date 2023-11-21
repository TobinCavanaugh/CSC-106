import math

m1 = 0

while(True):

    eq = input("Enter Equation. Use m1 to use the previous answer as a value\n")

    # Lowercase the string
    eq = eq.lower()

    # Remove spaces
    eq = eq.replace(" ", "")

    # Replace instances of m1 with the memory value
    eq = eq.replace("m1", " " + str(m1) + " ")

    eq = eq.replace("pi", str(math.pi))

    mathSymbols = ["+", "-", "*", "/", "sin", "cos", "tan"]

    # Add spacing around math operations
    for sym in mathSymbols:
        eq = eq.replace(sym, " " + sym + " ")

    # Split all the different numbers and operations apart
    elements = eq.split(" ")

    # Remove any empty strings 
    while "" in elements:
        elements.remove("")

    print(elements)

    index = 0
    val = 0
    # Iterate through the elements
    # TODO Improvements in the future should happen inside of here, implementation of PEMDAS etc.
    for el in elements:

        # We set this value based on if the index operation throws and exception, exception based programming is a cancer
        mathSymb = True
        try:
            mathSymbols.index(el)
        except:
            mathSymb = False
            

        # if its not numeric and its inside the mathsymbols array, then we treat it as a symbol
        if(not el.isnumeric() and mathSymb):
            
            i0 = 1

            # Get the number before the operator if one exists
            if(index - 1 >= 0):
                # number before the operator
                i0 = float(elements[index - 1])

            # Number after the operator
            i1 = float(elements[index + 1])

            # This is a non ideal way of doing this
            if(el == "+"):
                val = i0 + i1 
            elif(el == "-"):
                val = i0 - i1
            elif(el == "*"):
                val = i0 * i1
            elif(el == "/"):
                val = i0 / i1
            elif(el == "sin"):
                val = i0 * math.sin(i1)
            elif(el == "cos"):
                val = i0 * math.cos(i1)
            elif(el == "tan"):
                val = i0 * math.tan(i1)
        index += 1

    # Assign m1 to the value
    m1 = val

    # print out the final value
    print(eq + " = " + str(val))