#
from tkinter import *

class Data:
    def __init__(self, first_name, age, hasphone):
        self.first_name = first_name
        self.age = age
        self.hasphone = hasphone 
        if self.age == "yes":
            pass

class Interface1:
    def __init__(self, parent):

        frame1 = Frame(root, bg="violet", padx=20, pady=20)
        frame1.grid()

        self.cpd = Label(frame1, text="Collecting Person Data") 
        self.cpd.grid(row=0, column=0, sticky=W)

        show_all = Button(frame1, text="Show All", command=None)
        show_all.grid(row=0,column=1,sticky=E, padx=(70,0))

        frame2 = Frame(root)
        frame2.grid()

        frame3 = Frame(frame2)
        frame3.grid()

        first_name_label = Label(frame3, text="First name: ")
        first_name_label.grid(row=0,column=0, sticky=NW)

        age_label = Label(frame3, text="Age: ")
        age_label.grid(row=1,column=0, sticky=NW)

        first_name_entry = Entry(frame3, width = 20)
        first_name_entry.grid(row=0,column=1, sticky=NE, padx=(100,0))

        age_entry = Entry(frame3, width = 20)
        age_entry.grid(row=1,column=1, sticky=SE)

        frame4 = Frame(root)
        frame4.grid()

        phone_q = Label(frame4, text="Do you have a mobile phone? ")
        phone_q.grid(row=0,columnspan=2, sticky=W, padx=(10,120))

        frame5 = Frame(frame4)
        frame5.grid(padx=(140,0))

        self.opt_list = ["Yes", "No"]
        self.opt_var = StringVar()
        self.opt_var.set("*")
        for i in range(len(self.opt_list)):
            btns = Radiobutton(parent, text=self.opt_list[i], variable=self.opt_var,
            anchor=W, value=self.opt_list[i])
            btns.grid()

        enter_data = Button(parent, text="Enter Data", command=None)
        enter_data.grid(pady=20)

        #layout 2
        name_input = Label(parent, text=None)
        name_input.grid()

        age_input = Label(parent, text=None)
        age_input.grid()

        #hasphone = Label(parent, text="{} {} {} a mobile phone".format())
        #hasphone.grid()
        #def add_details(self):
        self.details = []
        self.details.append(Data(first_name_entry.get(), age_entry.get(), self.opt_var.get()))

        '''
        back = Button(parent, text = "Previous", command=None)
        back.grid(row=3, sticky=W)

        forward = Button(parent, text="Next", command=None)
        forward.grid(row=3, sticky=E)
        '''

        def change(self):
            self.cpd.configure(text="Displaying Person Data")
            self.first_name_label.forget()

#main routine
root = Tk()
root.geometry("300x250")
survey = Interface1(root)
root.mainloop()