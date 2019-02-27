import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
from warehouse import Warehouse
from wh_reader import WHreader
from wh_search import 

win = tk.Tk()
win.title("Warehouse Calculator")

"""Custom Input"""

#warehouse information

def load():
	"""
        opens a load dialogue window to load a file and creates a WHreader and a Warehouse object
    """
	filename = filedialog.askopenfilename(parent=win)
	file = open(filename)
	global read_setting
	read_setting = WHreader(filename)
	global whouse_object
	whouse_object = Warehouse(WHreader(filename).stock, WHreader(filename).psus)
   
def view():
	"""
        view the current warehouse setting in a different window
    """
	view_win = tk.Tk()
	stock_label = ttk.Label(view_win, text= 'Stock: ' + (', '.join(read_setting.stock)))
	stock_label.grid(column=1, row=0)
	psu_label = ttk.Label(view_win, text= 'PSUS:')
	psu_label.grid(column=1, sticky='W', row=1)
	counter = 0
	for psu in read_setting.psus:
		counter += 1
		psu_label = ttk.Label(view_win, text= 'PSU ' + str(counter) + ': ' + (', '.join(psu)))
		psu_label.grid(column=1, sticky='W', row=counter + 1)
 

warehouseFrame = ttk.LabelFrame(win, text=' Warehouse Information ') # 1
warehouseFrame.grid(column=1, sticky='WE', row=0, padx=5, pady=0)


load_setting_button = ttk.Button(warehouseFrame, text="Load", command=load)
load_setting_button.grid(column=1, row=1, padx=30, pady=10)

view_setting_button = ttk.Button(warehouseFrame, text="View", command=view)
view_setting_button.grid(column=2, row=1, padx=20, pady=10)


#order
def place_order():
	"""
        writes the order in a variable and prints it out as well in the GUI
    """
	order_string = scr.get(1.0, 99.0)
	placed_label = ttk.Label(orderFrame, text="Current Order: \n" + scr.get(1.0, 99.0))
	placed_label.grid(column=1, sticky='W', row=5, padx=10, pady=5)
	

orderFrame = ttk.LabelFrame(win, text=' Order ') # 1
orderFrame.grid(column=1,  sticky='NSWE', row=1, padx=5, pady=0)
	
order_label = ttk.Label(orderFrame, text="Please place your order!") 
order_label.grid(column=1, row=2, padx=10, pady=5)

scrolW = 20
scrolH = 5 
scr = scrolledtext.ScrolledText(orderFrame, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=1, sticky='WE', columnspan=2, padx=10, pady=5)

place_order_button = ttk.Button(orderFrame, text="Place this order", command=place_order)
place_order_button.grid(column=2, row=4, padx=5, pady=5)



"""Search Methods"""

#Button Action
def clickMe(butt, labe):
	
	"""
        marks one search method as selected and all others at not selected 
		writes the selected method into a global variable

        Args:
            butt (button): button of the search method
			labe (label): label of the search method
			
    """
		
	if butt.config('text')[-1] == '** Using **':
		butt.config(text='Use')
		labe.configure(foreground='black')
	else:
		butt.config(text='** Using **')
		global chosen_method
		chosen_method = labe.config('text')[-1]
		labe.configure(foreground='red')
		
		for i in range(len(button_list)):
			if button_list[i] != butt:
				button_list[i].config(text='Use')
				label_list[i].configure(foreground='black')
			else:
				continue
	


methodsFrame = ttk.LabelFrame(win, text=' Search Methods ') # 1
methodsFrame.grid(column=3, sticky='N', row=1, padx=5, pady=0)


#Hill Climbing
HC_label = ttk.Label(methodsFrame, text="Hill Climbing") # 5
HC_label.grid(column=4, row=0)

HC_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(HC_button, HC_label)) # 7
HC_button.grid(column=5, row=0) # 

#Fist Choice HC
FC_hc_label = ttk.Label(methodsFrame, text="First Choice Hill Climbing") # 5
FC_hc_label.grid(column=4, row=1)

FC_hc_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(FC_hc_button, FC_hc_label)) # using wrapper method to pass arguments to the command function
FC_hc_button.grid(column=5, row=1) # 

#Simmulated Annealing
SA_label = ttk.Label(methodsFrame, text="Simmulated Annealing") # 5
SA_label.grid(column=4, row=2)

SA_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(SA_button, SA_label)) # 7
SA_button.grid(column=5, row=2) # 

#Parallel Climbing
PC_label = ttk.Label(methodsFrame, text="Parallel Climbing") # 5
PC_label.grid(column=4, row=3)

PC_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(PC_button, PC_label)) # 7
PC_button.grid(column=5, row=3) # 

#Local Beam
LB_label = ttk.Label(methodsFrame, text="Local Beam") # 5
LB_label.grid(column=4, row=4)

LB_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(LB_button, LB_label)) # 7
LB_button.grid(column=5, row=4) # 

button_list = (HC_button, FC_hc_button, SA_button, PC_button, LB_button)
label_list = (HC_label, FC_hc_label, SA_label, PC_label, LB_label)

for child in methodsFrame.winfo_children():
	child.grid_configure(padx=15, pady=4)

	
"""OUTPUT"""

def solve():
	
	"""
        launches the search and prints out the solution n the method
		
    """
	
	selected = False
	for button in button_list:
		if button.config('text')[-1] == '** Using **':
			selected = True
		else:
			continue
			
	if selected == True:
		warning_label.configure(text='')
		
		to_print_out = bring_item(order,chosen_method,steps= 10000,n=4)
		
		solution_label = ttk.Label(methodsFrame, text=chosen_method + " gave you\nthe following solution: \n\n" + "LÖSUNG")
		solution_label.grid(column=4, sticky='W', row=7, padx=10, pady=5)
	
	else:
		warning_label.configure(foreground='red', text=' Please select \n a search method!')
		warning_label.grid(column=5, row=5)
		
#solution

solutionFrame = ttk.LabelFrame(methodsFrame, text=' Solution ') # 1
solutionFrame.grid(column=4, sticky='N', row=5, padx=5, pady=5)

solution_button = ttk.Button(solutionFrame, text="Go!", command=solve) # 7
solution_button.grid(column=4, row=6, sticky='WE', padx=5, pady=5) # 

warning_label = ttk.Label(methodsFrame, text='')



win.resizable(0, 0)
win.mainloop()