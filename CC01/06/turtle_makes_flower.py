import turtle

def draw_square(some_turtle):
  for i in range(1,3):
    some_turtle.right(120)
    some_turtle.forward(100)
    some_turtle.right(60)
    some_turtle.forward(100)




def draw_art():
  window = turtle.Screen()
  window.bgcolor("white")

  # draw flower
  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("purple")
  brad.speed(10)
  for i in range(1,73):
    draw_square(brad)
    brad.right(5)

  brad.right(90)
  brad.forward(300)

  window.exitonclick()

draw_art()