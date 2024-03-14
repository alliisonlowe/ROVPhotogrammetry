import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Application Setup
        self.title("LBCC Photogrammetry Software")
        self.geometry("1280x960")
        self.configure(bg="#333333")

        # Create and add the label to display the image
        self.width, self.height = 1280, 960
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create and add the button to upload the image
        self.upload_button = tk.Button(self, text="Locate Image", command=self.image_uploader)
        self.upload_button.pack(side=tk.BOTTOM, pady=20)

    def image_uploader(self):
        file_types = [("Image Files", "*.png;*.jpg;*.jpeg")]
        path = filedialog.askopenfilename(filetypes=file_types)

        if len(path):
            self.img = Image.open(path)
            self.width, self.height = self.img.size
            self.img = self.img.resize((self.width, self.height))
            self.pic = ImageTk.PhotoImage(self.img)

            self.canvas.delete("image")
            self.canvas.create_image(0, 0, image=self.pic, anchor="nw", tag="image")
            self.canvas.config(width=self.width, height=self.height)

        # In event of no image selected then an error prompt is displayed
        else:
            messagebox.showerror("Error", "No file was selected. Please select a file.")

if __name__ == "__main__":
    app = App()
    app.mainloop()

