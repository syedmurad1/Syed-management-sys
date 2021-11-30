from tkinter import *
from tkinter import messagebox
from subprocess import call
 
root = Tk()
root.title("Syed Murad's Employee Registation")
root.geometry("260x200")
global e1
global e2
 
def Ok():
    root.destroy()
    call(["python", "tkenter.py"]) # Change directory if needed

def Ok2():
    root.destroy()
    call(["python", "api.py"])  # Change directory if needed

def Ok3():
    root.destroy()
    call(["python", "images.py"])  # Change directory if needed

def Ok4():
    root.destroy()
    call([root, root.quit])  
 
Label(root, text="Welcome", font=("Arial", 15, "bold"), bg="#00376b", fg="#FFFCF9").place(x=30, y=10)
Button(root, text="Add", command=Ok, height= 3, width= 12).place(x=30,y=50)
Button(root, text="API", command=Ok2, height= 3, width= 12).place(x=30,y=110)
Button(root, text="Images", command=Ok3, height= 3, width= 12).place(x=150,y=50)
Button(root, text="Exit", command=Ok4, height= 3, width= 12).place(x=150,y=110)
 

 
root.mainloop()