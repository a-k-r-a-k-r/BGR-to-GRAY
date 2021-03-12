'''
    Program: BGR to GRAY Converter
    Author : akr
    GitHub : https://github.com/a-k-r-a-k-r
    Blog   : https://a-k-r-a-k-r.blogspot.com
'''

#importing modules and libraries
import tkinter
from PIL import ImageTk,Image
from tkinter import filedialog,BOTTOM,LEFT

#defining colors and fonts
root_color = "green"
output_background = "black"
button_background = "green"
thumb_background = "black"
button_color = "black"


#defining window
root=tkinter.Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("BGR 2 GRAY")
root.iconbitmap("resources/icons/icon.ico")
root.config(bg=root_color)


def showimage():
    global gray_real_img
    img_path=filedialog.askopenfilename(initialdir="/",title="Select Image",filetype=(("All Files","*.*"),("JPG File","*.jpg"),("PNG File","*.png")))
    #display original image
    orig_img=Image.open(img_path)
    orig_img.thumbnail((50,50))
    orig_img=ImageTk.PhotoImage(orig_img)
    orig_img_frame.config(image=orig_img)
    orig_img_frame.image=orig_img

    gray_img=Image.open(img_path).convert('LA')
    gray_real_img=Image.open(img_path).convert('LA')
    gray_img.thumbnail((350,350))
    img=ImageTk.PhotoImage(gray_img)
    img_frame.config(image=img)
    img_frame.image=img
    

def close():
    root.destroy()


def save():
    save_name=filedialog.asksaveasfilename(initialdir="/",defaultextension=".png",filetype=(("PNG File","*.png"),("JPG File","*.jpg"),("All Files","*.*")))
    gray_real_img.save(save_name)


#set default image
default_real_img=Image.open("resources/images/akr.png")
default_real_img.thumbnail((70,50))
default_real_img=ImageTk.PhotoImage(default_real_img)

default_img=Image.open("resources/images/akr.png").convert('LA')
default_img.thumbnail((350,350))
default_img=ImageTk.PhotoImage(default_img)


#defining frames
output_frame=tkinter.Frame(root)
output_frame.pack()
button_frame=tkinter.Frame(root,bg=button_background)
button_frame.pack(side=BOTTOM,padx=15,pady=(0,40))


#defining "output_frame" widgets
img_frame=tkinter.Label(output_frame,image=default_img,width=500,height=400,bg=output_background)
img_frame.grid(row=0,column=0)
orig_img_frame=tkinter.Label(output_frame,image=default_real_img,width=60,height=60,bg=thumb_background)
orig_img_frame.grid(row=0,column=0,sticky="NW")


#defining "button_frame" widgets
browse_button=tkinter.Button(button_frame,text="Browse Image",width=15,bg=button_color,fg="white",command=showimage)
browse_button.pack(side=LEFT)
save_button=tkinter.Button(button_frame,text="Save",width=15,command=save,bg=button_color,fg="white")
save_button.pack(side=LEFT,padx=10)
exit_button=tkinter.Button(button_frame,text="Exit",width=15,command=close,bg=button_color,fg="white")
exit_button.pack(side=LEFT)


#mainloop
root.mainloop()