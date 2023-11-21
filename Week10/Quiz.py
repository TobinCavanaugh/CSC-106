jClass = ["John", ("John", 106, ["John", "John"]), 106, {"John", 106, False}, False, "John"]

# Recursive function to locate all Johns
def FindJohns(value):
    johnCount = 0
    t = type(value)

    # If we have a data container, we want to traverse each of its elements
    if (t == (list) or t == (set) or t == (tuple) or t == (dict)):
        for el in value:
            print(f"internal element: {el} {type(el)}")
            johnCount += FindJohns(el)

    # This is the actual check
    elif (value == "John"):
        print(f"Found!: {johnCount + 1}")
        johnCount += 1

    print(f"Returning from {value}")
    return johnCount

print(FindJohns(jClass))