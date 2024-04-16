[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588388&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project Spring, 2024

## Team Members

Caitlin Bullock and Anya Wester

***

## Project Description

A game where you count the stars in the sky before time runs out 

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Timer
2. Play button
3. Randomly placed stars 
4. Clicker feature
5. Ending statement

### Classes

import random

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def blink(self):
        # Simulate blinking effect of stars
        return random.choice([True, False])

class Sky:
    def __init__(self, width, height, num_stars):
        self.width = width
        self.height = height
        self.stars = []
        self.generate_stars(num_stars)

    def generate_stars(self, num_stars):
        for _ in range(num_stars):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            self.stars.append(Star(x, y))

    def display(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if any(star.x == x and star.y == y and star.blink() for star in self.stars):
                    row += "*"
                else:
                    row += " "
            print(row)

# Example usage
night_sky = Sky(50, 20, 100)
night_sky.display()


- << You should have a list of each of your classes with a description >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
