#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import turtle

t = turtle.Pen()

turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]

for n in range(50):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    x = random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,turtle.window_height()//2)

t.penup()
t.setpos(x,y)
t.pendown()
for m in range(size):
    t.forward(m*2)
    t.left(91)