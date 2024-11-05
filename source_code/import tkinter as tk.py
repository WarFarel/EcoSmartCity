import tkinter as tk
from tkinter import messagebox#
import random
"""This imports the needed tkinter for the GUI"""


#This defines classes

class energy_source:
    def __init__(self, type,volume):
        self.active = True # This checks if source is on
        self.volume = volume #This sets the max volume kW
        self.type = type 
        
    def production(self):
        """This only will make the production count if it`s active"""
        return self.volume if self.active else None; 

    def activate(self):
        self.activvate = True
    #This turns the source on

    def deactivate(self):
        self.activate = False
    #This turns the source off


class distribution_grid:
    def __init__ (self):
        self.sources = []


    def add_source(self,source):
        self.sources.append(source)
        print(f"{source.source_type} has been added to the grid")
        """This adds an energy source by type"""

    def remove_source(self,source_type):
        self.sources = [src for src in self.sources 
                        if src.source_type != source_type]
        """This removes an energy source by type"""

    def deactivate_source(self, source_type):
        for src in self.sources:
            if src.source_type == source_type:
                src.deactivate()
                print (f"{source_type} deactivated.")

    def activate_source(self, source_type):
        for src in self.sources:
            if src.source_type == source_type:
                src.activate()
                print(f"{source_type} activated ")

    def all_production(self):
        return sum(source.production() for source in self.sources)
        #Sum up production of the sources
class energy_distribution_program:  
    def __init__ (self, root):
        self.root = root
        self.root.name ("Energy Distribution Program")
        self.grid = distribution_grid() #Starts an empty grid

        self.energy_choices = {
            
            "Solar":random.randint(0,200), #Solar set as random.
            "Wind":random.randint(0,150), #Wind set as random.
            "Hydro": 300, #Hydro set as 300 kW.
            "Grid":1000 #Grid power set as 1000 kW. 
        }
        
        #Dropdown menu for energy.
        self.source_type = tk.StringVar(root)
        self.source_type.set("Solar") #Default Value
        self.type_menu = tk.OptionMenu(root,self.source_type,
                                       *self.energy_choices.keys())
        self.type_menu.pack()

        #Buttons to do with the sources.
        #  add,remove,deactivate,activate.
        self.add_button = tk.Button(root, text = "Add Source",
                                     command = self.add_source)
        self.add_button.pack()


        self.remove_button = tk.Button(root, text = "Remove Source",
                        command = self.remove_source)
        self.remove_button.pack()


        self.deactivate_button = tk.Button(root,
              text = "Deactivate Source", command = self.deactivate_source)
        self.deactivate_button.pack()


        self.activate_button = tk.Button(root, text
         = "activate Source",command = self.activate_source)
        self.activate_button.pack()

        self.demand_label = tk.Lable(root, text = "Current Demand")
        self.demand_label.pack()
        self.demand_entry = tk.Entry(root)
        self.demand_entry.pack
        #This are demand input and buttons for optimazation
