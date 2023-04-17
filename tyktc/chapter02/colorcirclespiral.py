#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle

t = turtle.Pen()
b = turtle.Screen()

b.bgcolor("black")

pencil = ["red", "green", "blue", "yellow"]

for x in range(100):
    t.color(pencil[x%4])
    t.circle(x)
    t.left(91)