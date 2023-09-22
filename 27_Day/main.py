import tkinter


def miles_to_km():
    input = float(user_input.get())
    output = round(input * 1.609344, 3)
    change_lable.config(text=output)


windows = tkinter.Tk()
windows.title("my first gui program")
windows.minsize(width=200, height=100)
windows.config(padx=20, pady=20)

# lable
is_qual_to_lable = tkinter.Label()
is_qual_to_lable.config(text="is equal to")
is_qual_to_lable.grid(column=0, row=1)

# lable
miles_lable = tkinter.Label()
miles_lable.config(text="Miles")
miles_lable.grid(column=2, row=0)

# lable
km_lable = tkinter.Label()
km_lable.config(text="km")
km_lable.grid(column=2, row=1)

# lable
change_lable = tkinter.Label()
change_lable.config(text="0")
change_lable.grid(column=1, row=1)

# button
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)

#input
user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)










windows.mainloop()
