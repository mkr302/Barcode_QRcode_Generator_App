# ##########################################################################################################
# # Program:    Barcode_QRcode_Generator_GUI_App-Python_Tkinter_v1.0.py
# # Purpose:    GUI application for generating Barcode/QR code and to save the code as a PNG file
# # Author:     Muralikrishnan Rajendran
# # Date:       21-Jul-2020
# # Dependencies:
#        Py Version: 3.x
#        Packages:   tkinter, barcode, datetime, pyqrcode, PIL, time
# ##########################################################################################################

### libraries utilized
import barcode
from barcode.writer import ImageWriter
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import pyqrcode
from pyqrcode import QRCode
import png
from PIL import ImageTk, Image
from time import sleep

# print(barcode.PROVIDED_BARCODES)
# Tkinter window initialization
BarQRWin = tk.Tk()

#Tkinter elements initialization
textbox1 = tk.Text(BarQRWin, width=24, height=1.5, bd=5, bg='white', font = ("Helvetica", 10), relief ='raised')
textbox1.place(x=70,y=200)

myFont1 = font.Font(family='Helvetica', weight='bold')

btnbar_Set = tk.Button(BarQRWin, text="Generate Barcode", bd=5, width=15, height=2, bg="black", fg="white",
                       command=lambda:barcode())
btnbar_Set['font'] = myFont1
btnbar_Set.place(x = 80, y = 250)

textbox2 = tk.Text(BarQRWin, width=24, height=1.5, bd=5, bg='white', font = ("Helvetica", 10), relief ='raised')
textbox2.place(x=410,y=200)

btnqr_Set = tk.Button(BarQRWin, text="Generate QR code", bd=5, width=15, height=2, bg="black", fg="white",
                       command=lambda:qrcode())
btnqr_Set['font'] = myFont1
btnqr_Set.place(x = 420, y = 250)

separator1_style = ttk.Style()
separator1_style.configure("Line.TSeparator", bg="black")
separator1= ttk.Separator(BarQRWin, orient='horizontal')
separator1.place(x=0, y=350, height=20, width=695)

separator2= ttk.Separator(BarQRWin, orient='horizontal') 
separator2.place(x=0, y=580, width=695, height=20)

btnclr_Set = tk.Button(BarQRWin, text="Clear", bd=5, width=10, height=2, bg="orange", fg="black",
                       command=lambda:clearspace(textbox3))
btnclr_Set['font'] = myFont1
btnclr_Set.place(x = 450, y = 500)

textbox3 = tk.Text(BarQRWin, width=50, height=4, bd=5, bg='light blue', font = ("Helvetica", 12), relief ='raised')
textbox3.place(x = 100, y = 400)

btnclr1_Set = tk.Button(BarQRWin, text="Clear", width=5, height=1, bg="blue", fg="white",
                       command=lambda:clearspace(textbox1))
btnclr1_Set['font'] = myFont1
btnclr1_Set.place(x = 260, y = 200)

btnclr2_Set = tk.Button(BarQRWin, text="Clear", width=5, height=1, bg="blue", fg="white",
                       command=lambda:clearspace(textbox2))
btnclr2_Set['font'] = myFont1
btnclr2_Set.place(x = 600, y = 200)

textbox4 = tk.Text(BarQRWin, width=26, height=1, bg='light grey', font = ("Helvetica", 8), relief ='raised')
textbox4.config(highlightthickness = 0, borderwidth=0)
textbox4.place(x=50,y=583)
textbox4.insert('1.0', 'Copyright @ github.com/mkr302')
textbox4.configure(state='disabled')

image1 = "EAN_template_pic.png"

EAN_display_pic = ImageTk.PhotoImage(Image.open(image1))
EAN_display = tk.Label(BarQRWin, image = EAN_display_pic)
EAN_display.place(x = 80, y = 60)

image2 = "QR_template_pic.png"

QR_display_pic = ImageTk.PhotoImage(Image.open(image2))
QR_display = tk.Label(BarQRWin, image = QR_display_pic)
QR_display.place(x = 415, y = 60)


EAN = barcode.get_barcode_class('ean13')


def qrcode():
    
    """
    function to validate the user input and generate the
    QR code and save the code as png file
    """
    
    user_qrcode_input = textbox2.get("1.0","end").strip()
    if len(user_qrcode_input) == 0:
        textbox2.delete("1.0","end")
        textbox2.insert('1.0', "No inputs received!")
    else:
        qrcode_op = pyqrcode.create(user_qrcode_input)
        now = datetime.now().strftime("%d%m%Y%H%M%S")
        qr_file_name = "QR_code_{}.png".format(now)
        qrcode_op.png(qr_file_name, scale = 8)
        textbox2.delete("1.0","end")
        display_output("QR", "QR code is generated Successfully!", qr_file_name)

        
def display_output(code_name, op_str, file_name):
    
    """
    function to display the program execution message and also
    list the file name for the saved QR/Barcode
    """
    
    if code_name == 'QR':
        file_name = file_name
    else:
        file_name = '{}.png'.format(file_name)
    textbox3.delete("1.0","end")
    textbox3.insert('1.0', '\t{}{}{}'.format(op_str, "\n\n      Code is saved in file: ", file_name))
    im = Image.open(file_name)  
    im.show()


def barcode():
    
    """
    function to validate user input and generate
    EAN barcode, and also to save the code in a png file
    """
    
    user_barcode_input = textbox1.get("1.0","end").strip()
    if len(user_barcode_input) == 0:
        textbox1.delete("1.0","end")
        textbox1.insert('1.0', "No inputs received!")
    elif user_barcode_input.isdigit() and len(user_barcode_input) == 13:
        ean = EAN(user_barcode_input, writer=ImageWriter())
        now = datetime.now().strftime("%d%m%Y%H%M%S")
        ean_file_name = 'EAN_barcode_{}'.format(now)
        ean.save(ean_file_name)
#         # resizing the png file
#         img = Image.open('{}.png'.format(ean_file_name))
#         new_width  = 300
#         new_height = 150
#         img = img.resize((new_width, new_height), Image.ANTIALIAS)
#         img.save('{}.png'.format(ean_file_name))
        textbox1.delete("1.0","end")
        display_output("EAN", "EAN code generated successfully!", ean_file_name)
    elif user_barcode_input.isdigit() and len(user_barcode_input) != 13:
        textbox1.delete("1.0","end")
        textbox1.insert('1.0', "Less than 13 digits entered.")
    else:
        textbox1.delete("1.0","end")
        textbox1.insert('1.0', "Only digits allowed")

def clearspace(textboxn):
    
    """
    Clear the respective text boxes as per the click button
    """
    
    textboxn.delete("1.0","end")


###### Tkinter frame properties
        
# Title and size adjustments
BarQRWin.title('           BAR/QR CODE Generator App - USING PYTHON/TKINTER         ')
BarQRWin.geometry('695x600')
BarQRWin.resizable(0,0)
BarQRWin.configure(bg='burlywood')
BarQRWin.mainloop()


############################# END OF SCRIPTS ########################################