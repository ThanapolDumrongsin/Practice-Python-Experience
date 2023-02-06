# from turtle import Turtle , Screen
# Ball = Turtle()
# Ball.shape("turtle")
# Ball.color("red")
# Ball.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name" , ["1","2"])
table.add_column("column2" , ["1","2"])

print(table)