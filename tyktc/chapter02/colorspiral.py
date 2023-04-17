#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle

t = turtle.Pen()
b = turtle.Screen()

b.bgcolor("black")
sides = 5
pencil = ["red", "green", "blue", "yellow", "purple", "orange"]

for x in range(360):
    t.pencolor(pencil[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)