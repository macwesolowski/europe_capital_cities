import turtle
import pandas

ALIGNMENT = "center"
FONT_CITY = ("Lato", 8, "normal")
FONT_END = ("Lato", 18, "normal")

screen = turtle.Screen()
screen.setup(width=900, height=727)
screen.title("Europe Capital Cities Game")
image = "europe_map.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("capital-cities-europe.csv")
all_capitals = data.capital.to_list()
guessed_cap_cities = []

# How to find coordinates on the map:
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

while len(guessed_cap_cities) < 49:
    answer_city = screen.textinput(title=f"{len(guessed_cap_cities)}/49 Cities Correct",
                                   prompt="What's another capital city name? (Enter 'show' to forfeit): ")

    # user pressed the cancel button and we exit the program
    if answer_city == None:
        exit()
    else:
        answer_city = answer_city.title()

    if answer_city == "Show":
        missing_cities = []
        for capital in all_capitals:
            if capital not in guessed_cap_cities:
                missing_cities.append(capital)
                capital_data = data[data.capital == capital]
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.pencolor("red")
                t.goto(int(capital_data.x.iloc[0]), int(capital_data.y.iloc[0]))
                t.write(capital_data.capital.item(), font=FONT_CITY)
        new_data = pandas.DataFrame(missing_cities)
        new_data.to_csv("cities-to-learn.csv")
        break

    if answer_city in all_capitals:
        guessed_cap_cities.append(answer_city)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        capital_data = data[data.capital == answer_city]
        t.goto(int(capital_data.x.iloc[0]), int(capital_data.y.iloc[0]))
        t.write(answer_city, font=FONT_CITY)
        if len(guessed_cap_cities) == 49:
            t.pencolor("red")
            t.goto(13, 280)
            t.write(f"Congratulations! You know all the capital cities of Europe!",
                    align=ALIGNMENT, font=FONT_END)

screen.exitonclick()