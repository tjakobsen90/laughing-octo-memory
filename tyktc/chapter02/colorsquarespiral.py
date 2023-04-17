#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle

t = turtle.Pen()
b = turtle.Screen()

b.bgcolor("black")
pencil = ["red", "green", "blue", "yellow"]

for x in range(100):
    t.forward(x)
    t.pencolor(pencil[x%4])
    t.left(91)
    