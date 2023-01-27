import turtle

def draw_square():
    # Create a turtle object
    square = turtle.Turtle()
    # Use a for loop to repeat the following commands 4 times
    for i in range(4):
        square.forward(100) # move the turtle forward by 100 units
        square.right(90) # turn the turtle right by 90 degrees

draw_square()
turtle.done()

