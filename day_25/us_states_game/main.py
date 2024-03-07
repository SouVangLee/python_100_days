import turtle
import pandas as pd
from states import States

screen = turtle.Screen()
screen.title("US States Game")
# Add gif as the shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_manager = States()

STATES_DATA = pd.read_csv("50_states.csv")
STATES_LIST = STATES_DATA.state.to_list()
# print("STATES_LIST", STATES_LIST)
continue_game = True
while continue_game:
    
    answer_state = screen.textinput(title=f"{0}/50 States Correct", prompt="What's another state's name?").capitalize()
    # print("answer_state", answer_state)
    if answer_state in STATES_LIST:
        state_data = STATES_DATA[STATES_DATA.state == answer_state]
        x_cor = state_data.x
        print("x_cOR", x_cor)
        # print("statee", state_data)
        # states_manager.add_state(answer_state)
        # print(states_manager)
        
        
    
    
turtle.mainloop()
