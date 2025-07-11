#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle

t = turtle.Pen()

turtle.bgcolor("black")

colors = ["red", "yellow", "purple", "white","blue", "green", "orange", "brown", "gray", "pink" ]
family = []
name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end:")

while name != "":
    family.append(name)
    name = turtle.textinput("My family", "Enter a name, or just hit [ENTER] to end:")

for x in range(100):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold") )
    t.left(360/len(family) + 2)