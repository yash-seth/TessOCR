import pytesseract
import cv2
import numpy
import re
import time
import matplotlib.pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'

# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
import tkinter as tk
from tkinter import *

# import filedialog module
from tkinter import filedialog

# Function for opening the
# file explorer window
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("all files",
														"*.*"),
                                                        ("Text files",
														"*.txt*")
													))
	
	# Change label contents
	label_file_explorer.configure(text="File Opened: "+filename)
	outputOCR(filename)
	
																								
# Create the root window
window = Tk()

# Set window title
window.title('TessOCR')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 500
window_height = 500

x_coord = (screen_width/2) - (window_width/2)
y_coord = (screen_height/2) - (window_height/2)

# Set window size
window.geometry(f"{window_width}x{window_height}+{int(x_coord)}+{int(y_coord)}")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,
							text = "Select an image",
							width = 75, height = 4,
							fg = "blue")

	
button_explore = Button(window,
						text = "Browse Files",
						command = browseFiles)

button_exit = Button(window,
					text = "Exit",
					command = exit)

label_output_text = Text(window,
							width = 50, height = 15,
                            bg="white"
							)

label_output = Label(window,
							text = " Ouput:",
							width = 75, height = 2,
							bg = "white")							
# text_box = Text(
#     ws,
#     height=12,
#     width=40
# )
# text_box.pack(expand=True)
# text_box.insert('end', message)
# text_box.config(state='disabled')                            

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1,row = 3)
label_output.grid(column=1,row=4)
label_output_text.grid(column=1,row=5)

# Let the window wait for any events

def outputOCR(pathIMG):
    label_output_text.delete('1.0', END)
    #fileName = input('Input file name: ')
    pathIMG = pathIMG.encode('unicode-escape').decode()
    #pathIMG = fileName.encode('unicode-escape').decode()
    img = cv2.imread(pathIMG)
    #img = cv2.imread(fileName)
    bimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray =  cv2.threshold(bimg, 127, 255, cv2.THRESH_BINARY)
    # plt.imshow(bimg)
    # plt.show()
    words = pytesseract.image_to_string(img)
    #print(words)
    # label_output_text.configure(text=words)
    label_output_text.insert(tk.END,words)

window.mainloop()
