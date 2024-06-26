import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
slowpoke = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
slowpoke.shape('turtle')
# Set your turtle's speed using .speed(2)
slowpoke.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
slowpoke.color('green')
slowpoke.pencolor('blue')
# Move your turtle forward using .forward(100)
slowpoke.forward(100)
# TEST    Did your turtle move forward?
slowpoke.left(90)
# Move your turtle left or right using .left(90) or .right(90)
for i in range(4):
    slowpoke.left(90)
    slowpoke.forward(100)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?

# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
slowpoke.goto(0, 0)
slowpoke.begin_fill()
# Have your turtle draw a circle using .circle(radius, steps=30)
slowpoke.circle(30, steps=30)
# TEST    Did your turtle draw a circle?
slowpoke.end_fill()
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below

# Draw 3 more shapes with different fill colors!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
