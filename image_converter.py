"""
Image Conversion Application

This program creates a simple Tkinter-based GUI application for converting JPG images to either PNG or PDF format.

Dependencies:
- Tkinter for GUI
- Pillow (PIL) for image processing

Developed By: Karabo khunou

Usage:
- Run the script.
- Click the "Browse A File" button to select a JPG image.
- Click the "JPG_to_PNG" button to convert the selected JPG image to PNG format.
- Click the "JPG_to_PDF" button to convert the selected JPG image to PDF format.

Note: Converted files are saved as "sample1.png" or "sample1.pdf" in the current working directory.

"""

from tkinter import *
from tkinter import filedialog as fd
from PIL import Image

# Tkinter setup
root = Tk()
root.geometry("400x400")
root.title("Image_Conversion_App")

def jpg_to_png():
    """
    Convert selected JPG image to PNG format.

    Returns:
    None
    """
    filename = fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("sample1.png")
    else:
        Label_2 = Label(root, text="Error!", width=20, fg="red", font=("bold", 15))
        Label_2.place(x=80, y=280)

def jpg_to_pdf():
    """
    Convert selected JPG image to PDF format.

    Returns:
    None
    """
    filename = fd.askopenfilename()
    if filename.endswith(".jpg"):
        Image.open(filename).save("sample1.pdf", resolution=100.0)
    else:
        Label_2 = Label(root, text="Error!", width=20, fg="red", font=("bold", 15))
        Label_2.place(x=80, y=280)

# Labels and Buttons
Label_1 = Label(root, text="Browse A File", width=20, font=("bold", 15))
Label_1.place(x=80, y=80)

Label_3 = Label(root, text="</Developed By:-karabo/>", width=80, font=("bold", 8))
Label_3.place(x=10, y=365)

Button(root, text="JPG_to_PNG", width=20, height=2, bg="brown", fg="white", command=jpg_to_png).place(x=120, y=120)
Button(root, text="JPG_to_PDF", width=20, height=2, bg="brown", fg="white", command=jpg_to_pdf).place(x=120, y=220)

# Main event loop
root.mainloop()
