import turtle
import time
import random

posponer = 0.1

# crea una instancia de la clase Screen del módulo Turtle 
# y la almacena en la variable window.
window = turtle.Screen()
#Modifica el titulo de la ventana
window.title("Snake")
#Modifica el color background 
window.bgcolor("black")
#Modifica el tamaño de la ventana
window.setup(width= 600, height= 600)
#frames dede actualizacion
window.tracer(0)



"""
cabeza
Son las caracteristicas de la cabeza
"""
#una instancia de turtle para cabeza
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("circle")
cabeza.penup()
cabeza.goto(0,0)
cabeza.color("white")
cabeza.direction = "stop"


"""
comida
Son las caracteristicas de la cabeza
"""
#una instancia de turtle para comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0,100)
comida.color("red")
comida.direction = "stop"

""""
cuerpo
El cuerpo es una lista vacia
"""
segmentos = []


#funciones
def arriba():
    cabeza.direction = "up" 
def abajo():
    cabeza.direction = "down" 
def izquierda():
    cabeza.direction = "left" 
def derecha():
    cabeza.direction = "right" 

"""
Movimiento
"""
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)


#teclado
#toma las indicaciones por teclado
window.listen()
window.onkeypress(arriba,"Up")
window.onkeypress(abajo,"Down")
window.onkeypress(izquierda,"Left")
window.onkeypress(derecha,"Right")


while True:
    #actualiza continuamente la pantalla
    window.update()
    
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("circle")
        nuevo_segmento.penup()
        nuevo_segmento.goto(0,100)
        nuevo_segmento.color("grey")
        nuevo_segmento.direction = "stop"
        segmentos.append(nuevo_segmento)

    #mover el cuerpo
    total_Seg = len(segmentos)
    for index in range(total_Seg -1, 0, -1):
        x = segmentos[index -1].xcor()
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x,y)

    if total_Seg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

        
    mov()
    time.sleep(posponer)
