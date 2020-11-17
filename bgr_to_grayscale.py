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
root.iconbitmap("icon.ico")

def showimage():
    global gray_img
    img_path=filedialog.askopenfilename(initialdir="/",title="Select Image",filetype=(("All Files","*.*"),("JPG File","*.jpg"),("PNG File","*.png")))
    #display original image
    orig_img=Image.open(img_path)
    orig_img.thumbnail((50,50))
    orig_img=ImageTk.PhotoImage(orig_img)
    orig_img_frame.config(image=orig_img)
    orig_img_frame.image=orig_img

    gray_img=Image.open(img_path).convert('LA')
    gray_img.thumbnail((350,350))
    img=ImageTk.PhotoImage(gray_img)
    img_frame.config(image=img)
    img_frame.image=img
    
def close():
    root.destroy()

def save():
    save_name=filedialog.asksaveasfilename(initialdir="/",defaultextension=".png",filetype=(("PNG File","*.png"),("JPG File","*.jpg"),("All Files","*.*")))
    gray_img.save(save_name)

#set default image
default_real_img=Image.open("default.jpg")
default_real_img.thumbnail((70,50))
default_real_img=ImageTk.PhotoImage(default_real_img)

default_img=Image.open("default.jpg").convert('LA')
default_img.thumbnail((350,350))
default_img=ImageTk.PhotoImage(default_img)




#defining frames
output_frame=tkinter.Frame(root)
output_frame.pack()
button_frame=tkinter.Frame(root)
button_frame.pack(side=BOTTOM,padx=15,pady=(0,40))

#defining "output_frame" widgets

img_frame=tkinter.Label(output_frame,image=default_img,width=500,height=400,bg="black")
img_frame.grid(row=0,column=0)
orig_img_frame=tkinter.Label(output_frame,image=default_real_img,width=60,height=60,bg="black")
orig_img_frame.grid(row=0,column=0,sticky="NW")


#defining "button_frame" widgets
browse_button=tkinter.Button(button_frame,text="Browse Image",width=15,bg="black",fg="white",command=showimage)
browse_button.pack(side=LEFT)
save_button=tkinter.Button(button_frame,text="Save",width=15,command=save,bg="black",fg="white")
save_button.pack(side=LEFT,padx=10)
exit_button=tkinter.Button(button_frame,text="Exit",width=15,command=close,bg="black",fg="white")
exit_button.pack(side=LEFT)

#mainloop
root.mainloop()
