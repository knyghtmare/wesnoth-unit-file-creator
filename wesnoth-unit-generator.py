#!/usr/bin/env python3
from tkinter import *
from tkinter.ttk import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.amla_var = BooleanVar(self)
        self.amla_var.set(1)
        self.amla = ""

#    def say_hi(self):
#        print("Hi, there, everyone!")

    def createWidgets(self):
        # the frame for the main body
       
        self.frame = Labelframe(self)
        self.frame['text'] = "** Main Stats **"
        self.frame['width'] = 350
        self.frame['height'] = 20
        self.frame.grid(row=0, column=0, rowspan=1, columnspan=4, padx=10, pady=2)
        
        # the quit button
        self.qt_btn = Button(self)
        self.qt_btn['text'] = "Quit"
        # self.qt_btn['fg'] = "red"
        # self.qt_btn['bg'] = "black"
        self.qt_btn['command'] = self.quit
        self.qt_btn.grid(row=15, column=2, rowspan=1, columnspan=2)

        # add labels
        self.addMainLabels()

        # add entry fields
        self.addEntryFields()

        # add AMLA enabler
        self.addAMLAcheckbox()

        self.createunit = Button(self)
        self.createunit['text'] = "Create Unit"
        # self.createunit['fg'] = "green"
        self.createunit['command'] = self.createUnit
        self.createunit.grid(row=15, column=0, rowspan=1, columnspan=2)

    def addAMLAcheckbox(self):
        # the label
        self.label_amla = Label(self)
        self.label_amla['text'] = "Enable AMLA?"
        self.label_amla.grid(row=7, column=0, columnspan=2)

        self.check_amla = Checkbutton(self)
        self.check_amla['text'] = "Enabled"
        # error handling
        try:
            self.check_amla['variable'] = self.amla_var
        except AttributeError as e:
            # show message at terminal
            # but allow program to still compile
            print(e)
        self.check_amla['command'] = self.check_func
        self.check_amla.grid(row=7, column=2, columnspan=2)

    def check_func(self):
        value = self.amla_var.get()
        if value == 1:
            self.amla = "Yes"
        elif value == 0:
            self.amla = "No"

    def addMainLabels(self):
        # unit id
        self.label_id = Label(self)
        self.label_id['text'] = "ID:"
        self.label_id.grid(row = 1, column = 0, columnspan=2)

        # unit name
        self.label_name = Label(self)
        self.label_name['text'] = "Name:"
        self.label_name.grid(row=2, column=0, columnspan=2)

        # unit race
        self.label_race = Label(self)
        self.label_race['text'] = "Race:"
        self.label_race.grid(row=3, column=0, columnspan=2)

        # unit hitpoints
        self.label_hp = Label(self)
        self.label_hp['text'] = "Hitpoints:"
        self.label_hp.grid(row=4, column=0, columnspan=2)

        # unit experience
        self.label_xp = Label(self)
        self.label_xp['text'] = "Experience:"
        self.label_xp.grid(row=5, column=0, columnspan=2)

        # unit advances_to
        self.label_advances = Label(self)
        self.label_advances['text'] = "Advances To:"
        self.label_advances.grid(row=6, column=0, columnspan=2)

        # unit gender
        self.label_gender = Label(self)
        self.label_gender['text'] = "Gender:"
        self.label_gender.grid(row=8, column=0,columnspan=2)

        self.label_desc = Label(self)
        self.label_desc['text'] = "Unit Description:"
        self.label_desc.grid(row=9, column=0, columnspan=2)

        self.label_level = Label(self)
        self.label_level['text'] = "Unit Level:"
        self.label_level.grid(row=10, column=0, columnspan=2)

    def addEntryFields(self):
        # unit id
        self.enter_id = Entry(self)
        self.enter_id.insert(0, "Enter Unit ID")
        self.enter_id.grid(row=1, column=2, columnspan=2)

        # unit name
        self.enter_name = Entry(self)
        self.enter_name.insert(0, "Enter Unit Name")
        self.enter_name.grid(row=2, column=2, columnspan=2)

        # unit race
        self.enter_race = Entry(self)
        self.enter_race.insert(0, "Enter Unit Race")
        self.enter_race.grid(row=3, column=2, columnspan=2)

        # unit HP
        self.enter_hp = Entry(self)
        self.enter_hp.insert(0, "Enter Unit Hitpoints")
        self.enter_hp.grid(row=4, column=2, columnspan=2)

        # unit XP
        self.enter_xp = Entry(self)
        self.enter_xp.insert(0, "Enter Unit XP")
        self.enter_xp.grid(row=5, column=2, columnspan=2)

        # unit advances_to
        self.enter_advances = Entry(self)
        self.enter_advances.insert(0, "Enter Advancing Unit ID")
        self.enter_advances.grid(row=6, column=2, columnspan=2)

        # unit gender
        self.enter_gender = Entry(self)
        self.enter_gender.insert(0, "Enter Unit Gender/Sex")
        self.enter_gender.grid(row=8, column=2, columnspan=2)

        # unit description
        self.enter_desc = Text(self)
        self.enter_desc['height'] = 10
        self.enter_desc['width'] = 22
        self.enter_desc['font'] = "courier"
        self.enter_desc.insert(INSERT,"Enter Unit Description")
        self.enter_desc.grid(row=9, column=2, columnspan=2)

        # unit level
        self.enter_level = Entry(self)
        self.enter_level.insert(0, "Enter Unit Level")
        self.enter_level.grid(row=10, column=2, columnspan=2)

        # file name
        # self.enter_filename = Entry(self)
        # self.enter_filename.insert(0, "generic_unit")
        # self.enter_filename.grid(row=11, column=1, columnspan=2)

    def createUnit(self):
        # indicate that I created a file
        print("Unit file has been Created.")

        # not sure why this message box wont
        # pop up
        # self.response = self.messagebox.showinfo("Status:", "Unit file has been Created.")
        
        unit_file_name = self.enter_id.get()
        unit_file_name = unit_file_name.replace(" ","_")
        with open('{n}.cfg'.format(n=unit_file_name),'w') as unitfile:
            unitfile.write("\n[unit_type]\n")
            # bulk code here

            # unit id
            unit_id_final = '    id = "' + self.enter_id.get() + '"\n'
            unitfile.write(unit_id_final)

            # unit name
            unit_name_final = '    name = _ "' + self.enter_name.get() + '"\n'
            unitfile.write(unit_name_final)

            # unit race
            unit_race_final = '    race = "' + self.enter_race.get() + '"\n'
            unitfile.write(unit_race_final)

            # unit hp
            unit_hp_final = '    hitpoints = ' + self.enter_hp.get() + '\n'
            unitfile.write(unit_hp_final)

            # unit gender
            unit_gender_final = '    gender = "' + self.enter_gender.get() + '"\n'
            unitfile.write(unit_gender_final)

            # unit xp
            unit_xp_final = '    experience = ' + self.enter_xp.get() + '\n'
            unitfile.write(unit_xp_final)

            # unit level
            unit_lvl_final = '    level = ' + self.enter_level.get() + '\n'
            unitfile.write(unit_lvl_final)

            if self.amla == "Yes":
                amla_default = '    {AMLA_DEFAULT}' + '\n'
                unitfile.write(amla_default)
            elif self.amla == "No":
                amla_default = '\n'
                unitfile.write(amla_default)


            # unit advances_to
            unit_advances_final = '    advances_to = "' + self.enter_advances.get() + '"\n'
            unitfile.write(unit_advances_final)


            # unit description
            unit_desc_final = '    description = _ "' + self.enter_desc.get("0.0",END) + '"\n'
            unitfile.write(unit_desc_final)

            # conclude it with
            # the end tag
            unitfile.write("[/unit_type]\n")


# var = IntVar()


def main():
    root = Tk()
    root.title("Wesnoth Unit File Creator")
    root.geometry("400x430")
    # preventing a resize
    root.resizable(False, False)


    # instantiate the class
    app = Application(master=root)
    # loop it
    app.mainloop()
    # destroy it once you
    # are done
    root.destroy()

main()
