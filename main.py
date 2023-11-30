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
watermark_image_present = False
inserting_watermark_is_active = False
saving_image = False

size = (650, 650)
mark_size = (150, 150)


# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////

# functions
def pick_image():
    global image, main_image_selected, saving_image
    saving_image = False
    image = filedialog.askopenfilename()
    main_image_selected = True
    # print(image)
    check_image()


def check_image():
    global image, watermark
    if main_image_selected:
        try:

            panel.forget()
            our_image = Image.open(image)
            # our_image = our_image.convert('RGBA')
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
                save_as = filedialog.asksaveasfilename(filetypes=[('png file', '.png'), ('jpeg file', '.jpg')],
                                                       defaultextension='.png')

                try:
                    our_image.save(f'{save_as}')
                except ValueError:
                    not_saving = tk.messagebox.askyesnocancel(title='Aborting',
                                                              message='Do you wish to cancel your save?')
                    print(not_saving)
                    if not not_saving:
                        save_image()
                    else:
                        tk.messagebox.showwarning(title='Abort Success', message='Image save Aborted successfully!')
                else:
                    tk.messagebox.showwarning(title='Success', message='Image saved successfully!')

        except FileNotFoundError:
            tk.messagebox.showwarning(title="Error", message='Image Not Found!!')
    else:
        tk.messagebox.showwarning(title='Error', message='Must Load Image First!')


def select_watermark():
    global watermark, watermark_image_present
    watermark_image_present = True
    # giving option to choose your watermark
    open_watermark = filedialog.askopenfilename()
    watermark = Image.open(open_watermark)
    watermark = ImageOps.contain(watermark, mark_size)
    # watermark = watermark.convert('RGBA')
    watermark.putalpha(128)


def insert_watermark():
    global inserting_watermark_is_active
    inserting_watermark_is_active = True
    if watermark_image_present:
        check_image()
    else:
        tk.messagebox.showwarning(title='Error', message='Must Load Watermark Image First!')


def save_image():
    global saving_image
    saving_image = True
    check_image()


# //////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////

get_image = Button(window, text="Load Image", command=pick_image)
get_image.grid(row=2, column=0)

choose_watermark_image = Button(window, text="Choose Watermark Image", command=select_watermark)
choose_watermark_image.grid(row=2, column=1)

insert_watermark_image = Button(window, text="Insert Watermark", command=insert_watermark)
insert_watermark_image.grid(row=2, column=2)

save_watermarked_image = Button(window, text="Save Image", command=save_image)
save_watermarked_image.grid(row=2, column=3)

# Labels
panel = Label(window)  # display main image
panel.grid(row=0, columnspan=4)

mark_panel = Label(window)  # display watermark
mark_panel.grid(row=0, columnspan=4)

window.mainloop()
