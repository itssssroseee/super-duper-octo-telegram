import turtle as t


# Function to draw a star with a name

def draw_star(size,color,name):
    t.penup()
    t.setposition(50,50)
    t.pendown()
    angle = 144
    
    # We Set the fill color and filling in the star
    t.fillcolor(color)
    t.begin_fill()

    # draws the star
    for i in range(5):
        t.forward(size)
        t.right(angle)
        t.forward(size)
        t.right(72-angle)

    t.end_fill()
    
    # set name position 
    t.setposition(20,0)

    # write the name
    t.write(name, align = "center")
    


def main():
    draw_star(100, "gold", "Rose N.")
    t.mainloop()


if __name__ == "__main__": 
    main()
