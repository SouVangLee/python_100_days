import turtle
import pandas as pd
from states import States
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("US States Game")
# Add gif as the shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_manager = States()
scoreboard = Scoreboard()

STATES_DATA = pd.read_csv("50_states.csv")
STATES_LIST = STATES_DATA.state.to_list()
continue_game = True
while continue_game:
    
    answer_state = screen.textinput(title=f"{scoreboard.score}/50 States Correct", prompt="What's another state's name?").capitalize()
    
    if answer_state == "Exit":
        states_manager.save_to_csv()
        break
    
    if answer_state in STATES_LIST:
        state_data = STATES_DATA[STATES_DATA.state == answer_state]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        
        states_manager.add_state(state_name=answer_state, x_cor=x_cor, y_cor=y_cor)
        scoreboard.increase_score()
        
    if scoreboard.score == 50:
        continue_game = False
        scoreboard.game_over()
        
    
# turtle.mainloop()
