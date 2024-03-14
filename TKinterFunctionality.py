import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import math
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
        self.canvas.grid(row=0, column=0, sticky=tk.NSEW)

        self.pixel_length = 0
        self.ratioLength = 0

        # Create and add the button to upload the image
        self.upload_button = tk.Button(self, text="Locate Image", command=self.image_uploader)
        self.upload_button.grid(row=1, column=0, pady=20)

        # Create and add the button to set scale for conversion
        self.scale_button = tk.Button(self, text="Set Scale", command=self.set_conversionx)
        self.scale_button.grid(row=0, column=1, pady=20, padx=10)

        # Create and add the button to measure coral reef in pixels to convert to cm
        self.convert_button = tk.Button(self, text="Measure Coral Reef", command=self.pixel_to_cm)
        self.convert_button.grid(row=1, column=1, pady=30, padx=10)

        # Add a row and column configuration for the grid
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        #Creating Points for Drawing a line
        self.points = []
        self.canvas.bind("<Button-1>", self.on_click_disabled)


    def image_uploader(self):
        file_types = [("Image Files", "*.png;*.jpg;*.jpeg")]
        path = filedialog.askopenfilename(filetypes=file_types)

        if len(path):
            self.img = Image.open(path)
            self.width, self.height = self.img.size
            self.width = self.width *3
            self.height = self.height*3
            self.img = self.img.resize((self.width, self.height))
            self.pic = ImageTk.PhotoImage(self.img)

            self.canvas.delete("image")
            self.canvas.create_image(0, 0, image=self.pic, anchor="nw", tag="image")
            self.canvas.config(width=self.width, height=self.height)


            # Update the window size to match the canvas size
            self.geometry(f"{self.width}x{self.height}")

        # In event of no image selected then an error prompt is displayed
        else:
            messagebox.showerror("Error", "No file was selected. Please select a file.")
    
    def on_click_disabled(self, event):
        pass
    
    def on_click(self, event):
        self.points.append((event.x, event.y))
        
        if len(self.points) == 2:
            x1, y1 = self.points[0]
            x2, y2 = self.points[1]

            self.canvas.create_line(x1, y1, x2, y2, fill="red")
            self.pixel_length = self.calculate_pixel_length(x1, y1, x2, y2)
            print(f"Pixel Length: {self.pixel_length}")

            self.points = []

    def calculate_pixel_length(self, x1, y1, x2, y2):
            print("Before Swapping, x1: ", x1, "x2: ", x2, "y1: ", y1, "y2: ", y2)
            if x1 > x2:
                temp = x1
                x1 = x2
                x2 = temp
            elif y1 > y2:
                temp = y1
                y1 =y2
                y2=temp
            else:
                pass
            print("After Swapping, x1: ", x1, "x2: ", x2, "y1: ", y1, "y2: ", y2)

            pixel_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            return pixel_length


    def set_conversionx(self):
        length_conversion = self.pixel_length
        user_input_cm = None
        while user_input_cm is None:
            user_input_cm = float(input("Enter the length in centimeters: "))
            if user_input_cm is float:
                break
            else:
                continue
             
        self.canvas.bind("<Button-1>", self.on_click)
        # Get user input for length in centimeters
        # Calculate the ratio of pixels per centimeter
        self.ratioLength = length_conversion / user_input_cm
        print(self.ratioLength)
        self.canvas.unbind("<Button-1>")

    def set_conversiony(self):
        height_conversion = self.pixel_length
        user_input_cm = None
        while user_input_cm is None:
            user_input_cm = float(input("Enter the length in centimeters: "))
            if user_input_cm is float:
                break
            else:
                continue
            
        self.canvas.bind("<Button-1>", self.on_click)
        # Get user input for length in centimeters
        # Calculate the ratio of pixels per centimeter
        self.ratioWidth = height_conversion / user_input_cm
        print(self.ratioWidth)
        self.canvas.unbind("<Button-1>")
        

    def pixel_to_cm(self):
        print("THIS IS MY CONVERSION BUTTON")
        #self.ratio_x = pixels_x/cm_x
        
        #self.ratio_y = pixels_y/cm_y

        #button to start conversion if measured_x and measured y is taken
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()