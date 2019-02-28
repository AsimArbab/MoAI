import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
from warehouse import Warehouse
from wh_reader import WHreader

win = tk.Tk()
win.title("Warehouse Calculator")

##################################################################################
### Warehouse information ###
### top left frame ###
### Here you can open and load a file, that contains your warehouse setting and 
### review the current loaded setting in a new window. 

def load():
	"""
        opens a load dialogue window to load a file and creates a WHreader and a Warehouse object
    """
	filename = filedialog.askopenfilename(parent=win)
	global read_setting
	read_setting = WHreader(filename)	#read in the content of the file
	global whouse_object # create an actual warehouse object with the content of the file
	whouse_object = Warehouse(WHreader(filename).stock, WHreader(filename).psus)
   
def view():
	"""
        view the current warehouse setting in a different window
    """
	view_win = tk.Tk() # open a new window
	stock_label = ttk.Label(view_win, text= 'Stock: ' + (', '.join(read_setting.stock))) # display the different items in stock
	stock_label.grid(column=1, row=0)
	psu_label = ttk.Label(view_win, text= 'PSUs:')
	psu_label.grid(column=1, sticky='W', row=1)
	counter = 0 #number counter for naming the PSUs
	for psu in read_setting.psus:	# display the list of PSUs with their respective content
		counter += 1
		psu_label = ttk.Label(view_win, text= 'PSU ' + str(counter) + ': ' + (', '.join(psu)))
		psu_label.grid(column=1, sticky='W', row=counter + 1)
 

# design #
#ttk.Label creates labels
#ttk.Button creates buttons with text and command on click
#___.grid defines the place arrangement in the GUI 

warehouseFrame = ttk.LabelFrame(win, text=' Warehouse Information ') # create frame
warehouseFrame.grid(column=1, sticky='WE', row=0, padx=5, pady=0) # place frame

load_setting_button = ttk.Button(warehouseFrame, text="Load", command=load)
load_setting_button.grid(column=1, row=1, padx=30, pady=10)

view_setting_button = ttk.Button(warehouseFrame, text="View", command=view)
view_setting_button.grid(column=2, row=1, padx=20, pady=10)



##################################################################################
### Order ###
### bottom left frame ###
### Here an order can be placed by typing it in by hand, loading it from a file and subsequently pushing it to the program.

def load_order():
	"""
        loads an order from a file
    """
	global ordername
	ordername = filedialog.askopenfilename(parent=win)
	
	
def write_order():
	"""
		attaches the order to the warehouse object and prints it out in the GUI
    """
	global order
	order = whouse_object.place_order(ordername)
	read_order = WHreader(ordername) #read in the content of the file
	#print_order = (', \n'.join(read_order.stock))
	
	placed_label.configure(text="Current Order: \n" + (', \n'.join(read_order.stock))) # prints out the current order in the GUI, while each time updating the label, instead of creating a new one
	
	
# design #
#ttk.Label creates labels
#ttk.Button creates buttons with text and command on click
#___.grid defines the place arrangement in the GUI 

orderFrame = ttk.LabelFrame(win, text=' Order ') # create frame
orderFrame.grid(column=1,  sticky='NSWE', row=1, padx=5, pady=0) # place frame
	
order_label = ttk.Label(orderFrame, text="Please load your order!") 
order_label.grid(column=1, row=2, padx=10, pady=5)

load_order_button = ttk.Button(orderFrame, text="Load order", command=load_order)
load_order_button.grid(column=1, row=4, padx=5, pady=5)

place_order_button = ttk.Button(orderFrame, text="Place this order", command=write_order)
place_order_button.grid(column=2, row=4, padx=5, pady=5)

placed_label = ttk.Label(orderFrame, text='')
placed_label.grid(column=1, sticky='W', row=5, padx=10, pady=5)



##################################################################################
### Search Method ###
### top right frame ###
### Here a single search method has to be selected. For Random Restart Climbing and Local Beam Search a k can be entered

