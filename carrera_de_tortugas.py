import turtle
import random

s = turtle.Screen()
s.title("Carrera de tortugas")

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

jugador1.shape("turtle")
jugador1.color("red", "red")

jugador2.shape("turtle")
jugador2.color("blue", "blue")

jugador1.goto(-200, 200)
jugador2.goto(-200, -200)

turtle.done()
