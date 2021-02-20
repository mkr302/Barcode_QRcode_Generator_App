# Barcode/QR code Generator (GUI) Application - Python/Tkinter
    A GUI application for generating Barcode/QR code and to save the code as a PNG file.
    
#### What types of codes are generated:
     Barcode (EAN13):
            The International Article Number (also known as European Article Number or EAN) is a standard describing a barcode symbology and numbering system used in global trade to identify a specific retail product type, in a specific packaging configuration, from a specific manufacturer.

     QR code:
             A QR code (abbreviated from Quick Response code) is a type of matrix barcode (or two-dimensional barcode) first designed in 1994 for the automotive industry in Japan. A barcode is a machine-readable optical label that contains information about the item to which it is attached. In practice, QR codes often contain data for a locator, identifier, or tracker that points to a website or application. 

###### To read more on EAN13 --> https://en.wikipedia.org/wiki/International_Article_Number
###### For more on QR codes --> https://en.wikipedia.org/wiki/QR_code


#### Dependencies:
          Py Version: 3.x
          Packages:   tkinter, barcode, datetime, pyqrcode, PIL, time
          
#### Application Walkthrough:
        - The GUI App generates both EAN13 Barcodes and QR codes. 
        - Use the respective input text boxes to enter the values which needs to be converted to Bar/QR codes.
        
        - The layout of the GUI App is shown below - 
<p align="center">
    <img src="/demo_pic1.png" alt="Bar/QR code generator demo" width="350" title="Bar/QR code generator App">
</p>

        - Samples of QR and Bar codes generated given below - 

#### BAR CODE (EAN13)
<p align="center">
    <img src="/EAN_barcode_19022021210438.png" alt="Bar/QR code generator demo" width="350" title="Bar/QR code generator App">
</p>

#### QR CODE
<p align="center">
    <img src="/QR_code_19022021211651.png" alt="Bar/QR code generator demo" width="350" title="Bar/QR code generator App">
</p>


#### Features of the Application
        - Extensive user input validation
        - EAN13 Bar code input requires only numeric inputs and of length not exceeding 13
        - NULL inputs are ignored by the application.
        - The code is saved as a PNG file and also opened soon after the creation

## Instructions on how to use the Application code:

	Please refer the instructions at the {WIKI} section: https://github.com/mkr302/Barcode_QRcode_Generator_GUI_App-Python_Tkinter/wiki
