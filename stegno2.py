from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk, Image
from tkinter import messagebox
from stegano import exifHeader as stg





def encode():
    enc = Tk()
    enc.title("Encode")
    enc.geometry("600x400+300+150")
    enc.maxsize(600, 400)
    enc.minsize(600, 400)

    Label(enc, text="STEGIT", bg="grey", width="300", height="3", font=("Caliber", 15, "bold")).pack()
    label1 = Label(enc, text="Secret message:", bd=3, font=('', 10, 'bold'))
    label1.place(relx=0.1, rely=0.3, height=20, width=100)

    entry = Entry(enc, bd=3, font=('', 13))
    entry.place(relx=0.4, rely=0.3)

    label2 = Label(enc, text="File name:", bd=3, font=('', 10, 'bold'))
    label2.place(relx=0.1, rely=0.4, height=20, width=100)

    entrysave = Entry(enc, bd=3, font=('', 13))
    entrysave.place(relx=0.4, rely=0.4)

    def openfile():
        global fileopen
        fileopen = StringVar()
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg files", "*jpg"), ("all files", "*.*")))

        label3 = Label(enc, text=fileopen, bd=3, font=('', 13))
        label3.place(relx=0.3, rely=0.5)

    def encodee():
        response = messagebox.askyesno("pop up", "do you want to encode")
        if response == 1:
            stg.hide(fileopen, entrysave.get() + '.jpg', entry.get())
            messagebox.showinfo("pop up", "successfully encode")

        else:
            messagebox.showwarning("pop up", "unsuccessful")

    buttonselect = Button(enc, text="Select file", bd=3, font=('', 11, 'bold'), command=openfile)
    buttonselect.place(relx=0.1, rely=0.5)

    buttonencode = Button(enc, text="Encode", bd=3, font=('', 13, 'bold'), command=encodee)
    buttonencode.place(relx=0.4, rely=0.7)


def decode():
    dnc = Tk()
    dnc.title("Decode")
    dnc.geometry("500x400+300+150")
    dnc.maxsize(500, 400)
    dnc.minsize(500, 400)

    def openfile():
        global fileopen
        fileopen = StringVar()
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg files", "*jpg"), ("all files", "*.*")))

    def decodee():
        message = stg.reveal(fileopen)

        label4 = Label(dnc, text=message, bd=3, font=('', 13))
        label4.place(relx=0.3, rely=0.3)

    buttonselect = Button(dnc, text="Select file", bd=3, font=('', 13, 'bold'), command=openfile)
    buttonselect.place(relx=0.1, rely=0.3)

    buttondecode = Button(dnc, text="Decode", bd=3, font=('', 13, 'bold'), command=decodee)
    buttondecode.place(relx=0.4, rely=0.5)





class main:

    def __init__(self, master):
        self.master = master
        self.stegit()

    def stegit(self):
            stg = Tk()
            stg.title("STEGIT")
            stg.geometry("500x400+300+150")
            stg.maxsize(500, 400)
            stg.minsize(500, 400)

            Label(stg, text="STEGIT", bg="grey", width="300", height="3", font=("Caliber", 15, "bold")).pack()

            Button(stg, text="Encode", height="2", width="20", bd=3, font=('', 13, "bold"), borderwidth=10, command=encode).pack(pady=40)

            Button(stg, text="Decode", height="2", width="20", bd=3, font=('', 13, "bold"), borderwidth=10, command=decode).pack(pady=40)




root = Tk()
main(root)
root.mainloop()