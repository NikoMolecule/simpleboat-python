import turtle


s = turtle.getscreen()
t = turtle.Turtle()

t.speed(0)


s.title("ნავი")
s.bgcolor('LightSkyBlue')
s.setup(800, 500)

#ზღვა
t.pen(pensize=4, pencolor='MediumBlue', fillcolor='MediumBlue')

t.up()
t.goto(395, -240)

t.down()
t.begin_fill()
t.backward(793)
t.left(90)
t.forward(70)
t.right(90)
t.forward(793)
t.right(90)
t.forward(70)

t.end_fill()

#ნავის კორპუსი

t.pen(pensize=1, pencolor = 'SaddleBrown', fillcolor='SaddleBrown')

t.up()
t.goto(130, -167)

t.down()
t.begin_fill()
t.right(90)
t.forward(300)
t.right(60)
t.forward(75)
t.right(120)
t.forward(360)
t.right(120)
t.forward(75)
t.end_fill()

#იალქანი, დროშა.
t.pen(pensize=4, pencolor='White', fillcolor='White')
t.up()
t.goto(-180, -60)

t.down()
t.begin_fill()
t.left(120)
t.forward(310)
t.left(140)
t.forward(199.5)
t.left(79)
t.forward(201)
t.end_fill()


#იალქანი, მთავარი ჯოხი.
t.pen(pensize=1, pencolor='Black', fillcolor='Black')
t.up()
t.goto(-19, -103)

t.down()
t.begin_fill()
t.right(129)
t.forward(172)
t.left(90)
t.forward(7)
t.left(90)
t.forward(172)
t.end_fill()



#მზე

t.pen(pensize=1, pencolor='Yellow', fillcolor='Yellow')
t.up()
t.goto(-350,160)

t.down()
t.begin_fill()
t.circle(60)
t.end_fill()


#========================
t.hideturtle()
turtle.hideturtle()
turtle.done()