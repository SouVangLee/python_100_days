from turtle import Turtle

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.state_list = []
        
    def add_state(self, state, x_cor, y_cor):
        new_state = Turtle()
        new_state.penup()
        new_state.color("black")
        new_state.write(state)
        self.state_list.append(new_state)
        