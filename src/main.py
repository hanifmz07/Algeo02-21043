# import tkinter
# import kivy
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from identification import *
import os
# from multiprocessing import Process

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
train_dataset_condition = False
dataset_img = []
average_face = []
normal = []
covariance = []
eig_vec = []
eig_val = []
eig_vec_img = []

bg = '#071102'
bgBlock = '#0b2000'
bgBlock2 = '#0b2000'
titleColor ='#306615'
Cblock = '#224612'
CWrite = '#bdd4b1'
CBlock2 = '#0b2000'
CBright = '#1e453e'
CDark = '#110a4c'
red = '#bc0f0f'

# pengaturan background
# fid['background'] = bg
bgOpen = ImageTk.PhotoImage(Image.open(Background).resize((width, height)))
bg_fid = Label(fid, image = bgOpen)
bg_fid.place(height=height, width=width)


'''------------------------------------------ Functions ------------------------------------------'''

def refreshPartial():
    global train_dataset_condition
    timeExecution.configure(text=00.00)
    ResultBox.configure(text='None', fg=red)
    imgChangeN = ImageTk.PhotoImage(Image.open(NoPersonImg).resize((widthPic, heightPic)))
    TestR.configure(image=imgChangeN)
    TestR.image = imgChangeN
    ChooseFile.configure
    
def refresh():
    global train_dataset_condition
    timeExecution.configure(text=00.00)
    ResultBox.configure(text='None', fg=red)
    imgChangeN = ImageTk.PhotoImage(Image.open(NoPersonImg).resize((widthPic, heightPic)))
    TestR.configure(image=imgChangeN)
    TestR.image = imgChangeN
    ChooseFile.configure
    Train.configure(text="Train Dataset", fg=CWrite)
    train_dataset_condition = False

def SwitchCamera():
    global Camera_On, catch, TestI, cam
    refreshPartial()
    if(Camera_On):
        CamButton.configure(text="Camera off", fg=red)
        ChooseFile.configure(state=NORMAL)
        cam.place_forget()
        TestI.place(x=0.50 * width, y=0.500 * height, anchor=CENTER)
        catch.release()
        Camera_On=False
    else:
        CamButton.configure(text="Camera on", fg='green')
        ChooseFile.configure(state=DISABLED)
        TestI.place_forget()
        cam.place(x=0.50 * width, y=0.500 * height, anchor=CENTER, width=widthPic, height=heightPic, bordermode="ignore")
        catch = cv.VideoCapture(0) 
        displayCam()
        Camera_On=True

def displayCam():
    # menampilkan kamera 
   cvImg= cv.cvtColor(catch.read()[1], cv.COLOR_BGR2RGBA) 
   imageFromTK = ImageTk.PhotoImage(image = (Image.fromarray(cvImg)))
   cam.configure(image=imageFromTK)
   cam.imageFromTK = imageFromTK
   cam.after(15, displayCam)

def train_dataset():
    global folderName, train_dataset_condition, dataset_img, average_face, normal, covariance, eig_vec, eig_val, eig_vec_img
    if (train_dataset_condition):
        train_dataset_condition=False
        Train.configure(text="Train Dataset", fg = CWrite)
        # program mematikan train
        
    else:
        # program train a dataset
        if (os.path.isdir(folderName)):
            start = time.time()
            train_dataset_condition=True
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
            Train.configure(text="Dataset Trained", fg = 'green')
            timeExecution.configure(text=("{:0.2f}".format(time.time() - start)))
        else:
            print("belum input dataset")

def AskFolder():
    global folderName
    refresh()
    folderName = filedialog.askdirectory(initialdir="/", title="Choose a Dataset")
    if (os.path.isdir(folderName)):
        labelFolder.configure(text="Folder : " + os.path.basename(folderName), fg=CWrite)
    else :
        labelFolder.configure(text="None", fg=red)

