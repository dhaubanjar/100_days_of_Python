import random
from turtle import Turtle, Screen

joey = Turtle()
screen = Screen()

""" Extracted rgb code from a hurst painting using colorgram, a python package"""
colors_list = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]
screen.colormode(255)
joey.speed("fastest")               # sets speed to the fastest
joey.shape("arrow")
joey.penup()                        # unset the line drawing
joey.setheading(225)                # goes 225 degree down
joey.forward(500)                   # goes forward 500
joey.setheading(0)                  # turns back
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    joey.dot(40, random.choice(colors_list))
    joey.forward(80)
    if dot_count % 10 == 0:         # makes sure only 10 dots
        joey.setheading(90)         # changes direction to left
        joey.forward(80)
        joey.setheading(180)        # goes backward
        joey.forward(800)           # goes full length forward to repeat drawing from left
        joey.setheading(0)



screen.exitonclick()