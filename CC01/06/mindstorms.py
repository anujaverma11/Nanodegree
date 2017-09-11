import turtle

def draw_square(some_turtle):
  for i in range(1,5):
    some_turtle.right(90)
    some_turtle.forward(100)

def draw_art():
  window = turtle.Screen()
  window.bgcolor("white")

  # create the turtle brad - Draws a Square
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("purple")
  brad.speed(2)

  # Call draw_square as many times as the number of squares you want.
  for i in range(1,37):
    draw_square(brad)
    brad.right(10)


  # create the turtle angie - draw circle
  angie = turtle.Turtle()
  angie.shape("arrow")
  angie.color("blue")
  angie.circle(100)

  window.exitonclick()

draw_art()