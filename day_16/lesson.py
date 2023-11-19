# from turtle import Turtle, Screen

# my_turtle = Turtle()
# my_screen = Screen()


# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         my_turtle.color(c)
#         my_turtle.forward(steps)
#         my_turtle.right(30)
        
# my_turtle.shape("turtle")
# my_turtle.color("orange")
# my_turtle.width(4)
# my_turtle.forward(100)
# my_turtle.left(-90)
# my_turtle.forward(100)
# my_turtle.right(270)
# my_turtle.forward(100)
# my_turtle.home()
# print(my_turtle.pos())
# my_screen.clearscreen()

# my_turtle.mainloop()
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
  [
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"],
  ]
)
print(table)
