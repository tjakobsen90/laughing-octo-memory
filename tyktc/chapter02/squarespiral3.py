#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Draw a spiraling square

import turtle

t = turtle.Pen()

t.color("red")

for x in range(100):
    t.forward(x)
    t.left(91)
