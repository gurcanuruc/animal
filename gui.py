from tkinter import *
from tkinter import filedialog

#from tkinter.ttk import *

def browse_file():
    file = filedialog.askopenfile(mode="r",
                                  filetypes=[('Photos', '*.png'),
                                            ('Photos', '*.jpeg'),
                                            ('Photos', '*.jpg')])
    if file:
        print("Choosen file: ", file.name)
        file.close()
    else:
        print("No file choosen.")
    

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
           command=browse_file,
           )
sticker.pack(pady="20")
btn.pack(pady="100")

window.mainloop()