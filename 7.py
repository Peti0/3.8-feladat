import turtle
ablak=turtle.Screen()
ablak.bgcolor("green")
Kalóz=turtle.Turtle()
Kalóz.shape("turtle")
Kalóz.color("brown")

nezesirany=0
szögek = [160, -43, 270, -97, -43, 200, -940, 17,-86]
for x in szögek:
    nezesirany=nezesirany+x
    print("A kalóz ennyit fordul: ", x)
    if x>0:
        Kalóz.left(x)
    else:
        Kalóz.right(x)
    Kalóz.forward(100)
print("A kalóz nézésének iránya:", nezesirany)