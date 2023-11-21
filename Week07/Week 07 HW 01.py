from termcolor import colored
import time

display = [1,2,3,4,5,6,7,8]

dir = 1
index = 1
bounceCount = 3

while(True):
    # This sets each item in the display to black
    for d in range(0, len(display)):
        display[d] = colored(' ', 'black', attrs=['reverse', 'blink'])
    
    # If we have reached the rightmost display element
    if(index >= len(display) - 1):
        dir = -1
        bounceCount -= 1

    # If we have reached the leftmost display element
    if(index <= 0):
        dir = 1
        bounceCount -= 1

    # If we are out of bounces we can break
    if(bounceCount <= 0):
        break

    # Increment our index by the direction we are going
    index += dir

    # Set the element that should be red
    display[index] = colored(' ', 'red', attrs=['reverse', 'blink'])

    # Print out the actual display
    for d in display:
        print(d, end="")
    print('')

    time.sleep(.2)