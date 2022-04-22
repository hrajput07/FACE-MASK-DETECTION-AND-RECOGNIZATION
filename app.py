# tkinter gui for cv2 video stream

from tkinter import *
from PIL import Image, ImageTk
from detect_mask_video import muskDetection
from tkinter import filedialog

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb 

root = Tk()
root.geometry("1080x600")
root.configure(background=_from_rgb((255,167,129)))
root.bind("<Escape>", quit)
root.bind("q", quit)


label = Label(root)
label.pack()

Top = Frame(root, bd=10,  relief=RIDGE)
Top.pack(side=TOP, fill=X)

lbl_title = Label(Top, text = "CoverUp : Face Mask Detector",
                  bg=_from_rgb((255,167,129)), fg=_from_rgb((91,14,45)), font=('georgia', 56))
lbl_title.pack(fill=BOTH,expand=1)


# Image Frame
image = Image.open("maskk.png")
image = image.resize((600,450), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image)
label1 = Label(image=test ,bg=_from_rgb((255,167,129)))
label1.image = test
label1.place(x=-50, y=150)



sideFrame = Frame(root, bd=10,  relief=RIDGE)
sideFrame.pack(side=RIGHT)

def startlivefeed():
    muskDetection(0)
    
def startvideofedd():
    filename = filedialog.askopenfilename(title="Open file")
    muskDetection(filename)
    
    

button1 =  Button(root,text="Livefeed",padx=30,bg=_from_rgb((153,52,65)), fg=_from_rgb((255,232,237)) , relief=RIDGE,borderwidth=1,
                  font= ('georgia',20,'bold'),cursor="hand2", command=startlivefeed)
button1.place(x=600, y=260)

button2 =  Button(root,text="Browse Video",padx=30,bg=_from_rgb((153,52,65)), fg=_from_rgb((255,232,237)),relief=RIDGE,borderwidth=1,
                  font= ('georgia',20,'bold'),cursor="hand2", command=startvideofedd)
button2.place(x=600, y=370)

root.mainloop()