from turtle import Turtle
import pandas as pd

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.state_list = []
        
    def add_state(self, state_name, x_cor, y_cor):
        new_state = Turtle()
        new_state.penup()
        new_state.color("black")
        new_state.hideturtle()
        new_state.setpos(x_cor, y_cor)
        new_state.write(state_name, move=False, align="left", font=("Sans Serif", 10, "normal"))
        self.state_list.append(state_name)
        
    def save_to_csv(self):
        state_dict = { "state_names": self.state_list }
        state_data = pd.DataFrame(state_dict)
        state_data.to_csv("state_data.csv")
        