
jClass = ["John", ("John", 106, False), 106, {"John", 106, False}, False]


state = True
indexer = 0
value = jClass
count = 0

while(state):
    t = type(value)

    if(value == "John"):
        count += 1

    if(t == tuple or t == set or t == list or t == set):
        indexer = 0
        value = value[0]

    indexer += 1

    