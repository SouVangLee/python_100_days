import tkinter

window = tkinter.Tk()
window.title("GUI App")
window.minsize(width=500, height=300)
# Add padding around window
window.config(padx=20, pady=20)


# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
my_label.config(text="Another New Text")
# my_label.pack()

# Use place to put in very specific coords
# my_label.place(x=100, y=200)

# Use grid for flexibility
my_label.grid(column=0, row=1)


# Button


def button_clicked():
    my_label.config(text=input.get())


button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=3, row=2)

# Entry
input = tkinter.Entry(width=50)
# input.pack()
input.grid(column=4, row=4)

window.mainloop()
