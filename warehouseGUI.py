import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
from warehouse import Warehouse
from wh_reader import WHreader
#from wh_search import 

win = tk.Tk()
win.title("Warehouse Calculator")

##################################################################################
### Warehouse information ###
### top left frame ###

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
 

# design #
warehouseFrame = ttk.LabelFrame(win, text=' Warehouse Information ') # 1
warehouseFrame.grid(column=1, sticky='WE', row=0, padx=5, pady=0)

load_setting_button = ttk.Button(warehouseFrame, text="Load", command=load)
load_setting_button.grid(column=1, row=1, padx=30, pady=10)

view_setting_button = ttk.Button(warehouseFrame, text="View", command=view)
view_setting_button.grid(column=2, row=1, padx=20, pady=10)



##################################################################################
### Order ###
### bottom left frame ###

def load_order():
	ordername = filedialog.askopenfilename(parent=win)
	order_file = open(ordername)
	global read_order
	read_order = WHreader(ordername)
	
def place_order():
	"""
        writes the order in a variable and prints it out as well in the GUI
    """
	order_string = scr.get(1.0, 99.0)
	global print_order
	if len(order_string) != 1:
		print_order = order_string
	else:
		global read_order
		print_order = (', '.join(read_order.stock))
	
	#global final_order
	#final_order = print_order
	placed_label.configure(text="Current Order: \n" + print_order)
	
	
# design #
orderFrame = ttk.LabelFrame(win, text=' Order ') # 1
orderFrame.grid(column=1,  sticky='NSWE', row=1, padx=5, pady=0)
	
order_label = ttk.Label(orderFrame, text="Please type in OR load your order!") 
order_label.grid(column=1, row=2, padx=10, pady=5)

scrolW = 20
scrolH = 5 
scr = scrolledtext.ScrolledText(orderFrame, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=1, sticky='WE', columnspan=2, padx=10, pady=5)

load_order_button = ttk.Button(orderFrame, text="Load order", command=load_order)
load_order_button.grid(column=1, row=4, padx=5, pady=5)

place_order_button = ttk.Button(orderFrame, text="Place this order", command=place_order)
place_order_button.grid(column=2, row=4, padx=5, pady=5)

placed_label = ttk.Label(orderFrame, text='')
placed_label.grid(column=1, sticky='W', row=5, padx=10, pady=5)

##################################################################################
### Search Method ###
### top right frame ###


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
	


# design #

methodsFrame = ttk.LabelFrame(win, text=' Search Methods ') # 1
methodsFrame.grid(column=3, sticky='N', row=1, padx=5, pady=0)

#Hill Climbing
HC_label = ttk.Label(methodsFrame, text="Hill Climbing") # 5
HC_label.grid(column=4, row=0)

HC_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(HC_button, HC_label))
HC_button.grid(column=5, row=0)

#Fist Choice HC
FC_hc_label = ttk.Label(methodsFrame, text="First Choice Hill Climbing")
FC_hc_label.grid(column=4, row=1)

FC_hc_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(FC_hc_button, FC_hc_label)) # using wrapper method to pass arguments to the command function
FC_hc_button.grid(column=5, row=1)

#Simmulated Annealing
SA_label = ttk.Label(methodsFrame, text="Simmulated Annealing")
SA_label.grid(column=4, row=2)

SA_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(SA_button, SA_label))
SA_button.grid(column=5, row=2)

#Random Restart Climbing
RR_label = ttk.Label(methodsFrame, text="Random Restart Climbing")
RR_label.grid(column=4, row=3)

RR_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(RR_button, RR_label))
RR_button.grid(column=5, row=3)

RR_k_label = ttk.Label(methodsFrame, text="k = ")
RR_k_label.grid(column=6, row=3)

RR_k = tk.StringVar()
RR_k_button = ttk.Entry(methodsFrame, width=3, textvariable=RR_k)
RR_k_button.grid(column=7, row=3) 

#Local Beam
LB_label = ttk.Label(methodsFrame, text="Local Beam")
LB_label.grid(column=4, row=4)

LB_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(LB_button, LB_label))
LB_button.grid(column=5, row=4)

LB_k_label = ttk.Label(methodsFrame, text="k = ")
LB_k_label.grid(column=6, row=4)

LB_k = tk.StringVar()
LB_k_button = ttk.Entry(methodsFrame, width=3, textvariable=LB_k)
LB_k_button.grid(column=7, row=4) 

button_list = (HC_button, FC_hc_button, SA_button, RR_button, LB_button)
label_list = (HC_label, FC_hc_label, SA_label, RR_label, LB_label)

for child in methodsFrame.winfo_children():
	child.grid_configure(padx=15, pady=4)

	
##################################################################################
### Output ###
### bottom right frame ###

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
		if chosen_method == 'Random Restart Climbing':
			chosen_method = 'rr'
			n = RR_k
		elif chosen_method == 'Local Beam':
			chosen_method = 'lbs'
			n = LB_k
		elif chosen_method == 'First Choice Hill':
			chosen_method = 'fch'
			n = None
		elif chosen_method == 'Simmulated Annealing':
			chosen_method = 'sa'
			n = None
		else:
			chosen_method = 'hc'
			n = None

		global whouse_object
		to_print_out = whouse_object.bring_item(print_order,chosen_method, n)
		
		solution_label = ttk.Label(methodsFrame, text=chosen_method + " gave you\nthe following solution: \n\n" + (', '.join(to_print_out)))
		solution_label.grid(column=4, sticky='W', row=7, padx=10, pady=5)
		
	else:
		warning_label.configure(foreground='red', text=' Please select \n a search method!')
		warning_label.grid(column=5, row=5)

		
# design #

solutionFrame = ttk.LabelFrame(methodsFrame, text=' Solution ') # 1
solutionFrame.grid(column=4, sticky='N', row=5, padx=5, pady=5)

solution_button = ttk.Button(solutionFrame, text="Go!", command=solve) # 7
solution_button.grid(column=4, row=6, sticky='WE', padx=5, pady=5) # 

warning_label = ttk.Label(methodsFrame, text='')



win.resizable(0, 0)
win.mainloop()