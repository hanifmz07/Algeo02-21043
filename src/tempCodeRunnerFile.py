k.PhotoImage(Image.open(ImgTest).resize((widthPic, heightPic)))
TestI = Label(image=TestImage, borderwidth=0.5, bg='dark blue')
TestResult = ImageTk.PhotoImage(Image.open(ImgResult).resize((widthPic, heightPic)))
TestR = Label(image=