def clickMe(butt, labe):
	
	"""
        marks one search method as selected and all others at not selected --> creates a toggle button
		writes the selected method into a global variable

        Args:
            butt (button): button of the search method
			labe (label): label of the search method
			
    """
		
	if butt.config('text')[-1] == '** Using **': 		# if the text of the button is '**Using**' 
		butt.config(text='Use') 						# revert it back to 'Use'
		labe.configure(foreground='black')				# colour the label black
	else:
		butt.config(text='** Using **')					# otherwise set the text to '**Using**'
		labe.configure(foreground='red')				# colour the label red
		global chosen_method							
		chosen_method = labe.config('text')[-1]			# save the selected search method as chosen_method in looking at the label of the button that was clicked				
		
		for i in range(len(button_list)):				# turn all other buttons off
			if button_list[i] != butt:
				button_list[i].config(text='Use')
				label_list[i].configure(foreground='black')
			else:
				continue
				

# design #
#ttk.Label creates labels
#ttk.Button creates buttons with text and command on click
#___.grid defines the place arrangement in the GUI 

methodsFrame = ttk.LabelFrame(win, text=' Search Methods ') # creates frame
methodsFrame.grid(column=3, sticky='N', row=1, padx=5, pady=0) # places frame

#Hill Climbing
HC_label = ttk.Label(methodsFrame, text="Hill Climbing")
HC_label.grid(column=4, row=0)

HC_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(HC_button, HC_label)) # using wrapper method to pass arguments to the command function
HC_button.grid(column=5, row=0)

HC_steps_label = ttk.Label(methodsFrame, text="steps = ")
HC_steps_label.grid(column=6, row=0)

HC_steps = tk.IntVar() # creating integer variable HC_steps
HC_steps_button = ttk.Entry(methodsFrame, width=3, textvariable=HC_steps) # creating a text box widget and pushing the content to the integer variable HC_steps
HC_steps_button.grid(column=7, row=0) 

#Fist Choice HC
FC_hc_label = ttk.Label(methodsFrame, text="First Choice Hill Climbing")
FC_hc_label.grid(column=4, row=1)

FC_hc_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(FC_hc_button, FC_hc_label)) 
FC_hc_button.grid(column=5, row=1)

FC_steps_label = ttk.Label(methodsFrame, text="steps = ")
FC_steps_label.grid(column=6, row=1)

FC_steps = tk.IntVar() # creating integer variable FC_steps
FC_steps_button = ttk.Entry(methodsFrame, width=3, textvariable=FC_steps) 
FC_steps_button.grid(column=7, row=1) 

#Simmulated Annealing
SA_label = ttk.Label(methodsFrame, text="Simmulated Annealing")
SA_label.grid(column=4, row=2)

SA_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(SA_button, SA_label))
SA_button.grid(column=5, row=2)

SA_steps_label = ttk.Label(methodsFrame, text="steps = ")
SA_steps_label.grid(column=6, row=2)

SA_steps = tk.IntVar() # creating integer variable SA_steps
SA_steps_button = ttk.Entry(methodsFrame, width=3, textvariable=SA_steps) 
SA_steps_button.grid(column=7, row=2)

#Random Restart Climbing
RR_label = ttk.Label(methodsFrame, text="Random Restart Climbing")
RR_label.grid(column=4, row=3)

RR_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(RR_button, RR_label))
RR_button.grid(column=5, row=3)

RR_steps_label = ttk.Label(methodsFrame, text="steps = ")
RR_steps_label.grid(column=6, row=3)

RR_steps = tk.IntVar() # creating integer variable RR_steps
RR_steps_button = ttk.Entry(methodsFrame, width=3, textvariable=RR_steps) 
RR_steps_button.grid(column=7, row=3) 

RR_k_label = ttk.Label(methodsFrame, text="k = ")
RR_k_label.grid(column=8, row=3)

RR_k = tk.IntVar() # creating integer variable RR_k
RR_k.set(4) # set default to 4
RR_k_button = ttk.Entry(methodsFrame, width=3, textvariable=RR_k) # creating a text box widget and pushing the content to the integer variable RR_k
RR_k_button.grid(column=9, row=3) 

#Local Beam
LB_label = ttk.Label(methodsFrame, text="Local Beam")
LB_label.grid(column=4, row=4)

LB_button = ttk.Button(methodsFrame, text="Use", command= lambda: clickMe(LB_button, LB_label))
LB_button.grid(column=5, row=4)

LB_steps_label = ttk.Label(methodsFrame, text="steps = ")
LB_steps_label.grid(column=6, row=4)

