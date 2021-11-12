import turtle
import random

s = turtle.Screen()
s.title("Carrera de tortugas")
s.bgcolor("gray")

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("red", "red")
jugador1.shapesize(2, 2, 2)
jugador1.pensize(3)

jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("blue", "blue")
jugador2.shapesize(2, 2, 2)
jugador2.pensize(3)

jugador1.penup()
jugador1.goto(200, 100)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-200, 140)
jugador1.pendown()
jugador1.showturtle()

jugador2.penup()
jugador2.goto(200, -100)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-200, -60)
jugador2.pendown()
jugador2.showturtle()

dado = (1, 2, 3, 4, 5, 6)

for i in range(20) :
    if jugador1.pos() >= (160, 100) :
        print("la tortuga roja ha ganado")
        break
    elif jugador2.pos() >= (160, -100) :
        print("la tortuga azul ha ganado")
        break
    else :
        turno1 = input("Presione la tecla Enter para avanzar la tortuga roja: ")
        turno1 = random.choice(dado)
        print("tu numero es: ",turno1,"\nAvanzas: ",turno1*20)
        jugador1.pendown()
        jugador1.forward(20*turno1)
        
        turno2 = input("Presione la tecla Enter para avanzar la tortuga azul: ")
        turno2 = random.choice(dado)
        print("tu numero es: ",turno2,"\nAvanzas: ",turno2*20)
        jugador2.pendown()
        jugador2.forward(20*turno2)

turtle.done()
