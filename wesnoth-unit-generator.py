from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

#    def say_hi(self):
#        print("Hi, there, everyone!")

    def createWidgets(self):
        # the frame for the main body
        """
        self.frame = LabelFrame(self)
        self.frame['text'] = "Main Stats"
        self.frame['width'] = 300
        self.frame['height'] = 600
        self.frame.grid(row=0, column=0, rowspan=5, columnspan=9)
        """
        # the quit button
        self.qt_btn = Button(self)
        self.qt_btn['text'] = "Quit"
        self.qt_btn['fg'] = "red"
        # self.qt_btn['bg'] = "black"
        self.qt_btn['command'] = self.quit
        self.qt_btn.grid(row=9, column=1, rowspan=1)

        # add labels
        self.addMainLabels()

        # add entry fields
        self.addEntryFields()

        # sample hello button
        # self.hi_there = Button(self)
        # self.hi_there["text"] = "Hello"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack()
        self.createunit = Button(self)
        self.createunit['text'] = "Create Unit"
        self.createunit['fg'] = "green"
        self.createunit['command'] = self.createUnit
        self.createunit.grid(row=9, column=0, rowspan=1)

    def addMainLabels(self):
        # unit id
        self.label_id = Label(self)
        self.label_id['text'] = "ID:"
        # self.label_id['pady'] = 1
        # self.label_id['padx'] = 1
        self.label_id.grid(row = 1, column = 0)

        # unit name
        self.label_name = Label(self)
        self.label_name['text'] = "Name:"
        # self.label_name['pady'] = 1
        # self.label_name['padx'] = 1
        self.label_name.grid(row = 2, column = 0)

        # unit race
        self.label_race = Label(self)
        self.label_race['text'] = "Race:"
        self.label_race.grid(row = 3, column = 0)

        # unit hitpoints
        self.label_hp = Label(self)
        self.label_hp['text'] = "Hitpoints:"
        self.label_hp.grid(row = 4, column = 0)

        # unit experience
        self.label_xp = Label(self)
        self.label_xp['text'] = "Experience:"
        self.label_xp.grid(row = 5, column = 0)

        # unit advances_to
        self.label_advances = Label(self)
        self.label_advances['text'] = "Advances To:"
        self.label_advances.grid(row = 6, column = 0)

        self.label_desc = Label(self)
        self.label_desc['text'] = "Unit Description:"
        self.label_desc.grid(row = 7, column = 0)

    def addEntryFields(self):
        # unit id
        self.enter_id = Entry(self)
        self.enter_id.insert(0, "Enter Unit ID")
        self.enter_id.grid(row=1, column = 1)

        # unit name
        self.enter_name = Entry(self)
        self.enter_name.insert(0, "Enter Unit Name")
        self.enter_name.grid(row=2, column = 1)

        # unit race
        self.enter_race = Entry(self)
        self.enter_race.insert(0, "Enter Unit Race")
        self.enter_race.grid(row=3, column = 1)

        # unit HP
        self.enter_hp = Entry(self)
        self.enter_hp.insert(0, "Enter Unit Hitpoints")
        self.enter_hp.grid(row=4, column = 1)

        # unit XP
        self.enter_xp = Entry(self)
        self.enter_xp.insert(0, "Enter Unit XP")
        self.enter_xp.grid(row=5, column = 1)

        # unit advances_to
        self.enter_advances = Entry(self)
        self.enter_advances.insert(0, "Enter Unit ID")
        self.enter_advances.grid(row=6, column = 1)

        # unit description
        self.enter_desc = Entry(self)
        self.enter_desc.insert(0, "Enter Unit Description")
        self.enter_desc.grid(row=7, column = 1)

    def createUnit(self):
        # indicate that I created a file
        print("Unit file has been Created.")
        with open('generic_unit.cfg','w') as unitfile:
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
            unit_hp_final = '    hitpoints = "' + self.enter_hp.get() + '"\n'
            unitfile.write(unit_hp_final)

            # unit xp
            unit_xp_final = '    experience = "' + self.enter_xp.get() + '"\n'
            unitfile.write(unit_xp_final)

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


def main():
    root = Tk()
    root.title("Wesnoth Unit File Creator")
    # root.geometry("300x300")
    # instantiate the class
    app = Application(master=root)
    # loop it
    app.mainloop()
    # destroy it once you
    # are done
    root.destroy()

main()



