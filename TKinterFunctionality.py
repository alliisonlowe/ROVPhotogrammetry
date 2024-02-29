import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from PIL import Image,ImageTk



def imageUploader():
    fileTypes = [("Image Files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes = fileTypes)

    if len(path):
        img = Image.open(path)
        print(path)
        img = img.resize((200,200))
        pic = ImageTk.PhotoImage(img)

        app.geometry("960x720")
        label.config(image=pic)
        label.image = pic
            
    else:
        print("No file chose. Please select a file.")

if __name__ == "__main__":

    app = tk.Tk()
    app.title("LBCC ROV Photo Software")
    app.geometry("960x720")

    img=ImageTk.PhotoImage(file="vikingLogo.jpeg")
    imgLabel = Label(app, image=img)
    imgLabel.place(x=0,  y=0)

    
    app.option_add("*Label*Background","white")
    app.option_add("*Button*Background","lightgreen")

    label = tk.Label(app)
    label.pack(pady=10)

    uploadButton = tk.Button(app, text="Locate Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM,pady=20)

    app.mainloop()


