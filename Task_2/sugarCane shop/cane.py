from tkinter import *
from PIL import ImageTk, Image
import os


L = 0
M = 0
S = 0

def large():
	os.system("cls")
	global L
	price = 10
	large.counter+=1
	result = price * large.counter
	L = result
	print("number of large cup",str(large.counter),"your price is: " , result , "EGP")
large.counter =0


def medium():
	os.system("cls")
	global M
	price = 8
	medium.counter+=1
	result = price * medium.counter
	M = result
	print("number of medium cup",str(medium.counter),"your price is: " , result , "EGP")
medium.counter =0


def small():
	os.system("cls")
	global S
	price = 5
	small.counter+=1
	result = price * small.counter
	S = result
	print("number of small cup",str(small.counter),"your price is: " , result , "EGP")
small.counter =0


def finish():
	
	result = S + M + L
	print("Your total cost is ", result, "EGP :)")
	large.counter = 0
	medium.counter = 0
	small.counter = 0




window_1 = Tk()

window_1.title("Cane Shop")

window_1.geometry('600x600')


string_var = StringVar()
pass_var = StringVar()

def submit():
	name = string_var.get()
	password = pass_var.get()
	
	
	if (name == "b" and password == "b"):
		window_1.destroy()
		window_2 = Tk()
		window_2.title("Cane Shop")
		window_2.geometry('1000x800')
		frame = Frame(window_2, width = 500, height = 500)
		frame.pack()
		frame.place(anchor='center', relx=0.5, rely=0.5)
		imgg = ImageTk.PhotoImage(Image.open("cane.jpg"))
		label_img2 = Label(frame, image = imgg).pack()
		label_21 = Label(window_2, text = "  H e l l o, B a s s e l  ", font = ("Freestyle Script", 50), bg = "grey26", fg = "DarkGoldenrod2" ).place(x = 320, y = 100)
		
		button_2 = Button(window_2, text = "Close", bd = '5',bg = "burlywood4", command = window_2.destroy ).place(x = 0, y = 0)
		
		
		photo_1 = PhotoImage(file = 'glass.png')
		photo_2 = PhotoImage(file = 'glass.png')
		photo_3 = PhotoImage(file = 'glass.png')
		
		photo_1 = photo_1.subsample(5,5)
		photo_2 = photo_2.subsample(5,5)
		photo_3 = photo_3.subsample(5,5)
		
		button_3 = Button(window_2, image = photo_1, command = large).place(x = 50, y = 400)
		button_4 = Button(window_2, image = photo_2, command = medium).place(x = 350, y = 400)
		button_5 = Button(window_2, image = photo_3, command = small).place(x = 650, y = 400)
		button_6 = Button(window_2, text = "Cost", bd = '5', bg = "green", command = finish ).place(x=50, y = 650)
		
		labelT1 = Label(window_2, text = " Large cup " , bg = "saddle brown", fg = "DarkGoldenrod1" , font = ("Freestyle Script",30 )).place(x = 143, y = 330)
		labelT2 = Label(window_2, text = " Price: 10 EGP " , bg = "saddle brown", fg = "DarkGoldenrod1" , font = ("Freestyle Script",20 )).place(x = 140, y = 580)

		labelT1 = Label(window_2, text = " Medium cup " , bg = "saddle brown", fg = "DarkGoldenrod1" , font = ("Freestyle Script",30 )).place(x = 443, y = 330)
		labelT2 = Label(window_2, text = " Price: 8 EGP " , bg = "saddle brown", fg = "DarkGoldenrod1" , font = ("Freestyle Script",20 )).place(x = 440, y = 580)		

		labelT1 = Label(window_2, text = " Small cup " , bg = "saddle brown", fg = "DarkGoldenrod1" , font = ("Freestyle Script",30 )).place(x = 743, y = 330)
		labelT2 = Label(window_2, text = " Price: 5 EGP " , bg = "saddle brown", fg = "DarkGoldenrod1" , font = ("Freestyle Script",20 )).place(x = 740, y = 580)		
		
		window_2.mainloop()
		
	elif(name != "b" and password == "b"):
		label21 = Label(window_1,text = "         Wrong username                ", bg = "red", fg = "black").place(x = 300, y = 410)
		print("wrong password or Username please try again!!!..")
	elif (password != "b" and name == "b"):
		label22 = Label(window_1,text = "         Wrong password                ", bg = "red", fg = "black").place(x = 300, y = 410)
	else:
		label23 = Label(window_1,text = "                Wrong username and password           ", bg = "red", fg = "black").place(x = 250, y = 410)
	
	print("your name is: " + name)
	print("your password is : " + password)
	
	string_var.set("")
	pass_var.set("")
	



# frame = Frame(window_1, width=300, height=300)
# frame.pack()
# frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("cane.jpg"))

label_img = Label(window_1, image = img).pack()
#label_33 = Label(window_1, text = "Welcome to our shop",background = "grey26", fg = "DarkGoldenrod2", font = ("Times New Roman", 20) ).pack(side = TOP)



label_user 	= Label(window_1, text = "username",bg = "black", fg= "white" ,font = ("Times New Roman", 10, 'bold')).place(x = 230, y = 300)
entry_1 	= Entry(window_1, textvariable = string_var ,bg = "black", fg= "white" , font = ("Times New Roman", 10, 'bold')).place(x = 300, y = 300 )

label_pass 	= Label(window_1, text = "password", bg = "black" , fg= "white", font = ("Times New Roman", 10, 'bold') ).place(x = 230, y = 330)
entry_2 	= Entry(window_1, textvariable = pass_var ,bg = "black", fg= "white" , font = ("Times New Roman", 10, 'bold'), show = '*').place(x = 300, y = 330)

sub_but 	= Button(window_1, text = "log in", bd = '3', command = submit).place(x = 300, y = 370)


label_33 = Label(window_1, text = "Welcome to ITI cane shop",background = "grey26", fg = "DarkGoldenrod2", font = ("Times New Roman", 10) ).pack(side = TOP)






button_1 = Button(window_1, text = "Close", bd = '5',bg = "burlywood4", command = window_1.destroy ).place(x = 0, y = 0)


window_1.mainloop()