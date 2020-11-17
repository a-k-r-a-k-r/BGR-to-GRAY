#written by akr
#importing modules and libraries
import tkinter
from tkinter import filedialog,BOTTOM,LEFT
from PIL import ImageTk,Image

#defining window
root=tkinter.Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("RGB to GRAY")

def showimage():
    global gray_img

    img_path=filedialog.askopenfilename(initialdir="/",title="Select Image",filetype=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files",("*.*"))))
    gray_img=Image.open(img_path).convert('LA')
    gray_img.thumbnail((350,350))
    img=ImageTk.PhotoImage(gray_img)
    img_frame.config(image=img)
    img_frame.image=img
    
def close():
    root.destroy()

def save():
    save_name=filedialog.asksaveasfilename(initialdir="/",filetype=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files",("*.*"))))
    gray_img.save(save_name)

#set default image
default_img=ImageTk.PhotoImage(Image.open("default.jpg"))

button_frame=tkinter.Frame(root)
button_frame.pack(side=BOTTOM,padx=15,pady=15)
img_frame=tkinter.Label(root,image=default_img)
img_frame.pack()
browse_button=tkinter.Button(button_frame,text="Browse Image",command=showimage)
browse_button.pack(side=LEFT)
save_button=tkinter.Button(button_frame,text="Save",command=save)
save_button.pack(side=LEFT,padx=10)
exit_button=tkinter.Button(button_frame,text="Exit",command=close)
exit_button.pack(side=LEFT,padx=10)

#mainloop
root.mainloop()