def AskFile():
    global fileName
    refreshPartial()
    fileName = filedialog.askopenfilename(
        initialdir="/",
        title="Choose a file",
        filetypes=(("Image File (.jpg)", "*.jpg*"), ("All Files", "*.*")),
    )
    if (os.path.isfile(fileName)):
        labelFile.configure(text="File : " + os.path.basename(fileName), fg=CWrite)
        imgChangeN = ImageTk.PhotoImage(Image.open(fileName).resize((widthPic, heightPic)))
        TestI.configure(image=imgChangeN)
        TestI.image = imgChangeN 
    else :
        labelFile.configure(text="None", fg=red)

def Execution():
    global fileName, folderName, dataset_img, average_face, normal, covariance, eig_vec, eig_val, eig_vec_img
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
            if (not train_dataset_condition) :
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

            idx = identification(test_img, average_face, normal, eig_vec_img.T)
            print("Identification image DONE")
            
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
            result, imgCam = catch.read()
            print("Dataset      : " + folderName)         
            fileName = imgCam 
                
            # program
            print(fileName.shape)
            
            test_img = preprocessPhoto(fileName)
            
            print("Preprocess test image DONE")
            
            if (not train_dataset_condition) :
                dataset_img = preprocess(folderName)
                print("Preprocess dataset DONE")
                average_face = face_avg(dataset_img)
                print("Mean dataset DONE")
                normal = normalized_face(dataset_img, average_face)
                print("Normal dataset DONE")
                covariance = covariance_mat(normal)
                print("Covariance dataset DONE")
                eig_val, eig_vec = eig_val_and_vec(covariance)
                eig_vec_img = normal.T @ eig_vec
                
            idx = identification(test_img, average_face, normal, eig_vec_img.T)
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

'''------------------------------------------ Widgets ------------------------------------------ '''

fid.title("FaceIT")

cam = Label(fid, borderwidth=0, width=widthPic, height=heightPic,  anchor=CENTER, bg='black')

fidLabel1 = Label(
    fid,
    text="FaceIT - Face Recognition",
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
    fg="#e44949",
    bg=CBright,
    font=("times", 17)
)
labelFolder = Label(
    fid,
    text="You haven't choose a folder",
    width=widthLF,
    height=heightLF,
    # fg="#FFCCCB",
    fg="#e44949",
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
Train = Button(
    fid,
    text="Train Dataset",
    fg=CWrite,
    padx=padxButtonExc,
    pady=padyButtonExc,
    command=train_dataset,
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
)

# Shoving it onto the screen
fidLabel1.place(x=0.5 * width, y=0.045 * height, anchor=CENTER)  # bisa pakai rely or relx
fidLabel2.place(x=0.50 * width, y=0.106 * height, anchor=CENTER)
labelFolder.place(x=0.26 * width, y=0.300 * height, anchor=CENTER)
ChooseFolder.place(x=0.1 * width, y=0.300 * height, anchor=CENTER)

labelFile.place(x=0.26 * width, y=0.450 * height, anchor=CENTER)
ChooseFile.place(x=0.1 * width, y=0.450 * height, anchor=CENTER)
Execute.place(x=0.295 * width, y=0.580 * height, anchor=CENTER)
Train.place(x=0.195 * width, y=0.580 * height, anchor=CENTER)
CamButton.place(x=0.095 * width, y=0.580 * height, anchor=CENTER)

testImage.place(x=0.5 * width, y=0.200 * height, anchor=CENTER)
TestI.place(x=0.5 * width, y=0.500 * height, anchor=CENTER)
ClosestResult.place(x=0.8 * width, y=0.200 * height, anchor=CENTER)
TestR.place(x=0.8 * width, y=0.500 * height, anchor=CENTER)

timeEx.place(x=0.45 * width, y=0.800 * height, anchor=CENTER)
timeExecution.place(x=0.520 * width, y=0.800 * height, anchor=CENTER)

Result.place(x=0.08 * width, y=0.700 * height, anchor=CENTER)
ResultBox.place(x=0.10 * width, y=0.750 * height, anchor=CENTER)

fid.mainloop()

print("\nperintah ini akan print saat close program app nya\n")
print("Terima Kasih\n")