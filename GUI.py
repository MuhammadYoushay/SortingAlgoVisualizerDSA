import random
from tkinter import *
from tkinter import ttk
from buublesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort
from Insertionsort import insertion_sort
from Selectionsort import selection_sort

root = Tk()
#Adding title the display window.
root.title('Sorting Algorithm Visualiser')
#Defining the dimensions of the display window.
root.geometry('900x600+200+80')
#Setting the background of the display window.
root.config(bg='#01101c') #This is a color code for a shade of Blue.
data=[] # List created for data handling.
#This function is responsible for the visual display of the data set - creation pof bars at each iteration according to the algorithm.
def drawData(data,colorArray):
    canvas.delete("all") #Delete all the items on the foreground while leaving the background.
    # Defining the dimensions of canvas(black screen) where our graph bars will be displayed.
    canvas_height = 400
    canvas_width = 870
    x_width = canvas_width/(len(data)+1)
    offset = 10
    spacing= 10 #Define spacing between two bars.
    #Rescaling the data so that bars can be formed within the defined Canvas size.
    normalised_data = [i / max(data) for i in data]
    #Loop created for setting the size and generating data bars.
    for i, height in enumerate(normalised_data):
        x0 = i*x_width + offset + spacing
        y0 = canvas_height - height * 350
        #Setting the width of the bars.
        x1 = (i+1) * x_width
        #Setting the height of the bars.
        y1 = canvas_height
        #Creating the bar according to the selected width and height.
        canvas.create_rectangle(x0,y0, x1, y1, fill = colorArray[i])
        #Displaying text on the bar.
        canvas.create_text(x0+2, y0, anchor=SW, text = str(data[i]), font=("new roman", 15, "italic bold"), fill = "orange")
    #To do tasks in the queue.
    root.update_idletasks()
#Function created to call different sorting algorithms according to the user input.
def Start_Algorithm():
    global data
    #If no data is entered the program won't return anything.
    if not data:
        return
    #Calling Quick Sort
    if algo_menu.get()=='Quick Sort':
        quick_sort(data,0,len(data)-1,drawData,speedscale.get())
        drawData(data, ['green' for x in range(len((data)))])
    # Calling Bubble Sort
    elif algo_menu.get()=='Bubble Sort':
        bubble_sort(data,drawData,speedscale.get())
    # Calling Merge Sort
    elif algo_menu.get()=='Merge Sort':
        merge_sort(data,0,len(data)-1,drawData,speedscale.get())
        drawData(data, ['green' for x in range(len((data)))])
    # Calling Insertion Sort
    elif algo_menu.get()=='Insertion Sort':
        insertion_sort(data,drawData,speedscale.get())
        drawData(data, ['green' for x in range(len((data)))])
    # Calling Selection sort
    elif algo_menu.get()=='Selection Sort':
        selection_sort(data,drawData,speedscale.get())
        drawData(data, ['green' for x in range(len((data)))])


def Generate():
    global data
    #Getting the sorting algorithm which the user has selected.
    print("Selected Algorithm : " + selected_algorithm.get())
    #Getting the input from the Input list.
    lst=lstvalue.get()
    #Checking if the data list contains data or not.
    #If the input list contains data, data from this list would be transferred to to the our 'data' list which we initialized earlier.
    if len(lst)>1:
        data=lst.split(",")
        for i in range(0, len(data)):
            data[i] = int(data[i])
        #If the user input list is empty, we'll move on to check if there has been a random generation of data.
    else:
        #Getting the minimum value which the user has selected
        min_value = int(minvalue.get())
        # Getting the maximum value which the user has selected
        max_value = int(maxvalue.get())
        # Getting the size of values which has been selected by the user
        size_evalue = int(sizevalue.get())
        data = []
        for _ in range(size_evalue):
            # Random generation of data using the random function -- data would be generated of the size which the user has input and b/w the minimum and maximum value as provided by the user.
            data.append(random.randrange(min_value, max_value + 1))
    #Calling the drawData function for visualizing the data.
    drawData(data,['grey' for x in range(len(data))])


