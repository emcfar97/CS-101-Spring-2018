#####################################################################################
##
## CS 101
## Program #5
## Ethan McFarland
## Em463@mail.umkc.edu
##
## PROBLEM: Simluate physics for stone, sand, and water objects
##
## ALGORITHM: 
##      1.Draw user-input objects on graphics window
##          1.Call draw_screen function 
##          2.Assign retun of get_events function to events variable
##          3.For event in events
##              1.If event is 'CLEAR', assign grid to default value
##              2.Else, add x and y coordinates to grid at index 'event at index 0' 
##          4.For key and value in grid
##              1.For pair in value
##                  1.Pass key and pair to draw_grid function
##                  2.If key is not 'STONE', pass key and pair to appropriate physics
##                    function
## 
## ERROR HANDLING:
##      None
##
## OTHER COMMENTS:
##      None
##
#####################################################################################

import gravity_mod as gfx
import random
import time

def draw_grid(obj:str,x:int,y:int):
    '''Passes object and its x-y coordinates to draw_rect function'''
    size = 10
    resolution = 10
    
    x1 = x * resolution
    x2 = x1 + size
    y1 = y * resolution
    y2 = y1 + size

    if obj == 'STONE':
        win.draw_rect(x1, y1, x2, y2, "Darkgrey")
    elif obj == 'SAND':
        win.draw_rect(x1, y1, x2, y2, "Khaki")
    elif obj == 'WATER':
        win.draw_rect(x1, y1, x2, y2, "Cornflowerblue")

def sand_physics(pair:tuple):
    '''Applies gravity to sand objects'''
    temp = (pair[0], pair[1]+1)
    if (temp[1] <= 59) and (temp not in grid['STONE']) and (temp not in grid['SAND']):
        if temp in grid['WATER']:
            grid['SAND'].remove(pair)
            grid['WATER'].add(pair)
            grid['WATER'].remove(temp)
            grid['SAND'].add(temp)
        else:
            grid['SAND'].remove(pair)
            grid['SAND'].add(temp)      
    
def water_physics(pair:tuple):
    '''Applies gravity to water objects'''
    temp = (pair[0], pair[1]+1)
    if (temp[1] <= 59) and (temp not in grid['STONE']) and (temp not in grid['SAND']) and (temp not in grid['WATER']):
        temp = (pair[0], pair[1]+1)
        grid['WATER'].remove(pair)
        grid['WATER'].add(temp)

    else:
        slide = random.randrange(-1,2,2)
        temp = (pair[0]+slide, pair[1])
        if (0 <= temp[0] <= 60) and (temp not in grid['STONE']) and (temp not in grid['SAND']) and (temp not in grid['WATER']):
            try:
                grid['WATER'].remove(pair)
                grid['WATER'].add(temp)
            except KeyError:
                grid['WATER'].add(temp)

win = gfx.GravWindow()

functions = {
    'SAND' :sand_physics,
    'WATER':water_physics
    }

grid = {
    'STONE':set(),
    'SAND':set(),
    'WATER':set()
    }

while True:
    #Draw user-input objects on graphics window
    win.draw_screen()
    events = win.get_events()
    
    for event in events:
        if event == 'CLEAR':
            grid = {
                'STONE':set(),
                'SAND':set(),
                'WATER':set()
                }
        else:
            grid[event[0]].add(tuple(i//10 for i in event[1:]))
        
    for key,val in grid.items():
        for pair in val:
            draw_grid(key,*pair)
            if key != 'STONE':
                functions[key](pair)
    time.sleep(0.1)
