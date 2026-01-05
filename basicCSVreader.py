### objective: planner
### display window
### open file in window
### read a csv
### display data
### close window
import csv
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Project Planner")
    frm = ttk.Frame(root, padding = 10)
    frm.grid()
    dictionary = read_csv(get_filename())
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    ttk.Button(frm, text="Append Key", command=lambda: draw_dicts(append_key(dictionary),frm)).grid(column=0, row=0)
    #ttk.Button(frm, text="Open File", command=get_filename()).grid(column=0, row=1)
    #Need to figure out how to capture a variable from a Button
    draw_dicts(dictionary, frm)

    """
    canvas = tk.Canvas(root, width=800, height=400, bg="green")
    canvas.pack(side="bottom")
    """
    tk.mainloop()

    
 

def jokes(dictionary):
    ## does nothing but print and test dictionary stuff
    print(dictionary)

    print(dictionary[7]["title"])
    print(dictionary[4]["duration"], "cool cool cool")
    
    #
    print(dictionary.keys())
    for bag in dictionary:
        print(dictionary[bag]["duration"], end=" ")
    # notice the difference in output; your book wanted to append the results on the for loop
    # to a tuple. need to read more tuples and named tuples. im doing this kinda arrayish
    print()

def get_filename():
    #user input for filename and returns
    #a dictionary of csv informaiton
    try:
        filename = askopenfilename(title= "Open CSV Document", initialdir=".", 
                                   filetypes=[("CSV Document", "*.csv")])
    except:
        print("file not found: please check path to *csv file")
    print(f"Filename: {filename}")    
    return filename
    
def read_csv(filename):
    dictionary = {}
    for row in csv.reader(open(filename)):
        ## kinda makes a temp array with a cubby for every item() seperated by commas (csv)
        ## then uses that temp array to initialize a dict {cool : stuff} and it 
        ## turns the 'stuff' into a list[] so i can pull stuff by saying call[cool]["stuff"]
        key = int(row[0])
        title = row[1]
        duration = row[2]
        ## can have infinite 'rows' the 'row' ends with \n
        dictionary[key] = {"title" : title, "duration" : duration}
    return dictionary
    ## since dict variables are mutable i can return a full dict and work it over there

def append_key(dicts):
    new_key = input("positive#: ")
    k = input("tile? ")
    v = input ("duration?")
    dicts[int(new_key)] = {"title" : k, "duration" : v}
    ## adding new entries requires i continuously initialize the "title and duration keys"
    ## generally speaking i create a new funciton that automatically impliments that
    ## dictionary[input()] = {"title" : k, "duration" : v}
    return dicts
    

def draw_dicts(dicts, frame):
    tk.Label(frame, text="Key: ").grid(column=0, row=1)
    ttk.Label(frame, text="Obj 0: ").grid(column=1, row=1)
    ttk.Label(frame, text="Obj 1: ").grid(column=2, row=1)
    
    for csv in dicts:
        ttk.Label(frame, text=csv).grid(column=0, row=csv+2)
        ttk.Label(frame, text=dicts[csv]["duration"]).grid(column=2, row=csv+2)
        ttk.Label(frame, text=dicts[csv]["title"]).grid(column=1, row=csv+2)


main()