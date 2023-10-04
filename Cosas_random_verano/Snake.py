import turtle
import time
import random
posponer = 0.1  #Va a ir a una milesima de segundo moviendose de pixel en pixel
#Configuracion de la ventana
score = 0
high_score = 0

ven = turtle.Screen()
ven.title("Juego serpiente")
ven.bgcolor("black")
ven.setup(width=600, height=600)
ven.tracer(0)

#Crear la serpiente
cabeza = turtle.Turtle()  #Con esto creamos un objeto
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup() #Esto es para que cuando el objeto se mueve no deje ningun rastro
cabeza.goto(0,0) #Aparece en el centro de la pantalla
cabeza.direction = "stop" #Esta es la posicion inicial que va a tomar la caeza luego con el subprograma se ira modificando
#Comida
comida = turtle.Turtle()  #Con esto creamos un objeto
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup() #Esto es para que cuando el objeto se mueve no deje ningun rastro
comida.goto(150,0) #Aparece en el centro de la pantalla
#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score:0       High score:0",align= "center", font=("Courier",24,"normal"))
#Texto 2
texto2 = turtle.Turtle()
texto2.speed(0)
texto2.color("white")
texto2.penup()
texto2.hideturtle()
texto2.goto(0,150)

segmentos = [] #Creo una lista en la que voy añadiendo los segmentos de la culebra
color = ["red","blue","orange","green","purple"]
#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor() #Muestra la cordenada cuando avanza
        cabeza.sety(y + 20) #Se va a ir moviendo de 20 pixeles en 20
    elif cabeza.direction == "down":
        y = cabeza.ycor() #Muestra la cordenada cuando avanza
        cabeza.sety(y - 20) #Se va a ir moviendo de 20 pixeles en 20
    elif cabeza.direction == "left":
        x = cabeza.xcor() #Muestra la cordenada cuando avanza
        cabeza.setx(x - 20) #Se va a ir moviendo de 20 pixeles en 20
    elif cabeza.direction == "right":
        x = cabeza.xcor() #Muestra la cordenada cuando avanza
        cabeza.setx(x + 20) #Se va a ir moviendo de 20 pixeles en 20


#teclado
ven.listen() #Para que haga caso
ven.onkeypress(arriba, "Up")
ven.onkeypress(abajo, "Down")
ven.onkeypress(izquierda, "Left")
ven.onkeypress(derecha, "Right")
while True:
    ven.update() #Como que lo ejecuta y lo actauliza ña ventana
    texto2.clear()
    #Colisiones con los bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280  or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1) #Le damos una prada el juego ya que hemos perdido
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        #Esconder el segmento
        for i in segmentos:
            i.goto(100000,20000)
        #Limpiar los segmentos
        segmentos.clear()
        score = 0
        texto.clear()
        texto.write(f"Score:{score} High score:{high_score}", align="center", font=("Courier", 24, "normal"))

    mov()
    #Colisione cuerpo a cuerpo
    for i in segmentos:
        if i.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            #Esconder los segmentos
            for i in segmentos:
                i.goto(100000,200000)
            segmentos.clear()
            texto2.clear()
            texto2.write("Vuelvelo a intentar anda crack", align="center",
                         font=("Courier", 19, "normal"))

    if cabeza.distance(comida) < 20: #20 por que es el tamaño de la cabeza de la serpiente y de la comida y cuando ese tamaño
#sea menor de 20 significara que ha habido contacto entre ambas
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        nuevo_segmento = turtle.Turtle()  #Con esto creamos un objeto
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color(random.choice(color))
        nuevo_segmento.penup() #Esto es para que cuando el objeto se mueve no deje ningun rastro
        nuevo_segmento.goto(0,0) #Aparece en el centro de la pantalla
        segmentos.append(nuevo_segmento)

        score += 10
        if score > high_score:
            high_score = score
        texto.clear()
        texto.write(f"Score:{score}     High score:{high_score}",align= "center", font=("Courier",24,"normal"))


    totalseg = len(segmentos)
    for i in range(totalseg-1,0,-1):
        x = segmentos[i-1].xcor()
        y = segmentos[i-1].ycor()
        segmentos[i].goto(x,y)
    if totalseg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    time.sleep(posponer)