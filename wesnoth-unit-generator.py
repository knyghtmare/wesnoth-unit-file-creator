from tkinter import *
from tkinter.ttk import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        # self.var = var
        self.amla_var = StringVar()
        self.amla_var.set(1)
        self.amla = "Yes"

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

        # sample hello button
        # self.hi_there = Button(self)
        # self.hi_there["text"] = "Hello"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack()
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
        # self.check_amla['var'] = self.amla_var
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
        # self.label_id['pady'] = 1
        # self.label_id['padx'] = 1
        self.label_id.grid(row = 1, column = 0, columnspan=2)

        # unit name
        self.label_name = Label(self)
        self.label_name['text'] = "Name:"
        # self.label_name['pady'] = 1
        # self.label_name['padx'] = 1
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

        # unit description
        self.enter_desc = Entry(self)
        self.enter_desc.insert(0, "Enter Unit Description")
        self.enter_desc.grid(row=9, column=2, columnspan=2)

        # unit level
        self.enter_level = Entry(self)
        self.enter_level.insert(0, "Enter Unit Level")
        self.enter_level.grid(row=10, column=2, columnspan=2)

        # file name
        self.enter_filename = Entry(self)
        self.enter_filename.insert(0, "generic_unit")
        self.enter_filename.grid(row=11, column=1, columnspan=2)

    def createUnit(self):
        # indicate that I created a file
        print("Unit file has been Created.")
        unit_file_name = self.enter_filename.get()
        with open('{n}.cfg'.format(n=unit_file_name),'w') as unitfile:
            unitfile.write("[unit_type]\n")
            # bulk code here

            # unit id
            unit_id_final = '    id = "' + self.enter_id.get() + '"\n'
            unitfile.write(unit_id_final)

            # unit name
            unit_name_final = '    name = "' + self.enter_name.get() + '"\n'
            unitfile.write(unit_name_final)

            # unit race
            unit_race_final = '    race = "' + self.enter_race.get() + '"\n'
            unitfile.write(unit_race_final)

            # unit hp
            unit_hp_final = '    hitpoints = ' + self.enter_hp.get() + '\n'
            unitfile.write(unit_hp_final)

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
                pass
            else:
                pass

            # unit advances_to
            unit_advances_final = '    advances_to = "' + self.enter_advances.get() + '"\n'
            unitfile.write(unit_advances_final)

            # add code for AMLA_DEFAULT
            # enabler here

            # unit description
            unit_desc_final = '    description = "' + self.enter_desc.get() + '"\n'
            unitfile.write(unit_desc_final)

            # conclude it with
            # the end tag
            unitfile.write("[/unit_type]\n")


# var = IntVar()


def main():
    root = Tk()
    root.title("Wesnoth Unit File Creator")
    root.geometry("400x320")

    # global var

    # instantiate the class
    app = Application(master=root)
    # loop it
    app.mainloop()
    # destroy it once you
    # are done
    root.destroy()

main()
