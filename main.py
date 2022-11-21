# import tkinter
# import kivy
from tkinter import *
from tkinter import filedialog
import cv2 as cv
import time
from PIL import ImageTk, Image
from identification import *
import os
from multiprocessing import Process

'''------------------------------------------ SET UP ------------------------------------------'''

fid = Tk()
width = fid.winfo_screenwidth()
height = fid.winfo_screenheight()
# fid.geometry("%dx%d" % (width, height))
print("%dx%d" % (width, height))
fid.state('zoomed') 


widthPic = (width * 100) // 375 
heightPic = (height * 100) // 211
padxButtonCam = width  // 128
padyButtonCam = height // 70
padxButtonExc = width  // 128
padyButtonExc = height // 70
padxCF = width // 90
padyCF = height //43
widthLF =  width // 75
heightLF = height // 360

fileName = 'notOpen'
folderName = 'notOpen'
NoPersonImg = "pictures\\noPerson2.jpeg"
BG = "pictures\\BG.jpg"
print("File location using os.getcwd():", os.getcwd())
NoPersonImg =  os.path.join(os.getcwd(), NoPersonImg)
Background = os.path.join(os.getcwd(), BG )
ImgTest = NoPersonImg
ImgResult = NoPersonImg
Camera_On = False
# print(width/widthPic)
# print(height/heightPic)
# print(width/padxButtonCam)
# print(height/padyButtonCam)
# print(width/padxButtonExc)
# print(height/padyButtonExc)
# print(width/padxCF)
# print(height/padyCF)
# print(width/widthLF)
# print(height/heightLF)

bg = '#071102'
bgBlock = '#0b2000'
bgBlock2 = '#0b2000'
titleColor ='#306615'
Cblock = '#274e13'
CWrite = '#bdd4b1'
CBlock2 = '#0b2000'
CBright = '#1e453e'
CDark = '#110a4c'
red = '#bc0f0f'

#  pengaturan warna bg
# fid['background'] = bg
bgOpen = ImageTk.PhotoImage(Image.open(Background).resize((width, height)))
bg_fid = Label(fid, image = bgOpen)
bg_fid.place(height=height, width=width)


'''------------------------------------------ Functions ------------------------------------------'''

def refresh():
    timeExecution.configure(text=00.00)
    ResultBox.configure(text='None', fg=red)
    imgChangeN = ImageTk.PhotoImage(Image.open(NoPersonImg).resize((widthPic, heightPic)))
    TestR.configure(image=imgChangeN)
    TestR.image = imgChangeN
    ChooseFile.configure

def SwitchCamera():
    global Camera_On, cap, TestI, cam
    refresh()
    if(Camera_On):
        CamButton.configure(text="Camera off", fg=red)
        ChooseFile.configure(state=NORMAL)
        cam.place_forget()
        TestI.place(x=0.50 * width, y=0.500 * height, anchor=CENTER)
        cap.release()
        Camera_On=False
    else:
        CamButton.configure(text="Camera on", fg='green')
        ChooseFile.configure(state=DISABLED)
        TestI.place_forget()
        cam.place(x=0.50 * width, y=0.500 * height, anchor=CENTER, width=widthPic, height=heightPic, bordermode="ignore")
        cap = cv.VideoCapture(0) 
        showFrame()
        Camera_On=True

