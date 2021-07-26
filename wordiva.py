from tkinter import *
import json
from tkinter import messagebox
from difflib import get_close_matches

elements = json.load(open("wordbook.json"))


page = Tk()
page.geometry("1123x300")
page.title("Wordiva")
page.iconbitmap(r"Dicto.ico")
page.configure(background="#5A20CB")
userin = " "


def wordm():
    a = elements.keys()
    userin = e1.get()
    if userin.lower() in elements:
        t1.delete("1.0", END)
        t1.insert(END, elements[userin.lower()])
    elif userin.upper() in elements:
        t1.delete("1.0", END)
        t1.insert(END, elements[userin.upper()])

    elif len(get_close_matches(userin, a)) > 0:
        b = get_close_matches(userin, a)[0]
        t1.delete("1.0", END)
        c = "Are you looking for (%s) instead --type(y/n) in 2nd box" % b
        d = "Sorry try another word please"
        e = "Please try again"
        t1.insert(END, c)
        userin1 = e2.get()

        if userin1.lower() == "y":
            t1.delete("1.0", END)
            t1.insert(END, elements[b])
        elif userin1.lower() == "n":
            t1.delete("1.0", END)
            t1.insert(END, d)

    else:
        messagebox.showinfo("Error", "Sorry try another word please")


b1 = Button(page, text="Submit", command=wordm,
            bg="#CAD5E2", height=1, width=10, font=("times"))
b1.pack()
b1.grid(row=2, column=2,)

entry = StringVar()  # HERE WORD IS ENTERED
e1 = Entry(page, textvariable=entry, font=("Comic Sans", "16"))
e1.grid(row=0, column=2)


entry1 = StringVar()  # HERE WORD IS ENTERED
e2 = Entry(page, textvariable=entry1, font=("Comic Sans", "16"), width=5)
e2.grid(row=1, column=2)

# MEANING WILL PRINTED HERE
t1 = Text(page, height=15, width=75, font="tahoma 20", fg="#120E43")
t1.grid(row=4, column=2)


page.mainloop()
