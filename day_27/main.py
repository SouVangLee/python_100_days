from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.maxsize(width=300, height=300)
window.config(padx=20, pady=20)


# Entry
input = Entry(width=10)
input.grid(row=0, column=1)

# "Miles" Label
miles = Label(text="Miles", font=("Arial", 12))
miles.grid(row=0, column=2)

# "is equal to" Label
is_equal_to = Label(text="is equal to", font=("Arial", 12))
is_equal_to.grid(row=1, column=0)

# converted Label
converted_value = Label(text="0", font=("Arial", 12))
converted_value.grid(row=1, column=1)

# Km Label
km = Label(text="Km", font=("Arial", 12))
km.grid(row=1, column=2)

def convert_miles_to_km():
    km_value = format(int(input.get()) * 1.60, '.2f')
    converted_value.config(text=f"{km_value}")
    

# Calculate button
calculate_btn = Button(text="Calculate", command=convert_miles_to_km)
calculate_btn.grid(row=2, column=1)




window.mainloop()