def showFrame():
   # Get the latest frame and convert into Image
   cv2image= cv.cvtColor(cap.read()[1],cv.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgTK = ImageTk.PhotoImage(image = img)
   cam.imgTK = imgTK
   cam.configure(image=imgTK)
   # Repeat after an interval to capture continiously
   cam.after(20, showFrame)
   
def AskFolder():
    global folderName
    refresh()
    folderName = filedialog.askdirectory(initialdir="/", title="Choose a Dataset")
    if (os.path.isdir(folderName)):
        labelFolder.configure(text="Folder : " + os.path.basename(folderName), fg="green")
    else :
        labelFolder.configure(text="None", fg=red)

def AskFile():
    global fileName
    # AskFile.fileName = filedialog.askopenfilename(
    refresh()
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
    else :
        labelFile.configure(text="None", fg=red)

def Execution():
    global fileName, folderName
    start_time = time.time()
    
    # Menjalankan program
    if (not Camera_On):
        if (os.path.isfile(fileName) and os.path.isdir(folderName)):
            print("\nMenjalankan program dengan input file test image")
            print("...................")
            print("Dataset      : " + folderName)
            print("Test image   : " + fileName)
            
            # program 
            test_img = preprocessFile(fileName)
            print("Preprocess test image DONE")
            dataset_img = preprocess(folderName)
            print("Preprocess dataset DONE")
            average_face = face_avg(dataset_img)
            print("Mean dataset DONE")
            normal = normalized_face(dataset_img, average_face)
            print("normal dataset DONE")
            covariance = covariance_mat(normal)
            print("Covariance dataset DONE")
            eig_val, eig_vec = eig_val_and_vec(covariance)
            eig_vec_img = normal.T @ eig_vec

            # E_pred = np.empty((0, eig_vec_img.T.shape[1]), 'float64')
            # for i in range(int(eig_vec_img.T.shape[0]*0.3)):
            #     E_pred = np.append(E_pred, [eig_vec_img.T[i]], axis=0)

            idx = identification(test_img, average_face, normal, eig_vec_img.T)
            # idx = identification(test_img, average_face, normal, E_pred, dataset_img)
            print("Identification image DONE")
            
            # listFile = os.listdir(folderName)
            # fileResult = os.path.join(folderName, listFile[idx])
            
            fileR = listFileDataset[idx]
            imgResult = ImageTk.PhotoImage(Image.open(fileR).resize((widthPic, heightPic)))
            TestR.configure(image=imgResult)
            TestR.image = imgResult 
            
            resultName = (os.path.splitext(os.path.basename(fileR)))[0]
            resultNoInt = ''.join([i for i in resultName if not i.isdigit()])
            ResultBox.configure(text=resultNoInt, fg='light green' ) # perlu .
            print("hasil")
            print(idx)
            print(resultName)
            
        else :
            print("ada yang masih belum input")
    else:
        if (os.path.isdir(folderName)):
            print("\nMenjalankan program FaceID dengan kamera")
            print("...................")
            result, imgCam = cap.read()
            # imgCam = cv.resize(imgCam, (256,256)) 
            print("Dataset      : " + folderName)
            # print(imgCam)
            # fileName = cv.imresize() # ??
            # fileName = smart_resize(imgCam, 256 )            
            fileName = imgCam 
            # fileName = np.reshape(fileName, (256,256, 3))            
            # program
            print(fileName.shape)
            # cv.imwrite("nig.png", fileName)
            # cam.place(x=0.50 * width, y=0.500 * height, anchor=CENTER, width=widthPic, height=heightPic, bordermode="ignore")
            
            # cap = cv.VideoCapture(0) 
            
            test_img = preprocessPhoto(fileName)
            # timeExecution.configure(text=("{:0.2f}".format(time.time() - start_time)))
            # ResultBox.configure(text='Preprocess test image DONE', fg='light green' ) 
            print("Preprocess test image DONE")
            dataset_img = preprocess(folderName)
            # ResultBox.configure(text="Preprocess dataset DONE", fg='light green' ) 
            print("Preprocess dataset DONE")
            average_face = face_avg(dataset_img)
            # ResultBox.configure(text="Mean dataset DONE", fg='light green' ) 
            print("Mean dataset DONE")
            normal = normalized_face(dataset_img, average_face)
            # ResultBox.configure(text="Normal dataset DONE", fg='light green' ) 
            print("Normal dataset DONE")
            covariance = covariance_mat(normal)
            # ResultBox.configure(text="Covariance dataset DONE", fg='light green' ) 
            print("Covariance dataset DONE")
            eig_val, eig_vec = eig_val_and_vec(covariance)
            eig_vec_img = normal.T @ eig_vec
            idx = identification(test_img, average_face, normal, eig_vec_img.T)
            # ResultBox.configure(text='DONE', fg='light green') 
            print("Identification image DONE")
            
            fileR = listFileDataset[idx]
            imgResult = ImageTk.PhotoImage(Image.open(fileR).resize((widthPic, heightPic)))
            TestR.configure(image=imgResult)
            TestR.image = imgResult 
            
            resultName = (os.path.splitext(os.path.basename(fileR)))[0]
            resultNoInt = ''.join([i for i in resultName if not i.isdigit()])
            ResultBox.configure(text=resultNoInt, fg='light green' ) 
            print("hasil")
            print(idx)
            print(resultName)
            

        else :
            print("belum input dataset")
        
        
    timeExecution.configure(text=("{:0.2f}".format(time.time() - start_time)))
    # Execute.configure(bg = Cblock)
    # timeExecution = Label(
    # fid, text=("{:0.2f}".format(timeFormat)), fg="green", font=("times", 14)

'''------------------------------------------ Widgets ------------------------------------------ '''

fid.title("FaceID")

cam = Label(fid, borderwidth=0, width=widthPic, height=heightPic,  anchor=CENTER, bg='black')
# cap = cv.VideoCapture(0)

fidLabel1 = Label(
    fid,
    text="FaceID - Face Recognition",
    font=("Forte", 68, "bold"),
    justify="center",
    borderwidth=0,
    relief=SOLID,
    fg = titleColor,
    bg = bg
)
fidLabel2 = Label(
    fid, text="------------------------------------------------------ Tubes 2 Algeo ----------------------------------------------------", font=("helvetica", 18),
    fg= titleColor, bg = bg
    )
labelFile = Label(
    fid,
    text="You haven't choose a file",
    width=widthLF,
    height=heightLF,
    fg="#ed7878",
    bg=CBright,
    font=("times", 17)
)
labelFolder = Label(
    fid,
    text="You haven't choose a folder",
    width=widthLF,
    height=heightLF,
    # fg="#FFCCCB",
    fg="#ed7878",
    bg=CBright,
    font=("times", 17),
)
testImage = Label(fid, text="Test Image", bg=bgBlock, fg=CWrite, font=("times", 20))
ClosestResult = Label(fid, text="Closest Result", bg=bgBlock, fg=CWrite, font=("times", 20))
Result = Label(fid, text="Result", fg=CWrite, font=("times", 17, "bold"), bg = CDark)
ResultBox = Label(fid, text="None", fg=CWrite, font=("helvetica", 14), bg=CDark)
timeEx = Label(fid, text="Execution time :", bg=bgBlock2, fg=CWrite, font=("times", 20))
timeExecution = Label(fid, text="00.00", bg=bgBlock2, fg="lightgreen", font=("times", 20))

TestImage = ImageTk.PhotoImage(Image.open(NoPersonImg).resize((widthPic, heightPic)))
TestI = Label(image=TestImage, borderwidth=0, bg='dark blue')
TestResult = ImageTk.PhotoImage(Image.open(NoPersonImg).resize((widthPic, heightPic)))
TestR = Label(image=TestResult, borderwidth=0, bg='dark blue')

# Button
ChooseFolder = Button(
    fid,
    font=("helvetica", 14, "bold"),
    text="Choose a dataset",
    padx=padxCF,
    pady=padyCF,
    command=AskFolder,
    fg= CWrite,
    bg= Cblock,
    borderwidth=0
)
ChooseFile = Button(
    fid,
    font=("helvetica", 14, "bold"),
    text="Choose a picture",
    padx=padxCF,
    pady=padyCF,
    fg= CWrite,
    bg= Cblock,
    borderwidth=0,
    command=AskFile,  
)
Execute = Button(
    fid,
    text="Execute",
    fg=CWrite,
    padx=padxButtonExc,
    pady=padyButtonExc,
    command=Execution,
    font=("times", 17, "bold"),
    bg= CBlock2
)
CamButton = Button(
    fid,
    text="Camera",
    fg=CWrite,
    padx=padxButtonCam,
    pady=padyButtonCam,
    font=("times", 17, "bold"),
    bg= CBlock2,
    command=SwitchCamera,
    # cam.configure(x=0.50 * width, y=0.500 * height)
)

# Shoving it onto the screen
# fidLabel1.grid(row=0, column=10)
fidLabel1.place(
    x=0.5 * width, y=0.045 * height, anchor=CENTER
)  # bisa pakai rely or relx
# fidLabel1.pack(side=TOP)
fidLabel2.place(x=0.50 * width, y=0.106 * height, anchor=CENTER)
# fidLabel2.grid(row=15, column=)
labelFolder.place(x=0.26 * width, y=0.300 * height, anchor=CENTER)
# labelFolder.grid(row=10, column=10)
ChooseFolder.place(x=0.1 * width, y=0.300 * height, anchor=CENTER)
# ChooseFolder.grid(row=10, column=2)

labelFile.place(x=0.26 * width, y=0.450 * height, anchor=CENTER)
ChooseFile.place(x=0.1 * width, y=0.450 * height, anchor=CENTER)
Execute.place(x=0.20 * width, y=0.580 * height, anchor=CENTER)
CamButton.place(x=0.10 * width, y=0.580 * height, anchor=CENTER)

testImage.place(x=0.5 * width, y=0.200 * height, anchor=CENTER)
TestI.place(x=0.5 * width, y=0.500 * height, anchor=CENTER)
ClosestResult.place(x=0.8 * width, y=0.200 * height, anchor=CENTER)
TestR.place(x=0.8 * width, y=0.500 * height, anchor=CENTER)
# cam.place(x=0.50 * width, y=0.500 * height, anchor=CENTER)
# showFrame()

timeEx.place(x=0.45 * width, y=0.800 * height, anchor=CENTER)
timeExecution.place(x=0.520 * width, y=0.800 * height, anchor=CENTER)

Result.place(x=0.08 * width, y=0.700 * height, anchor=CENTER)
ResultBox.place(x=0.10 * width, y=0.750 * height, anchor=CENTER)

fid.mainloop()

print("\nperintah ini akan print saat close program app nya\n")
print("Terima Kasih\n")