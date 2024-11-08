import tkinter as tk
from tkinter import messagebox
import random

#This imports the needed tkinter for the GUI

class energy_source:
    def __init__(self, type, volume):
        self.active = True # This checks if source is on
        self.volume = volume #This sets the max volume kW
        self.type = type 
        
    def production(self):
        """This only will make the production count if it`s active"""
        return self.volume if self.active else 0

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False


class distribution_grid:
    def __init__(self):
        self.sources = []

    def add_source(self, source):
        self.sources.append(source)
        print(f"{source.type} has been added to the grid")

    def remove_source(self, source_type):
        self.sources = [src for src in self.sources if src.type != source_type]

    def deactivate_source(self, source_type):
        for src in self.sources:
            if src.type == source_type:
                src.deactivate()
                print(f"{source_type} deactivated.")

    def activate_source(self, source_type):
        for src in self.sources:
            if src.type == source_type:
                src.activate()
                print(f"{source_type} activated")

    def all_production(self):
        return sum(source.production() for source in self.sources)

class energy_distribution_program:
    def __init__(self, root):
        self.root = root
        self.root.title("Energy Distribution Program")
        self.grid = distribution_grid()

        self.energy_choices = {
            "Solar": random.randint(0, 200),
            "Wind": random.randint(0, 150),
            "Hydro": 300,
            "Grid": 1000
        }
        
        self.source_type = tk.StringVar(root)
        self.source_type.set("Solar")
        self.type_menu = tk.OptionMenu(root, self.source_type, * self.energy_choices.keys())
        self.type_menu.pack()

        self.add_button = tk.Button(root, text=
                                "Add Source", command=self.add_source)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text=
                                    "Remove Source", command=self.remove_source)
        self.remove_button.pack()

        self.deactivate_button = tk.Button(root, text = 
                                 "Deactivate Source", command=self.deactivate_source)
        self.deactivate_button.pack()


        self.activate_button = tk.Button(root, text=
                                "Activate Source", command=self.activate_source)
        self.activate_button.pack()


        self.demand_label = tk.Label(root, text="Current Demand")
        self.demand_label.pack()
        self.demand_entry = tk.Entry(root)
        self.demand_entry.pack()


        self.optimize_button = tk.Button(root, text=
                                 "Optimize Distribution", command=self.optimize_distribution)
        self.optimize_button.pack()

        self.production_display = tk.Label(root, text=
                                        "Total Production 0 kW")
        self.production_display.pack()



        self.demand_display = tk.Label(root, text=
                                     "Demand in kW")
        self.demand_display.pack()


        self.difference_display = tk.Label(root, text=
                                         "Surplus/Deficit 0 kW")
        self.difference_display.pack()


        self.source_list_label = tk.Label(root, text=
                                       "Sources in Grid")
        self.source_list_label.pack()
        self.source_listbox = tk.Listbox(root, width=40)
        self.source_listbox.pack()
        
    
    #These will the different sources added etc.
    def add_source(self):
        source_type = self.source_type.get()
        volume = self.energy_choices[source_type]
        new_source = energy_source(source_type, volume)
        self.grid.add_source(new_source)
        self.update_display()


    def remove_source(self):
        source_type = self.source_type.get()
        self.grid.remove_source(source_type)
        self.update_display()


    def activate_source(self):
        source_type = self.source_type.get()
        self.grid.activate_source(source_type)
        self.update_display()


    def deactivate_source(self):
        source_type = self.source_type.get()
        self.grid.deactivate_source(source_type)
        self.update_display()


    def optimize_distribution(self):
        try:
            demand = float(self.demand_entry.get())
            total_production = self.grid.all_production()
            difference = total_production - demand
            self.demand_display.config(text=f"Current Demand : {demand}kW")
            self.difference_display.config(text=f"Surplus/Deficit: {difference} kW")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid demand")

    def update_display(self):
        total_production = self.grid.all_production()
        self.production_display.config(text=f"Total Production: {total_production} kW")
        
        self.source_listbox.delete(0, tk.END)
        for source in self.grid.sources:
            status = "Active" if source.active else "Inactive"
            self.source_listbox.insert(tk.END, f"{source.type}: {status} {source.volume} kW")

if __name__ == "__main__":
    root = tk.Tk()
    app = energy_distribution_program(root)
    root.mainloop()
