#
from tkinter import *

class Data:
    def __init__(self, first_name, age, hasphone):
        """Stores data in a list"""
        self.first_name = first_name
        self.age = age
        self.hasphone = hasphone 

class Interface1:
    def __init__(self, parent):
        """Label, entry and button widgets """
        self.details = []

        #Collect Person Data
        self.frame1 = Frame(parent, bg="violet", padx=20, pady=20)
        self.frame1.grid()

        self.frame2 = Frame(parent)
        self.frame2.grid()

        self.cpd = Label(self.frame1, text="Collecting Person Data") 
        self.cpd.grid(row=0, column=0, sticky=W)

        self.show_all = Button(self.frame1, text="Show All", command=self.display)
        self.show_all.grid(row=0,column=1,sticky=E, padx=(70,0))

        self.first_name_label = Label(self.frame2, text="First name: ")
        self.first_name_label.grid(row=0,column=0, sticky=NW)

        self.age_label = Label(self.frame2, text="Age: ")
        self.age_label.grid(row=1,column=0, sticky=NW)

        self.first_name_entry = Entry(self.frame2, width = 20)
        self.first_name_entry.grid(row=0,column=1, sticky=NE)

        self.age_entry = Entry(self.frame2, width = 20)
        self.age_entry.grid(row=1,column=1, sticky=SE)

        self.phone_q = Label(self.frame2, text="Do you have a mobile phone? ")
        self.phone_q.grid(row=2, sticky=E)

        self.opt_list = ["Yes", "No"]
        self.opt_var = StringVar()
        self.opt_var.set("*")
        for i in range(len(self.opt_list)):
            btns = Radiobutton(self.frame2, text=self.opt_list[i], variable=self.opt_var,
            anchor=W, value=self.opt_list[i])
            btns.grid()

        self.enter_data = Button(self.frame2, text="Enter Data", command=self.input)
        self.enter_data.grid(pady=20, columnspan=2)

        #Display Person Data
        self.frame3 = Frame(parent, bg="violet", padx=20, pady=20)
        self.frame3.grid()
        self.frame3.grid_forget()

        self.dpd = Label(self.frame3, text="Displaying Personal Data")
        self.dpd.grid(row=0, column=0, sticky=W)

        self.show_all = Button(self.frame3, text="Add New Person", command=self.change)
        self.show_all.grid(row=0,column=1,sticky=W, padx=(70,0))

        self.frame4 = Frame(parent)
        self.frame4.grid()
        self.frame4.grid_forget()

        self.name_label = Label(self.frame4, text="First Name: ")
        self.name_label.grid(row=0,column=0, sticky=NW)

        self.name_display = Label(self.frame4, text="")
        self.name_display.grid(row=0,column=1, sticky=NE)

        self.age_label2 = Label(self.frame4, text="Age: ")
        self.age_label2.grid(row=1,column=0, sticky=NW)

        self.age_display = Label(self.frame4, text="")
        self.age_display.grid(row=1,column=1, sticky=SE)

        self.phone_display = Label(self.frame4, text="")
        self.phone_display.grid(row=2, sticky=E)

        self.back = Button(self.frame4, text = "Previous", command=self.left)
        self.back.grid(row=3, column=0, sticky=W, padx=10)
        
        self.forward = Button(self.frame4, text="Next", command=self.right)
        self.forward.grid(row=3, column=3, sticky=E, padx=10)
        self.target= 0

    def input(self):
        """Collects the data"""
        self.details.append(Data(self.first_name_entry.get(), str(self.age_entry.get()), self.opt_var.get()))
        self.name_display.configure(text = self.details[0].first_name)
        self.age_display.configure(text = self.details[0].age)
        if self.details[0].hasphone == "Yes":
            self.phone_display.configure(text= "{} has a mobile phone".format(self.details[self.target].first_name))
        else:
            self.phone_display.configure(text="{} does not have a mobile phone".format(self.details[self.target].first_name))

        self.first_name_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.opt_var.set("*")

    def display(self):
        """Switch to Display Person Data"""
        self.frame1.grid_forget()
        self.frame2.grid_forget()
        self.frame3.grid()
        self.frame4.grid()
        
    def change(self):
        """Switch to Colelcting Person Data"""
        self.frame3.grid_forget()
        self.frame4.grid_forget()
        self.frame1.grid()
        self.frame2.grid()

    def left(self):
        """Displays the previous person data"""
        self.target -= 1
        if self.target < 0:
            self.target = len(self.details) - 1 
        self.name_display.configure(text= self.details[self.target].first_name)
        self.age_display.configure(text= self.details[self.target].age)
        if self.details[self.target].hasphone == "Yes":
            self.phone_display.configure(text= "{} has a mobile phone".format(self.details[self.target].first_name))
        else:
            self.phone_display.configure(text="{} does not have a mobile phone".format(self.details[self.target].first_name))

    def right(self):
        """Displays the next person data"""
        self.target += 1
        if self.target >= len(self.details):
            self.target = 0
        self.name_display.configure(text= self.details[self.target].first_name)
        self.age_display.configure(text=self.details[self.target].age)
        self.phone_display.configure(text=self.details[self.target])
        if self.details[self.target].hasphone == "Yes":
            self.phone_display.configure(text= "{} has a mobile phone".format(self.details[self.target].first_name))
        else:
            self.phone_display.configure(text="{} does not have a mobile phone".format(self.details[self.target].first_name))

#main routine
root = Tk()
root.geometry("350x250")
survey = Interface1(root)
root.mainloop()