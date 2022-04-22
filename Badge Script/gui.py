from cProfile import label
from cgitb import text
from fileinput import filename
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter.tix import COLUMN
from turtle import left
from PIL import Image, ImageTk
from unicodedata import name
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import PySimpleGUI as sg

root= Tk() #Creates window
root.configure(bg="#FABF98")

def Validated():
  if(firstNameField.get() == ""):
    sg.Popup("Need to enter a first name!")
    return False
  if(lastNameField.get() == ""):
    sg.Popup("Need to enter a last name!")
    return False
  if(jobPositionField.get() == ""):
    sg.Popup("Need to enter a job position!")
    return False
  try:
    var = float(employeeIDField.get())
    if(len(employeeIDField.get())==0 or len(employeeIDField.get())>9):
      sg.Popup("Employee Id needs to between 9 digits")
      return False
  except:
    sg.Popup("Need to enter a a valid employee number!")
    return False
  if(locationField.get() == ""):
    sg.Popup("Need to enter a location!")
    return False
  try:
    img = Image.open(ppath[0])
  except:
    sg.Popup("Profile photo needs to be an image")
    return False
  try:
    img = Image.open(cpath[0])
  except:
    sg.Popup("Corporate logo photo needs to be an image")
    return False
  return True

#Function that executes when button is clicked
def myClick():
    
    if(Validated()):
      #Takes values from GUI and puts them into variables to store the data
      name = firstNameField.get() +" "+ lastNameField.get()
      jobPosition = jobPositionField.get()
      employeeID = employeeIDField.get()
      location = locationField.get()
      pfp_path = ppath[0]
      businesslogo = cpath[0]

      #Opens the base badge and stores it in a object
      img = Image.open('Base Badges/Base Badge3.png') 

      #Opens the profile picture and stores it in a object
      pfp = Image.open(pfp_path)

      #Opens company logo and stores it in a object
      lp = Image.open(businesslogo)

      #Creates Object that allows the manipulation of image
      modImage = ImageDraw.Draw(img)


      #Sets font and size of text
      nameFont = ImageFont.truetype('fonts/RADLEY-REGULAR.TTF',28)
      positionFont = ImageFont.truetype('fonts/RADLEY-REGULAR.TTF',16)
      employeeIdNumberFont = ImageFont.truetype('fonts/CLEARSANS-REGULAR.TTF',12)
      barcodeFont = ImageFont.truetype('fonts/FRE3OF9X.TTF',55)


      #Creates text using inputed field data and places it on the badge based off coordinates
      modImage.text((281,145), name, anchor="ms", font=nameFont, fill=(0,0,0)) 
      modImage.text((281,168), jobPosition, anchor="ms", font=positionFont, fill=(255,0,0))
      modImage.text((281,225), employeeID, anchor='ms', font=barcodeFont, fill=(0,0,0))
      modImage.text((98,48), employeeID, font=employeeIdNumberFont, fill=(255,255,255))
      modImage.text((76,33), location, font=employeeIdNumberFont, fill=(255,255,255))

      #Resizes personal profile picture to fit the badge
      pfp = pfp.resize((123,148), Image.ANTIALIAS)


      #Resizes company logo to fit the badge 
      lp = lp.resize((80,80), Image.ANTIALIAS)


      
      img.paste(pfp, (26,76)) #Places pfp image based off coordinates
      img.paste(lp, (310,28)) #Places corprate logo image based off coordinates
      img.save('Created Badges/doneBadge.png',quality=95)

      img.show() #Shows badge picture

    


ppath = [0] #Stores path of profie picture
cpath = [0] #Stores path of corprate logo

def upload_file(kindOfPic):
    f_types = [('PNG File', '*.png')] #Sets the file explorer to look for png images
    filename = filedialog.askopenfilename(filetypes=f_types) #Opens file explorer and allows user to upload image and filename stores the image path
    if(kindOfPic=="pPic"):
      ppath[0] = filename
      #Label that shows files path
      uploadPFPTextLabel["text"] = "* "+filename

        
    if(kindOfPic=="CPlogo"):
        cpath[0] = filename
        #Label that shows files path
        uploadCorporatePhotoTextLabel["text"] = "* "+filename



#Creating Widgets
frame1 = LabelFrame(root, padx=50, pady=50, labelanchor='n', bg="#FABF98")
firstNameLabel = Label(frame1, text="First Name:", bg="#FABF98")
lastNameLabel = Label(frame1, text="Last Name:", bg="#FABF98")
jobPositionLabel = Label(frame1, text="Job Position:", bg="#FABF98")
employeeIDLabel = Label(frame1, text="Employee ID:", bg="#FABF98")
firstNameField = Entry(frame1, width=15, bg="#F5EAD5")
lastNameField = Entry(frame1, width=15, bg="#F5EAD5")
jobPositionField = Entry(frame1, width=15, bg="#F5EAD5")
employeeIDField = Entry(frame1, width=15, bg="#F5EAD5")
locationFieldLabel = Label(frame1, text="Location:", bg="#FABF98")
locationField = Entry(frame1, width=15, bg="#F5EAD5")
l1 = tk.Label(frame1,text='Profile Picture:', bg="#FABF98") #Profile Picture Label
#Upload File Button for Profile Picture
b1 = tk.Button(frame1, text='Upload File', 
   width=10,command = lambda:upload_file('pPic')) #Lambda runs the function only when Clicked
l2 = tk.Label(frame1,text='Corporate Logo:', bg="#FABF98")  #Corporate Picture Label
#Upload file button for Corporate Logo
b2 = tk.Button(frame1, text='Upload File', 
  width=10,command = lambda:upload_file('CPlogo')) 
uploadPFPTextLabel = tk.Label(frame1,fg="#F00A42", bg="#FABF98")
uploadCorporatePhotoTextLabel = tk.Label(frame1,fg="#F00A42", bg="#FABF98")


#Places frame
frame1.pack(padx=10, pady=10)


#Places widgits on window relative to frame:

firstNameLabel.grid(column=0, row=0) #First Name 
firstNameField.grid(column=1, row=0)


lastNameLabel.grid(column=0, row=1) #Last Name 
lastNameField.grid(column=1, row=1)


jobPositionLabel.grid(column=0, row=2) #Job Position
jobPositionField.grid(column=1, row=2)

employeeIDLabel.grid(column=0, row=3) #EmployeeID
employeeIDField.grid(column=1, row=3)

locationFieldLabel.grid(column=0, row=4)
locationField.grid(column=1, row=4)

uploadPFPTextLabel.grid(column=4,row=1, sticky='w', pady=(0,15))
uploadCorporatePhotoTextLabel.grid(column=4,row=3, sticky='w', pady=(0,15))

#Upload File Button for Profile Picture
b1.grid(column=3, row=1, padx=(15,0), pady=(0,15))

#Label for Profile Picture Button
l1.grid(column=3, row=0, padx=(15,0))

#Label for Corporate Logo Button
l2.grid(column=3, row=2, padx=(25,0))

#Upload file button for Corporate Logo
b2.grid(column=3, row=3, padx=(15,0), pady=(0,15))


#Command runs a function 
btnCreate = Button(frame1, text="Create",command=myClick, width=10)
btnCreate.grid(column=0,row=5, pady=(10,0))


#Set a loop that will keep window open until user exits the window
root.mainloop()