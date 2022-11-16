# import tkinter
# import kivy
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import time
import img
import os
import eigen as eg

widthPic = 450
heightPic = 450
bg = '#081643'
titleColor ='#3d85c6'

# SET UP window
fid = Tk()
width = fid.winfo_screenwidth()
height = fid.winfo_screenheight()
# fid.geometry("%dx%d" % (width, height))
fid.state('zoomed') 
#  pengaturan warna bg
fid['background'] = bg

# # Add image file
# bga = PhotoImage(file = "BG.jpg")
# # Create Canvas
# canvas1 = Canvas(fid)
# canvas1.pack(fill = "both", expand = True)
# # Display image
# canvas1.create_image( 0, 0, image = bga, 
#                      anchor = "nw")


# fid.geometry(f'{width}x{height}')
# fid.attributes('-fullscreen', True)
# fid.config(background="grey")
# bar = Frame(fid, bg="green", relief="raised", bd =5)
# bar.pack(expand=1, fill=X)

# Functions
def AskFolder():
    fiName = filedialog.askdirectory(initialdir="/", title="Choose a Dataset")

    labelFolder.configure(text="File : " + fiName, fg="green")


def AskFile():
    fiName = filedialog.askopenfilename(
        initialdir="/",
        title="Choose a file",
        filetypes=(("Image File (.jpeg)", "*.jpeg*"), ("All Files", "*.*")),
    )
    labelFile.configure(text="File : " + os.path.basename(fiName), fg="green")
    imgChangeN = ImageTk.PhotoImage(Image.open(fiName).resize((widthPic, heightPic)))

    # imgChange = imgChangeN.resize((350, 350))
    TestI.configure(image=imgChangeN)
    TestI.image = imgChangeN 


def Execution():
    start_time = time.time()
    # Menjalankan program

    timeFormat = time.time() - start_time
    timeExecution.configure(text=("{:0.2f}".format(timeFormat)))
    # timeExecution = Label(
    # fid, text=("{:0.2f}".format(timeFormat)), fg="green", font=("times", 14)

# Widgets
fid.title("FaceID")
NoPersonImg = "noPerson.png"
ImgTest = NoPersonImg
ImgResult = NoPersonImg
fidLabel1 = Label(
    fid,
    text="FaceID - Face Recognition",
    font=("Forte", 40, "bold"),
    justify="center",
    borderwidth=0,
    relief=SOLID,
    fg = titleColor,
    bg = bg
)
fidLabel2 = Label(
    fid, text="Tubes-Algeo02", font=("helvetica", 18),
    fg= titleColor, bg = bg
    )
labelFile = Label(
    fid,
    text="You haven't choose a file",
    width=50,
    height=3,
    fg="red",
    font=("times", 12),
)
labelFolder = Label(
    fid,
    text="You haven't choose a folder",
    width=50,
    height=3,
    fg="red",
    font=("times", 12),
)
testImage = Label(fid, text="Test Image", fg="black", font=("times", 13))
ClosestResult = Label(fid, text="Closest Result", fg="black", font=("times", 13))
Result = Label(fid, text="Result", fg="black", font=("times", 17, "bold"))
ResultBox = Label(fid, text="None", fg="blue", font=("helvetica", 14))
timeEx = Label(fid, text="Execution time :", fg="black", font=("times", 14))
timeExecution = Label(fid, text="00.00", fg="green", font=("times", 14))

# print("--- %s seconds ---" % (time.time() - start_time))
# imgOpen =
TestImage = ImageTk.PhotoImage(Image.open(ImgTest).resize((widthPic, heightPic)))
TestI = Label(image=TestImage)
TestResult = ImageTk.PhotoImage(Image.open(ImgResult).resize((widthPic, heightPic)))
TestR = Label(image=TestResult)

# Button
ChooseFolder = Button(
    fid,
    font=("helvetica", 12),
    text="Choose a dataset",
    padx=25,
    pady=25,
    command=AskFolder,
    fg="blue",
)
ChooseFile = Button(
    fid,
    font=("helvetica", 12),
    text="Choose a picture",
    padx=25,
    pady=25,
    command=AskFile,
    fg="blue",
)
Execute = Button(
    fid,
    text="Execute",
    fg="black",
    padx=15,
    pady=15,
    command=Execution,
    font=("times", 17, "bold"),
)


# Shoving it onto the screen
# fidLabel1.grid(row=0, column=10)
fidLabel1.place(
    x=0.5 * width, y=0.042 * height, anchor=CENTER
)  # bisa pakai rely or relx
# fidLabel1.pack(side=TOP)
fidLabel2.place(x=0.50 * width, y=0.080 * height, anchor=CENTER)
# fidLabel2.grid(row=15, column=)
labelFolder.place(x=0.25 * width, y=0.300 * height, anchor=CENTER)
# labelFolder.grid(row=10, column=10)
ChooseFolder.place(x=0.08 * width, y=0.300 * height, anchor=CENTER)
# ChooseFolder.grid(row=10, column=2)

labelFile.place(x=0.25 * width, y=0.450 * height, anchor=CENTER)
# labelFile.grid(row=15, column=10)
ChooseFile.place(x=0.08 * width, y=0.450 * height, anchor=CENTER)
# ChooseFile.grid(row=15, column=2)
Execute.place(x=0.20 * width, y=0.580 * height, anchor=CENTER)

testImage.place(x=0.50 * width, y=0.200 * height, anchor=CENTER)
TestI.place(x=0.50 * width, y=0.450 * height, anchor=CENTER)
ClosestResult.place(x=0.80 * width, y=0.200 * height, anchor=CENTER)
TestR.place(x=0.80 * width, y=0.450 * height, anchor=CENTER)

timeEx.place(x=0.45 * width, y=0.700 * height, anchor=CENTER)
timeExecution.place(x=0.5 * width, y=0.700 * height, anchor=CENTER)

Result.place(x=0.08 * width, y=0.750 * height, anchor=CENTER)
ResultBox.place(x=0.10 * width, y=0.800 * height, anchor=CENTER)

fid.mainloop()
