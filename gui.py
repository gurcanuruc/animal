from tkinter import *
#from tkinter.ttk import *

def button_clicked():
    print("bunun yerine pencere açılıp fotoğraf seçilecek")

window=Tk()

window.title("Animal Recognizer") 
window.geometry("800x600")
window.resizable(width=False, height=False)
window.configure(bg="#262626")
sticker=Label(window , text = "Please import an image to recognize which animal is.",
              fg="gray",
              bg ="#262626",
              font="Arial 20 bold",
              )

btn=Button(window, text ="Choose an image",
           fg="black",
           font="Arial 20 bold",
           bg ="#424242",
           cursor = "hand2",
           anchor= "center",
           command=button_clicked,
           )
sticker.pack(pady="20")
btn.pack(pady="100")

window.mainloop()