LB_steps = tk.IntVar() # creating integer variable LB_steps
LB_steps_button = ttk.Entry(methodsFrame, width=3, textvariable=LB_steps) 
LB_steps_button.grid(column=7, row=4) 

LB_k_label = ttk.Label(methodsFrame, text="k = ")
LB_k_label.grid(column=8, row=4)

LB_k = tk.IntVar() # creating integer variable LB_k
LB_k.set(4) # set default to 4
LB_k_button = ttk.Entry(methodsFrame, width=3, textvariable=LB_k) # creating a text box widget and pushing the content to the integer variable LB_k
LB_k_button.grid(column=9, row=4) 


# list of all buttons and labels to loop over when switching all of but the selected one 
button_list = (HC_button, FC_hc_button, SA_button, RR_button, LB_button)
label_list = (HC_label, FC_hc_label, SA_label, RR_label, LB_label)

for child in methodsFrame.winfo_children(): # for every widget in the Method Frame
	child.grid_configure(padx=15, pady=4)  	# add padding of 15x4 pixel

	
##################################################################################
### Output ###
### bottom right frame ###

def solve():
	
	"""
        launches the search and prints out the solution and the method
		
    """
	
	selected = False 
	for button in button_list:  # detect if a method has been selected by checking if the text of any button is '**Using**'
		if button.config('text')[-1] == '** Using **':
			selected = True
		else:
			continue
			
	if selected == True:	# if a method was selected
		warning_label.configure(text='')	# reset warning label
		global chosen_method		# look up which method was chosen
		if chosen_method == 'Random Restart Climbing':	# set arguments for the bring_item method
			method = 'rr'
			k = RR_k.get()
			steps = RR_steps.get()
		elif chosen_method == 'Local Beam':
			method = 'lbs'
			k = LB_k.get()
			steps = LB_steps.get()
		elif chosen_method == 'First Choice Hill':
			method = 'fch'
			k = None
			steps = FC_steps.get()
		elif chosen_method == 'Simmulated Annealing':
			method = 'sa'
			k = None
			steps = SA_steps.get()
		else:
			method = 'hc'
			k = None
			steps = HC_steps.get()

		global whouse_object
		result = whouse_object.bring_item(order, method, k, steps) # calculate the SOLUTION with the warehouse object, the current order, the chosen_method and the k (if existent)
		
		PSUamount= str(len(result)) # how many PSUs were used
		solution_label = ttk.Label(methodsFrame, text=chosen_method + " gave you the following solution: \nDetails: \n\n" + PSUamount +" PSU(s) were moved.") # print out information about the solution
		solution_label.grid(column=4, sticky='W', row=7, padx=10, pady=5)
		
		psu_list = []
		for psu in result: # create a list of all PSUs in the result and their content
			name = psu.get_name()
			inventar = str(psu.get_inventory())
			print(name+" mit folgende items: "+inventar)
			psu_list.append(name+" with the following items: "+inventar+'\n')
			scr_psu.delete(1.0, 9999.0)
			scr_psu.insert(1.0, ''.join(psu_list))
		

	else:  		# if not method was selected, show warning message to please select a method
		warning_label.configure(foreground='red', text=' Please select \n a search method!')
		warning_label.grid(column=5, row=5)

		
# design #
#ttk.Label creates labels
#ttk.Button creates buttons with text and command on click
#___.grid defines the place arrangement in the GUI 

solutionFrame = ttk.LabelFrame(methodsFrame, text=' Solution ') # create frame
solutionFrame.grid(column=4, sticky='N', row=5, padx=5, pady=5) # place frame

solution_button = ttk.Button(solutionFrame, text="Go!", command=solve)
solution_button.grid(column=4, row=6, sticky='WE', padx=5, pady=5)

warning_label = ttk.Label(methodsFrame, text='')

scrolW = 20 # height and width of the scrolled text widget
scrolH = 5 
scr_psu = scrolledtext.ScrolledText(methodsFrame, width=scrolW, height=scrolH, wrap=tk.WORD) # create scrolled text widget
scr_psu.grid(column=4, sticky='WE', row=8, columnspan=4, padx=10, pady=5) # place widget

win.resizable(0, 0) # window size can not be changed by the user
win.mainloop()