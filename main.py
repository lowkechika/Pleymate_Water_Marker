import tkinter.messagebox
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk, ImageOps, ImageEnhance
from tkinter import filedialog, simpledialog

window = Tk()
window.title('Pleymate Watermarker')

# resolution
window.geometry("700x700")
window.maxsize(width=700, height=700)

# window.config(background="white")

image = ''
watermark = ''
main_image_selected = False
inserting_watermark_is_active = False
saving_image = False

size = (650, 650)
mark_size = (150, 150)


# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////

# functions
def pick_image():
    global image, main_image_selected
    image = filedialog.askopenfilename()
    main_image_selected = True
    # print(image)
    check_image()
    print(type(watermark))


def check_image():
    global image, watermark
    if main_image_selected:
        try:

            panel.forget()
            our_image = Image.open(image)
            our_image = our_image.convert('RGBA')
            if not saving_image:
                our_image = ImageOps.contain(our_image, size)
                our_image = ImageTk.PhotoImage(our_image)

                if not inserting_watermark_is_active:
                    panel.config(image=our_image)
                    panel.image = our_image
                else:
                    our_image.paste(watermark)
                    panel.config(image=our_image)
                    panel.image = our_image
            else:
                our_image.paste(watermark)
                image_name = simpledialog.askstring(title='Naming File', prompt="Enter file name with ie myfile.png")
                our_image.save(f'{image_name}', format="png")

        except FileNotFoundError:
            tk.messagebox.showwarning(title="Error", message='Image Not Found!!')
    else:
        tk.messagebox.showwarning(title='Error', message='Must Load Image First!')


def select_watermark():
    global watermark
    # giving option to choose your watermark
    open_watermark = filedialog.askopenfilename()
    watermark = Image.open(open_watermark)
    watermark = ImageOps.contain(watermark, mark_size)
    watermark = watermark.convert('RGBA')
    watermark.putalpha(128)


def check_file_status():
    global inserting_watermark_is_active
    inserting_watermark_is_active = True
    check_image()


def save_image():
    global saving_image
    saving_image = True
    check_image()


# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////

get_image = Button(window, text="Load Image", command=pick_image)
get_image.grid(row=2, column=0)

insert_watermark = Button(window, text="Choose Watermark Image", command=select_watermark)
insert_watermark.grid(row=2, column=1)

insert_watermark = Button(window, text="Insert Watermark", command=check_file_status)
insert_watermark.grid(row=2, column=2)

insert_watermark = Button(window, text="Save Image", command=save_image)
insert_watermark.grid(row=2, column=3)

# Labels
panel = Label(window)  # display main image
panel.grid(row=0, columnspan=4)

mark_panel = Label(window)  # display watermark
mark_panel.grid(row=0, columnspan=4)
print(type(watermark))

window.mainloop()
