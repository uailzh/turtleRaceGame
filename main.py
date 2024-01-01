import turtle
import time
import random

# Set up the dimensions of the turtle racing screen
WIDTH, HEIGHT = 500, 500

# Define a list of colors that turtles can have
COLORS = ['red', 'cyan', 'brown', 'yellow', 'green', 'blue', 'orange', 'pink', 'black', 'purple']

# Function to get the number of racers from user input
def get_number_of_racers():
    racers = 0

    while True:
        racers = input("Enter the number of racers (2 - 10): ")

        # Validate input to ensure it's a digit
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input should be a number... Please, try again")
            continue

        # Check if the number of racers is within the specified range
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number should be in the range of 2 to 10!")

# Function to simulate the turtle race and determine the winner
def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            # Every time, randomly choose the distance the racer will move between one to twenty pixels
            distance = random.randrange(1, 20)
            racer.forward(distance)

            # Get the position of the racer
            x, y = racer.pos()

            # Check if the racer has reached or crossed the top of the screen
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

# Function to create turtle objects with specified colors
def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)  # Left and right are using degrees, so we turn the turtle, and forward, backward use pixels

        # Penup and pendown control how the line is drawn
        racer.penup()

        # Set the initial position of the turtle
        racer.setposition(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)

        # Pendown to start drawing
        racer.pendown()
        turtles.append(racer)

    return turtles

# Function to initialize the turtle screen
def ini_turtles():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

# Get the number of racers from the user
racers = get_number_of_racers()

# Initialize the turtle screen
ini_turtles()

# Shuffle and select colors for the racers
random.shuffle(COLORS)
colors = COLORS[:racers]

# Simulate the race and determine the winner
winner = race(colors)

# Print the color of the winning turtle
print("The winner is the turtle with color:", winner)

# Pause execution for 5 seconds before closing the window
time.sleep(5)
