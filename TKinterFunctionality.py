import tkinter as tk
from tkinter import Label
from tkinter import filedialog
<<<<<<< HEAD
from tkinter import *
from PIL import Image,ImageTk

## Function for Uploading Images

def imageUploader():
    fileTypes = [("Image Files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes = fileTypes)
    global pic
=======
from PIL import Image,ImageTk

## Function for Uploading Images
def imageUploader():
    fileTypes = [("Image Files", "*.png;*.jpg;*.jpeg")]
    path = tk.filedialog.askopenfilename(filetypes = fileTypes)
>>>>>>> main

    if len(path):
        img = Image.open(path)
        ## Automatically sizes the dimensions of the image when uploading sono scaling issues
        width,height = img.size
        img = img.resize((width,height))
        pic = ImageTk.PhotoImage(img)

<<<<<<< HEAD
        
        canvas.create_image(width/2, height/2, image=pic, anchor="center")
=======
        app.geometry("1280x960")
        label.config(image=pic)
        label.image = pic
        label.place(x=50, y=50)
>>>>>>> main
            
    else:
        print("No file chose. Please select a file.")

<<<<<<< HEAD
   


=======
>>>>>>> main
if __name__ == "__main__":

    app = tk.Tk()
    app.title("LBCC ROV Photo Software")
    app.geometry("1280x960")
    app.configure(bg="#333333")
<<<<<<< HEAD

    app.option_add("*Label*Background","white")
    app.option_add("*Button*Background","lightgreen")

    uploadButton = tk.Button(app, text="Locate Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM)

    #drawButton =tk.Button(app, text="Mark Points", command=draw_line)
    #drawButton.pack(side=tk.BOTTOM)



    canvas = Canvas(app, width=1280, height=960)
    canvas.pack()
    click_num=0

    ## Function for drawing line between two points
    # def draw_line(event):
    #     global click_num
    #     global x1, y1
    #     global x2, y2

    # if click_num==0:
    #     x1=event.x
    #     y1=event.y
    #     click_num=1
    # else:
    #     x2=event.x
    #     y2=event.y   
    # app.create_line(x1,y1,x2,y2, fill="green", width=5)  
    #canvas.bind('<Button-1>', draw_line)
    def paint( event ):
        x1, y1 = ( event.x - 1 ), ( event.y - 1 )
        x2, y2 = ( event.x + 1 ), ( event.y + 1 )
        canvas.create_oval( x1, y1, x2, y2, fill = "black" )
    canvas.bind( "<B1-Motion>", paint )

        
=======
    
    app.option_add("*Label*Background","white")
    app.option_add("*Button*Background","lightgreen")

    label = tk.Label(app)
    label.pack(pady=10)

    uploadButton = tk.Button(app, text="Locate Image", command=imageUploader)
    uploadButton.pack(side=tk.BOTTOM,pady=20)
>>>>>>> main

    app.mainloop()


