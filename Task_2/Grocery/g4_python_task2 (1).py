# -*- coding: utf-8 -*-
"""G4_python_Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vf9FJp4gM8CESdamVDaMLyq2RaBKLpcg
"""

import time
import os
import csv
grocery_dict = {
    "shop name" : "Market",
    "lists"     : ["banana", "apple", "rice", "oil"],
    "price"     : [25,        33,       85,     99],
    "stock"     : [3,         5,        9,      10],

}




customer = {
    "bag"       : [],
    "quantity"  : [],
    "prices"     : [],
}



print("--------------------------- welcome to ITI Market -----------------------------")
time.sleep(2)

TT = True
while TT :                        
  os.system("cls")
  print("Grocery owner  press 1 ")
  print("Customer       press 2 ")
  print("exit           press 0 ")
  print("---------------------------")

  x = int(input("Enter your choice: "))

  print("---------------------------")

  if x == 1:
    your = 3
    correct = 0
    flag = 1
    looping = True
    print("----------------- Welcome to grocery owner account ----------------------------")
    while looping:
      password = int(input("please enter your password: "))
      print("-------------------------------------------------------------")
      while (your != 0 and flag == 1):
        if password == 123:
          correct = 1
          flag = 0
        else:
          print("please try again")
          password = int(input("please enter your password: "))
        your -=1

      if (correct == 1):
        print("---------------------------------------")
        print("welcome back my friend!! ;)")
        print("---------------------------------------")
        looping2 = True
        while looping2:
          print("show all items press 1 ")
          print("add items      press 2 ")
          print("change price   press 3 ")
          print("finished       press 4 ")
          print("exit           press 0 ")
          print("---------------------------")
          y = int(input("Enter your choice: "))
          print("---------------------------")
          if y == 1:
            print("\n----------------- Your Lists ----------------------")
            print(grocery_dict["lists"])
            print("---------------------------------------------------\n")
          elif y == 2:
            z1 = input("Please add your items:  ")
            grocery_dict["lists"].append(z1)
            z2 = int(input("Please add items' price:  "))
            grocery_dict["price"].append(z2)
            z3 = int(input("Please add items quantity:  "))
            grocery_dict["stock"].append(z3)

            with open ('market.csv', 'w') as data:
              x = ['lists', 'price', 'stock']
              product = csv.DictWriter(data, fieldnames = x)
              product.writeheader()
              for i in range(len(grocery_dict["lists"])):
                product.writerow({"lists" : grocery_dict["lists"][i], "price" : grocery_dict["price"][i], "stock":grocery_dict["stock"][i]})


            print("----------------------------------")
            print(grocery_dict["lists"])
            print(grocery_dict["price"])
            print(grocery_dict["stock"])
            print("----------------------------------")
          elif y == 3 :
            print(grocery_dict["lists"])
            o = input("Which element do you want to change it's price:   ")
            price = int(input("What is the new price"))
            grocery_dict["price"][grocery_dict["lists"].index(o)] = price

            with open ('market.csv', 'a') as data:
                    fieldname = ['lists', 'price', 'stock']
                    product = csv.DictWriter(data, fieldnames = fieldname)
                    product.writeheader()
                    for i in range(len(grocery_dict["lists"])):
                      product.writerow({"lists" : grocery_dict["lists"][i], "price" : grocery_dict["price"][i], "stock":grocery_dict["stock"][i]})

          elif y == 4:
            looping = False
            looping2 = False
          else:
            TT = False
            looping = False 
            looping2 = False       

      elif (correct == 0):
        print("your account is blocked")
        looping = False

  elif x == 2 :
    print("you want to buy element  press 1 ")
    print("Exit                     press 0 ")
    print("---------------------------")
    choice = int(input("Enter your choice: "))
    print("---------------------------")
    if choice == 1 :
      print(grocery_dict["lists"])
      print(grocery_dict["stock"])
      loop = True
      while loop:
        print("-------------------------------------")
        print("-------------------------------------")
        print("Continue buying  press 1")
        print("print bills      press 2")
        print("Finished         press 0")
        buy = int(input("your choice:  "))
        print("-------------------------------------")
        print("-------------------------------------")
        if buy == 1:
          element = input("Enter your element:  ")
          customer["bag"].append(grocery_dict["lists"][grocery_dict["lists"].index(element)])
          print(customer["bag"])
          quantity = int(input("Enter your quantity of this element:  "))
          customer["quantity"].append(quantity)
          grocery_dict["stock"][grocery_dict["lists"].index(element)] -= quantity
          print(grocery_dict["stock"])
          customer["prices"].append(grocery_dict["price"][grocery_dict["lists"].index(element)] * quantity)
          print(customer["prices"])



        elif buy == 2:
          with open("bag.csv", "w") as bag:
            field = ["Bag", "Quantity", "Price"]
            bags = csv.DictWriter(bag, fieldnames= field)
            bags.writeheader()
            for j in range(len(customer["bag"])):
               bags.writerow({"Bag" : customer["bag"][j], "Quantity" : customer["quantity"][j], "Price":customer["prices"][j]})

          recipe = open("recipe.txt", "w")
          recipe.write("---------------------------------------------\n")
          recipe.write("-------- Welcome to ITI market ------------- \n")
          recipe.write("---------------------------------------------\n")
          data1 = csv.reader(open("bag.csv", "r"))
          for line in data1:
            recipe.write("|| " + line[0] + " ||\t\t|| " + line[1] + " ||\t\t|| " + line[2] + "|| \n")
            #recipe.writelines(line)
            break
          recipe.write("---------------------------------------------\n")
          for jj in range(len(customer["bag"])):
            recipe.write("\t" +  customer["bag"][jj] + "\t\t\t\t\t\t\t" + str(customer["quantity"][jj]) + "    \t\t\t\t\t" + str(customer["prices"][jj]) + "\n")



          bills = 0
          print(len(customer["bag"]))
          for i in range(len(customer["bag"])):
            bills += grocery_dict["price"][grocery_dict["lists"].index(customer["bag"][i])] * customer["quantity"][i]
            print(bills)

          recipe.write("---------------------------------------------\n")
          recipe.write(">>>> Total price: " + str(bills) + "                       *" + "\n")
          recipe.write("---------------------------------------------\n")
          recipe.write("Thank you for shopping\n")
          recipe.write("                        HAVE A NICE DAY  :)  \n")
          recipe.write("#############################################\n")

        elif buy == 0:
          loop = False

    else:
      TT = False


  else:
    TT = False

recipe = open("recipe.txt", "w")
recipe.write("---------------------------------------------\n")
recipe.write("-------- Welcome to ITI market ------------- \n")
recipe.write("---------------------------------------------\n")
data1 = csv.reader(open("bag.csv", "r"))
for line in data1:
  recipe.write("|| " + line[0] + " ||\t\t|| " + line[1] + " ||\t\t|| " + line[2] + "|| \n")
  #recipe.writelines(line)
  break
recipe.write("---------------------------------------------\n")
for jj in range(len(customer["bag"])):
  recipe.write("\t" +  customer["bag"][jj] + "\t\t\t\t\t\t\t" + str(customer["quantity"][jj]) + "    \t\t\t\t\t" + str(customer["prices"][jj]) + "\n")

recipe.write("---------------------------------------------\n")
recipe.write(">>>> Total price: " + str(bills) + "                       *" + "\n")
recipe.write("---------------------------------------------\n")
recipe.write("Thank you for shopping\n")
recipe.write("                        HAVE A NICE DAY  :)  \n")
recipe.write("#############################################\n")