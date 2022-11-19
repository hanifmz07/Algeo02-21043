# import tkinter
# import kivy
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import time
# from identification import *
import os

fileName = 'notOpen'
folderName = 'notOpen'

widthPic = 512
heightPic = 512
bg = '#081643'
bgBlock = bg
bgBlock2 = bg
titleColor ='#3d85c6'
Cblock = '#4a7c9f'
CWrite = '#e6e6fa'
CBlock2 = '#191970'
CWrite2 = ''
CBlock3 = ''
CBright = '#d6ebff'
CDark = '#00407b'

NoPersonImg = "Tubes2-Algeo\\Algeo02-21043\\noPerson.png"
ImgTest = NoPersonImg
ImgResult = NoPersonImg

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
    global folderName
    folderName = filedialog.askdirectory(initialdir="/", title="Choose a Dataset")
    if (os.path.isdir(folderName)):
        labelFolder.configure(text="Folder : " + os.path.basename(folderName), fg="green")

def AskFile():
    global fileName
    # AskFile.fileName = filedialog.askopenfilename(
    fileName = filedialog.askopenfilename(
        initialdir="/",
        title="Choose a file",
        filetypes=(("Image File (.jpg)", "*.jpg*"), ("All Files", "*.*")),
    )
    if (os.path.isfile(fileName)):
        labelFile.configure(text="File : " + os.path.basename(fileName), fg="green")
        imgChangeN = ImageTk.PhotoImage(Image.open(fileName).resize((widthPic, heightPic)))
        # labelFile.configure(text="File : " + os.path.basename(AskFile.fileName), fg="green")
        # imgChangeN = ImageTk.PhotoImage(Image.open(AskFile.fileName).resize((widthPic, heightPic)))

        # imgChange = imgChangeN.resize((350, 350))
        TestI.configure(image=imgChangeN)
        TestI.image = imgChangeN 

def Execution():
    start_time = time.time()
    # Menjalankan program
    
    # try:
    #     # folderDS = AskFolder.folderName
    #     dir = AskFile.fileName
    #     print(dir)
    #     print()
    #     # print(folderDS)
    #     # print()
    # except :
    #     print("belum input\n")
        
    if ((fileName != 'notOpen') and (folderName != 'notOpen')):
    # if (fileName != 'notOpen'):
        print("\nMenjalankan program")
        print("...................")
        print("Dataset      : " + folderName)
        print("Test image   : " + fileName)
        # program 
        
        
    else :
        print("belum input")
        
    timeFormat = time.time() - start_time
    timeExecution.configure(text=("{:0.2f}".format(timeFormat)))
    # Execute.configure(bg = Cblock)
    # timeExecution = Label(
    # fid, text=("{:0.2f}".format(timeFormat)), fg="green", font=("times", 14)

# Widgets
fid.title("FaceID")
fidLabel1 = Label(
    fid,
    text="FaceID - Face Recognition",
    font=("Forte", 50, "bold"),
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
    width=30,
    height=3,
    fg="red",
    bg=CBright,
    font=("times", 17)
)
labelFolder = Label(
    fid,
    text="You haven't choose a folder",
    width=30,
    height=3,
    fg="red",
    bg=CBright,
    font=("times", 17),
)
testImage = Label(fid, text="Test Image", bg=bgBlock, fg=CWrite, font=("times", 20))
ClosestResult = Label(fid, text="Closest Result", bg=bgBlock, fg=CWrite, font=("times", 20))
Result = Label(fid, text="Result", fg="white", font=("times", 17, "bold"), bg = CDark)
ResultBox = Label(fid, text="None", fg="White", font=("helvetica", 14), bg=CDark)
timeEx = Label(fid, text="Execution time :", bg=bgBlock2, fg=CWrite, font=("times", 20))
timeExecution = Label(fid, text="00.00", bg=bgBlock2, fg="lightgreen", font=("times", 20))

# print("--- %s seconds ---" % (time.time() - start_time))
# imgOpen =
TestImage = ImageTk.PhotoImage(Image.open(ImgTest).resize((widthPic, heightPic)))
TestI = Label(image=TestImage, borderwidth=0.5, bg='dark blue')
TestResult = ImageTk.PhotoImage(Image.open(ImgResult).resize((widthPic, heightPic)))
TestR = Label(image=TestResult, borderwidth=0.5, bg='dark blue')

# Button
ChooseFolder = Button(
    fid,
    font=("helvetica", 14, "bold"),
    text="Choose a dataset",
    padx=25,
    pady=25,
    command=AskFolder,
    fg= CWrite,
    bg= Cblock,
    borderwidth=0
)
ChooseFile = Button(
    fid,
    font=("helvetica", 14, "bold"),
    text="Choose a picture",
    padx=25,
    pady=25,
    command=AskFile,
    fg= CWrite,
    bg= Cblock,
    borderwidth=0
)
Execute = Button(
    fid,
    text="Execute",
    fg=CWrite,
    padx=15,
    pady=15,
    command=Execution,
    font=("times", 17, "bold"),
    bg= CBlock2
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
ChooseFile.place(x=0.08 * width, y=0.450 * height, anchor=CENTER)
Execute.place(x=0.20 * width, y=0.580 * height, anchor=CENTER)

testImage.place(x=0.50 * width, y=0.200 * height, anchor=CENTER)
TestI.place(x=0.50 * width, y=0.500 * height, anchor=CENTER)
ClosestResult.place(x=0.80 * width, y=0.200 * height, anchor=CENTER)
TestR.place(x=0.80 * width, y=0.500 * height, anchor=CENTER)

timeEx.place(x=0.45 * width, y=0.800 * height, anchor=CENTER)
timeExecution.place(x=0.520 * width, y=0.800 * height, anchor=CENTER)

Result.place(x=0.08 * width, y=0.750 * height, anchor=CENTER)
ResultBox.place(x=0.10 * width, y=0.800 * height, anchor=CENTER)

fid.mainloop()

print("\nperintah ini akan print saat close program app nya\n")
print("Terima Kasih\n")