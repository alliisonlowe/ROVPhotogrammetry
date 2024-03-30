import tkinter as tk
## Adding Testing Brach

root = tk.Tk()
root.geometry("800x500")
root.title("LBCC ImagePixel-Length Software")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=30)

## Can be sized any way and allow for scrolling text etc.
textbox = tk.Text(root,height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

## One Line Entry No scroll and limited
# myentry =tk.Entry(root)
# myentry.pack()

## Creating Buttons
# button = tk.Button(root, text="Click Me", font=('Arial', 18))
# button.pack(padx=10, pady=10)


##Grid Layouts inside of Packs
buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0,weight=1)
buttonFrame.columnconfigure(1,weight=1)
buttonFrame.columnconfigure(2,weight=1)

btn1=tk.Button(buttonFrame, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0,sticky=tk.W + tk.E)

btn2=tk.Button(buttonFrame, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1,sticky=tk.W + tk.E)

btn3=tk.Button(buttonFrame, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2,sticky=tk.W + tk.E)

buttonFrame.pack(fill='x')

anotherbtn =tk.Button(root,text="TEST")
anotherbtn.place(x=200, y=200, height=100, width=100)

root.mainloop()
