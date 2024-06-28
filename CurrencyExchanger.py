import os
from currency_data import exchange_rates, available_currencies
from tkinter import Tk, Canvas, Entry, Text, Button, Label, PhotoImage
from tkinter.ttk import Combobox
from tkinter import messagebox

def load_asset(path: str):
    return os.path.join(os.getcwd(), "assets", "frame0", path)


def convert_currency():
    from_currency = from_combobox.get()
    to = to_combobox.get()
    _amount = amount.get()
    if from_currency is not None and to is not None:
        if from_currency in exchange_rates and to in exchange_rates[from_currency]:
            try:
                rate = exchange_rates[from_currency][to]['rate']
                converted_amount = float(_amount) * float(rate)
                result.config(text=f"{round(converted_amount, 3)} {to}")
                return converted_amount
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "No data available for conversion!")
    else:
        messagebox.showerror("Error", "Provide the required values.")


window = Tk()

window.geometry("865x610")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 610,
    width = 866,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    38,
    35,
    anchor="nw",
    text="Currency Converter",
    fill="#0365D7",
    font=("KulimPark SemiBold", -36)
)

canvas.create_text(
    77,
    114,
    anchor="nw",
    text="From",
    fill="#000000",
    font=("KulimPark SemiBold", -24)
)

canvas.create_text(
    84,
    455,
    anchor="nw",
    text="Result",
    fill="#000000",
    font=("KulimPark SemiBold", -24)
)

canvas.create_text(
    478,
    114,
    anchor="nw",
    text="To",
    fill="#000000",
    font=("KulimPark SemiBold", -24)
)

image_image_1 = PhotoImage(
    file=load_asset("image_1.png"))
image_1 = canvas.create_image(
    232,
    175,
    image=image_image_1
)

from_combobox = Combobox(window, values=available_currencies, width=23, height=20, font=("KulimPark SemiBold", -24))
from_combobox.place(x=70, y=157)

image_image_2 = PhotoImage(
    file=load_asset("image_2.png"))
image_2 = canvas.create_image(
    633,
    175,
    image=image_image_2
)

to_combobox = Combobox(window, values=available_currencies, width=23, height=20, font=("KulimPark SemiBold", -24))
to_combobox.place(x=472, y=157)

image_image_3 = PhotoImage(
    file=load_asset("image_3.png"))
image_3 = canvas.create_image(
    432,
    271,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=load_asset("entry_1.png"))
entry_bg_1 = canvas.create_image(
    515,
    271,
    image=entry_image_1
)
amount = Entry(
    bd=0,
    bg="#DFDCDC",
    fg="black",
    font=("KulimPark SemiBold", -30),
    highlightthickness=0
)
amount.place(
    x=238,
    y=241,
    width=566,
    height=58,
)

button_image_1 = PhotoImage(
    file=load_asset("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: convert_currency(),
    relief="flat"
)
button_1.place(
    x=260,
    y=337,
    width=350,
    height=80
)

image_image_4 = PhotoImage(
    file=load_asset("image_4.png"))
image_4 = canvas.create_image(
    432,
    516,
    image=image_image_4
)

result = Label(
    window,
    anchor="nw",
    text="",
    font=("KulimPark SemiBold", -33),
    bg="#EFEBEB"
)
result.place(x=340,y=493)

window.resizable(False, False)
window.mainloop()
