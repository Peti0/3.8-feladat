import turtle

ablak=turtle.Screen()
ablak.bgcolor("lightgreen")
Eszti=turtle.Turtle()
Eszti.shape("turtle")
Eszti.color("blue")

for i in range(1,13):
    Eszti.penup()
    Eszti.forward(100)
    Eszti.pendown()
    Eszti.forward(20)
    Eszti.penup()
    Eszti.forward(15)
    Eszti.stamp()
    Eszti.backward(135)
    Eszti.right(30)

    print("Itt éles a duma m")
    

ablak.mainloop() 