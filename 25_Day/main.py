import turtle
import pandas

# to get the cordinates on map
# def get_mouse_click_cord(x,Y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_cord)
# turtle.mainloop()


screen = turtle.Screen()
screen.title("U.S State Game")
image = r'25_Day\blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
gussed_state = []


while len(gussed_state) < 50:
    answer_state = screen.textinput(title=f"{len(gussed_state)}/50 State Correct", prompt="What's another state name?").title()

    data = pandas.read_csv(r"25_Day\50_states.csv")
    all_state = data.state.to_list()

    if answer_state == "Exit":
        missing_states = []
        for state in all_state:
            if state not in gussed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(r"25_Day\state_to_learn.csv", header=False)
        break
    if answer_state in all_state:
        gussed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int( state_data.y))
        t.write(answer_state)
