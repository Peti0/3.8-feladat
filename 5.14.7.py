import turtle

def oszlop(t, magasság):
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.forward(magasság)
    t.write(" "+ str(magasság))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(magasság)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)

ablak= turtle.Screen()
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()

Eszti.color("blue", "red" )
Eszti.pensize(3)


xs = [48,117,200,240,160,260,220]

for m in xs:
    oszlop(Eszti, m)

ablak.mainloop()