import tkinter as tk
from tkinter import Label
from tkinter import filedialog
from PIL import Image,ImageTk

## Function for Uploading Images
def imageUploader():
    fileTypes = [("Image Files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes = fileTypes)

    if len(path):
        img = Image.open(path)
        ## Automatically sizes the dimensions of the image when uploading sono scaling issues
        width,height = img.size
        img = img.resize((width,height))
        pic = ImageTk.PhotoImage(img)

        app.geometry("1280x960")
        label.config(image=pic)
        label.image = pic
        label.place(x=50, y=50)
            
    else:
        print("No file chose. Please select a file.")

if __name__ == "__main__":

    app = tk.Tk()
    app.title("LBCC ROV Photo Software")
    app.geometry("1280x960")
    app.configure(bg="#333333")
    
    app.option_add("*Label*Background","white")
    app.option_add("*Button*Background","lightgreen")

    label = tk.Label(app)
    label.pack(pady=10)

    uploadButton = tk.Button(app, text="Locate Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM,pady=20)

    app.mainloop()


