#!/usr/bin/env python3
# -*- coding: utf-8 -*-

problem = input("Enter a math problem, or 'q' to quit and 'h' for help: ")

while(problem != "q"):
    if(problem == "h"):
        print(""" + is addition, - is subtraction, * is multiplication, / is division, ** is exponent and () is grouping""")
        problem = input("Enter another math problem, or 'q' to quit and 'h' for help: ")
    else:
        print("The answer to", problem, "is:", eval(problem) )
        problem = input("Enter another math problem, or 'q' to quit and 'h' for help: ")