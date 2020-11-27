from tkinter import *
import random, copy, time
from threading import Thread

wx = 900
wy = 900
size = 3
dx = wx // size
dy = wy // size

mmap = [[random.randint(0, 1) for y in range(dy)] for x in range(dx)]
window = Tk()
cav = Canvas(window, width = wx, height = wy, bg = 'black')
cav.pack()
mainalive = True

def getColor(x, y):
    if mmap[x][y] == 1:
        return 'white'
    elif mmap[x][y] == 0:
        return 'black'
    else:
        pass

def setColor():
    cav.delete('all')
    tmap = copy.deepcopy(mmap)
    for x in range(dx):
        for y in range(dy):
            sum = 0
            if x - 1 >= 0 and y - 1 >= 0 and tmap[x - 1][y - 1] == 1:
                sum += 1
            if y - 1 >= 0 and tmap[x][y - 1] == 1:
                sum += 1
            if x + 1 < dx and y - 1 >= 0 and tmap[x + 1][y - 1] == 1:
                sum += 1
            
            if x - 1 >= 0 and tmap[x - 1][y] == 1:
                sum += 1
            if x + 1 < dx and tmap[x + 1][y] == 1:
                sum += 1
            
            if x - 1 >= 0 and y + 1 < dy and tmap[x - 1][y + 1] == 1:
                sum += 1
            if y + 1 < dy and tmap[x][y + 1] == 1:
                sum += 1
            if x + 1 < dx and y + 1 < dy and tmap[x + 1][y + 1] == 1:
                sum += 1
            if sum == 3:
                mmap[x][y] = 1
                cav.create_rectangle(x * size, y * size, x * size + size, y * size + size, fill = 'white')
            elif sum == 2:
                if tmap[x][y] == 1:
                    cav.create_rectangle(x * size, y * size, x * size + size, y * size + size, fill = 'white')
                continue
            else:
                mmap[x][y] = 0
    cav.update()

for x in range(dx):
    for y in range(dy):
        cav.create_rectangle(x * size, y * size, x * size + size, y * size + size, fill = getColor(x, y))

def stop(event):
    mainalive = False

def run(event):
    mainalive = True
    while mainalive:
        setColor()

cav.bind('<Button-1>', run)
cav.bind('<Button-3>', stop)
window.mainloop()