selected_algorithm = StringVar()
# Display the 'Algorithm' label at the top right of the screen.
mainlabel = Label(root, text = "Alogrithm : ", font = ("new roman", 16, "italic bold"), bg = '#05897A', width = 10, fg = "black", relief = GROOVE, bd = 5)
mainlabel.place(x=0,y=0)
# Creating a drop down list for the users to select their desired algorithms.
algo_menu = ttk.Combobox(root, width=15, font=('new roman', 19, "italic bold"), textvariable=selected_algorithm, values = ['Bubble Sort', 'Merge Sort', "Quick Sort","Insertion Sort","Selection Sort"])
algo_menu.place(x=145, y=0)
algo_menu.current(0)
#Button created which would display the randomly generated data.
random_generate = Button(root, text = "Visualize your Data", bg="#2DAE9A", font = ("arial",12,"italic bold"), relief = SUNKEN, activebackground="#05945B", activeforeground="white", bd = 5, width= 10, height=3,wraplength=80, command = Generate)
random_generate.place(x=760, y=100)
#Creating an input list where the user can enter data which they want to sort.
lstlabel=Label(root, text="Enter Data : ", font = ("new roman", 16, "italic bold"), bg = "#05897A", width=10, fg="black", relief=GROOVE, bd = 5)
lstlabel.place(x=400,y=0)
lstvalue=Entry(root,width=30)
lstvalue.place(x=546, y=9)
#Display a heading letting the users know that they have the option of random generation of data.
heading=Label(root,text="Use the functions below for Random Data Generation",font = ("new roman", 13, "italic bold"),fg="white",bg="#01101c", relief=FLAT, bd = 5)
heading.place(x=220,y=47)
heading1=Label(root,text="Input Format - 3,2,1,9...",font = ("new roman", 9, "italic bold"),fg="white",bg="#01101c", relief=FLAT, bd = 5)
heading1.place(x=546,y=28)
#Creating a label to let the users know that they have to enter the 'data size' here.
sizevaluelabel = Label(root, text="Size : ", font = ("new roman", 16, "italic bold"), bg = "#05897A", width=10, fg="black", relief=GROOVE, bd = 5)
sizevaluelabel.place(x=0, y=75)
#Creating the size button.
sizevalue = Scale(root,from_ = 0, to = 30, resolution=1, orient=HORIZONTAL, font = ("arial",14,"italic bold"), relief=GROOVE, bd = 2, width=10)
sizevalue.place(x=17,y=120)
#Creating a label to let the users know that they have to enter the 'minimum value' here.
minvaluelabel = Label(root, text="Min Value : ", font = ("new roman", 16, "italic bold"), bg = "#05897A", width=10, fg="black", relief=GROOVE, bd = 5)
minvaluelabel.place(x=200, y=75)
#Creating the minimum value button.
minvalue = Scale(root,from_ = 0, to = 10, resolution=1, orient=HORIZONTAL, font = ("arial",14,"italic bold"), relief=GROOVE, bd = 2, width=10)
minvalue.place(x=219,y=120)
#Creating a label to let the users know that they have to enter the 'maximum value' here.
maxvaluelabel = Label(root, text="Max Value : ", font = ("new roman", 16, "italic bold"), bg = "#05897A", width=10, fg="black", relief=GROOVE, bd = 5)
maxvaluelabel.place(x=400, y=75)
#Creating the maximum value button.
maxvalue = Scale(root,from_ = 0, to = 100, resolution=1, orient=HORIZONTAL, font = ("arial",14,"italic bold"), relief=GROOVE, bd = 2, width=10)
maxvalue.place(x=418,y=120)
#Creating the sort button. Pressing here would result in the running of the visualizer.
start = Button(root, text = "Sort", bg="#90ee90", font = ("arial",12,"italic bold"), relief = SUNKEN, activebackground="#05945B", activeforeground="white", bd = 5, width= 10, command=Start_Algorithm)
start.place(x=760, y=0)
def Close():
    root.destroy()
#Creating the send button. Pressing here would result in the closing of the program.
exit_button = Button(root, text="End", command=Close, bg="red", font = ("arial",12,"italic bold"), relief = SUNKEN, activebackground="#05945B", activeforeground="white", bd = 5, width= 10)
exit_button.place(x=760, y=50)
#Creating a label to let the users know that they can adjust their algorithm speed from here.
speedlabel = Label(root, text="Speed : ", font = ("new roman", 16, "italic bold"), bg = "#05897A", width=10, fg="black", relief=GROOVE, bd = 5)
speedlabel.place(x=590, y=75)
#Creatin a button to control speed.
speedscale = Scale(root,from_ = 0.1, to = 5.0, resolution=0.2, length=95, digits =2, orient=HORIZONTAL, font = ("arial",14,"italic bold"), relief=GROOVE, bd = 2, width=10)
speedscale.place(x=610,y=120)
#Creating the black screen where the data bars will appear.
canvas = Canvas(root, width=870, height = 400 , bg = "black")
canvas.place(x=15,y=180)

root.mainloop()