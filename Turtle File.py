#################################################################################
##
## CS 101
## Program #4
## Ethan McFarland
## Em463@mail.umkc.edu
##
## PROBLEM: Open and execute turtle drawing of user specified files while
##          properly handling any errors that occur
##
## ALGORITHM: 
##      1.Get user input, open file, and call appropriate function
##          1.Retrieve user input
##          2.Try to open file, excepting FileNotFoundError, return to 1
##              1.Declare 'data' as empty list
##              2.For line in file
##                  1.Strip line of '\n', split along ',', and append to line
##              3.For line in data
##                  1.For number and element in line
##                      1.Equate line at index number with stripped element
##                  2.Try to pass line to function list, excepting IndexError or TypeError, return to 1 
##                  3.Draw file contents with appropriate function
##      2.Ask for and then validate user input, then determine if loop program
##        or terminate program
##          1.Retrieve user input
##          2.While user input is not Y, YES, N, or NO
##              1.Inform user that user input is invalid and ask for user input
##          3.If user input is Y or YES, return to beginning
##          4.Else, terminate program
## 
## ERROR HANDLING:
##      None
##
## OTHER COMMENTS:
##      None
##
#################################################################################

from math import *
from turtle import *
import os

def draw_rectangle(x, y, width, height, color):
    """Draws a rectangle of given width and height at position x, y"""

    x = int(x)
    y = int(y)
    width = int(width)
    height = int(height)
    
    penup()
    goto(x,y)
    pendown()
    
    fillcolor(color)
    pencolor(color)
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw_circle(x, y, radius, color):
    """Draws a circle with turtle at the point x, y with the given radius""" 

    radius = int(radius)
    x = int(x)
    y = int(y)
    y += radius/12.5
    color = str(color)

    circum = 2 * pi * radius 
    segment = circum/36
    
    penup()
    goto(x,y)
    forward(radius)
    right(90)
    pendown()
    
    fillcolor(color)
    pencolor(color)
    begin_fill()
    for i in range(36):
        forward(segment)
        right(10)
    end_fill()

def draw_triangle(x, y, width, height, color):
    """Draws a triangle of given width and height at position x, y"""

    x = int(x)
    y = int(y)
    width = int(width)
    height = int(height)
    
    penup()
    goto(x,y)
    pendown()
    
    fillcolor(color)
    pencolor(color)
    begin_fill()
    for i in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw_line(x, y, head, length, color):
    """Draws a line of from heading to given length at position x, y"""

    x = int(x)
    y = int(y)
    head = int(head)
    length = int(length)
    
    penup()
    goto(x,y)
    pendown()
    
    fillcolor(color)
    pencolor(color)
    begin_fill()
    setheading(head)
    forward(length)
    end_fill()
    
speed(10)
    
func_list = {'RECT':draw_rectangle,
             'rect':draw_rectangle,
             'circle':draw_circle,
             'triangle':draw_triangle,
             'line':draw_line
             }

while True:
    #Get user input, open file, and call appropriate function
    user_input = input('\nEnter File to open and draw ==> ')
    try:
        with open(user_input) as file:
            data = []
            for line in file:
                data.append(line.strip('\n').split(','))
            for line in data:
                for num,ele in enumerate(line):
                    line[num] = ele.strip()
                try:
                    func_list[line[0]](*line[1:])
                except IndexError:
                    print('IndexError\n\nTry again.')
                    continue          
                except TypeError:
                    print('TypeError\n\nTry again.')
                    continue
    except FileNotFoundError:
        print('FileNotFoundError\n\nTry again.')
        continue

    #Ask for and then validate user input, then determine if loop program or terminate program
    play = input('\nDo you want to try another word? Y/YES/N/NO ==> ').upper()
    while not (play in ('Y', 'YES', 'N', 'NO')):
        play = input('You must enter Y YES N or NO\n\nDo you want to try another word? Y/YES/N/NO ==> ').upper()
    if play in ('Y', 'YES'):
        continue
    else:
        break
