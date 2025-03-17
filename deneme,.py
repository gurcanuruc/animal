from tkinter import *
#from tkinter.ttk import *

def button_clicked():
    print("bunun yerine pencere açılıp fotoğraf seçilecek")

window=Tk()

window.title("Animal Recognizer") 
window.geometry("800x600")
window.resizable(width=False, height=False)
sticker=Label(window , text = "Please import an image to recognize which animal is.",
              fg="gray",
              font="Arial 20 bold",
              )
tus=Button(window, text ="Choose an image",
           fg="black",
           font="Arial 10 bold",
           cursor = "hand2",
           anchor= "center",
           command=button_clicked,
           )
sticker.pack()
tus.pack()

window.mainloop()