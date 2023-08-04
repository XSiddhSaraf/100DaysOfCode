import turtle

import pandas as pd

screen = turtle.Screen()
screen.title('U.S. State Gamees')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

state_data_df = pd.read_csv('50_states.csv')
states = state_data_df["state"].to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states answered", prompt="What's another state name?")
    answer = answer_state.title()
    print(answer)

    if answer == 'Exit':
        missing_state = []
        for i in states:
            if i not in guessed_state:
                missing_state.append(i)
        print(missing_state)
        missing_df = pd.DataFrame(missing_state)
        missing_df.to_csv('Missed states while guissing.csv')
        break
    if answer in states:
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data_cor = state_data_df[state_data_df["state"] == answer]
        t.goto(int(state_data_cor["x"]), int(state_data_cor["y"]))
        t.write(answer)

screen.exitonclick()
