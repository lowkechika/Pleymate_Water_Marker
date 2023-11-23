import tkinter.messagebox
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk, ImageOps
from tkinter import filedialog

window = Tk()
window.title('Pleymate Watermarker')

# resolution
window.geometry("700x700")
window.resizable(width=True, height=True)
window.config(background="white")

image = ''

size = (650, 650)
mark_size = (300, 300)


# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////

# functions
def pick_image():
    global image
    image = filedialog.askopenfilename()
    # print(image)
    check_image()


def check_image():
    try:
        panel.forget()
        our_image = Image.open(image)
        our_image = ImageOps.contain(our_image, size)
        our_image = ImageTk.PhotoImage(our_image)
        panel.config(image=our_image)
        panel.image = our_image

    except FileNotFoundError:
        tk.messagebox.showwarning(title="Error", message='Image Not Found!!')


def watermark():
    mark_panel.forget()
    # giving option to choose your watermark
    your_watermark = filedialog.askopenfilename()

    your_mark = Image.open(your_watermark)
    your_mark.convert("RGBA")
    your_mark = ImageOps.contain(your_mark, mark_size)

    your_mark = ImageTk.PhotoImage(your_mark)

    # mark label
    mark_panel.config(image=your_mark,)
    mark_panel.image = your_mark


# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////

get_image = Button(window, text="Load Image", command=pick_image)
get_image.grid(row=2, column=1)

insert_watermark = Button(window, text="Insert Watermark", command=watermark)
insert_watermark.grid(row=2, column=2)

# Labels
panel = Label(window)  # display main image
panel.grid(row=0, columnspan=4)

mark_panel = Label(window)  # display watermark
mark_panel.grid(row=0, columnspan=4)


window.mainloop()
