import pandas as pd
from collections import deque

pk = pd.read_csv("pak.csv")
jp = pd.read_csv("japan.csv")
italy = pd.read_csv("italy.csv")
grk = pd.read_csv("greek.csv")
china = pd.read_csv("china.csv")
account = pd.read_csv("accounts_info.csv")

# Starting of the main program.
class personal_info():
    def __init__(self):

        while True:            
            while True:
                try:
                    self.Name = str(input("Enter your name: "))
                    break
                except:
                    print("Wrong datatype, Try again! ")
                    pass

            while True:
                try:
                    self.Age = eval(input("Enter your age: "))
                    break
                except:
                    print("Wrong datatype, Try again! ")    
    
            while True:
                self.Email = input("Enter your Email: ")
                self.same_Email = account[account['Email'] == self.Email]
                if self.same_Email.empty == False:
                    print("Email already exists, please try again. ")
                else:
                    break
            while True:
                self.Phone_no = input("Enter your Contact Number: ")
                if self.Phone_no[0] == "0":
                    break
                else:
                    print("Try again! ")
            self.City= input("Enter the name of your city: ")
            self.Password=input("Set a strong password: ")
            
            account_dict = {'Name': self.Name , 'Age': self.Age , 'Email': self.Email,
            "Phone number": self.Phone_no, "City": self.City , 'Password' : self.Password}        
            account.loc[len(account)] = account_dict
            account.to_csv("accounts_info.csv", index=False)
            print("---------------------------")
            print("    ~ ACCOUNT CREATED ~ ")
            print("---------------------------")
            break

class main_interface():
    def call(self):
        outer_most_loop =True
        while outer_most_loop:
            print("---------------------------")
            print("|  ACCOUNT REG INTERFACE  |")
            print("---------------------------")
            print("| Already have an account?|")
            print("|     Login       [y]     | \n|     Register    [n]     | \n|     Don't Login [l]     | ")
            print("---------------------------")  
            acc_choice=input("Enter your choice: ")
            print("---------------------------")
            infinite_loop = True
            while infinite_loop:
              if acc_choice.lower() == 'y':
                      checkEmail = input("Enter your Email:\n    ") 
                      checkPassword = input("--------------------------- \nPassword:\n     ")              #To check match the password and email of a specific row
                        
                      Emailcheck = account[account['Email'] == checkEmail]        #At this time it is randomnly checking the pass and email of random rows
                      passcheck = Emailcheck[Emailcheck['Password'] == checkPassword]
                      if Emailcheck.empty | passcheck.empty:
                          print("Account not found / Incorrect Email OR Password !")
                          acc_choice= input("Try again [y] / Register Now [n] / Don't Login [l] :")
                          
                          if acc_choice.lower() == "y":
                              pass
                          
                          elif acc_choice.lower() == "n":
                              info = personal_info()
                              self.logged_in = "True"
                              outer_most_loop = False
                              
                              break
                          
                          elif acc_choice.lower() == "l":
                              self.logged_in = "False"
                              infinite_loop = False
                              outer_most_loop = False
                              
                          else:
                              print("Invalid Option ! ")
                      
                      elif not( passcheck.empty & Emailcheck.empty):
                          print("---------------------------")
                          print("       ~ LOGGED IN ~       ")
                          print("---------------------------")
                          self.logged_in = "True"
                          infinite_loop = False
                          outer_most_loop = False

                      else:
                          pass     

              elif acc_choice.lower() == 'n':
                  info = personal_info()
                  print("---------------------------")
                  print("       ~ LOGGED IN ~       ")
                  print("---------------------------")
                  infinite_loop = False
                  outer_most_loop = False
                  self.logged_in = "True"
                  break

              elif acc_choice.lower() == 'l':
                  self.logged_in = "False"
                  infinite_loop = False
                  outer_most_loop = False
                  
              else:
                  print("---------------------------")
                  print("The option doesn't exists ! ")
                  print("---------------------------")
                  self.logged_in = "False"
                  infinite_loop=False

    def generate_bill(self,bill):
      if self.logged_in=="True":  
        bill_per=float(bill*0.1)
        bill=bill-bill_per
        print("The discounted amount to be paid is",bill)
      elif self.logged_in=="False":
        print("No discount for you! Nikalo paisay! ")
        print("The total amount to be paid is",bill)
  

class T_Node():
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Trees():
    def __init__(self):
        self.root=None

class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class linkedlist():

  def __init__(self):
    self.head = None
    
  def confirm(self):
    self.flag1=True
    if self.flag1==True:
      bill = 0
      self.deq = deque()
      if len(stack)==0:
        print("Your Cart is empty! ")
        self.flag1=False

      for i in range(len(stack)):
        dict={}
        popped_value=stack.pop()
        
        dict[nstack.pop()] = popped_value
        self.deq.appendleft(dict)

      for i in range(len(self.deq)):
        popped_item = self.deq.pop()
        print(popped_item)
        
        while True:
          while True:
            try:  
              print("[1] Confirm item\n[2] Discard Item")
              user_choice273 = eval(input("Enter your choice: "))
              break
            except:
              print("Invalid Input")
          if user_choice273 == 1:
            self.deq.appendleft(popped_item)
            bill = bill + list(popped_item.values()).pop()
            break       
          elif user_choice273 == 2:
            print("Item discarded!")
            break
          else:
            print("Invalid Input, Try again.")

      if len(list(self.deq))!=0:
        c_q.append(list(self.deq))
        print(c_q) # Why are we printing the orders of all the customers?
      if self.flag1==True:
        print("The total amount to be paid is",bill) # Why are we printing this before the account registeration interface?
        acc=main_interface()
        acc.call()
        acc.generate_bill(bill)
      


  def next(self):
    self.head = self.head.next
  
  def prev(self):
    self.head = self.head.prev
  
  def select(self):
    tree=Trees()
    tree.root=T_Node(self.head.data)

    if tree.root.data == 'Pakistani Cuisine':
      tree.root.left = T_Node(pk)
    elif tree.root.data == 'Italian Cuisine':
      tree.root.left = T_Node(italy)
    elif tree.root.data == 'Chinese Cuisine':
      tree.root.left = T_Node(china)
    elif tree.root.data == 'Greek Cuisine':
      tree.root.left = T_Node(grk)
    elif tree.root.data == 'Japanese Cuisine':
      tree.root.left = T_Node(jp)
    
    print(tree.root.left.data[['Name','price']])

    run_cat=True
    while run_cat:
      print("[1] Order\n[2] Filter by Category\n[3] Return")
      user_choice = eval(input("Enter your choice: "))
      print(tree.root.left.data)
      if user_choice == 1:
        while True:
            try:
                while True:
                    try:
                        search = int(input("Order using Product ID : "))
                        break
                    except:
                        print("Invalid datatype, Kindly enter a valid datatype ")
                product = tree.root.left.data[tree.root.left.data['Product ID'] == search]
                price = int(product['price'])
                name = list(product['Name'])
                nstack.append(name.pop())
                stack.append(price)
                print("Product name: ",nstack)
                print("Product price: ",stack)
                break
            except:
                print("Product not found, Try again! ")

      elif user_choice == 2:  
 
          run_again=True
          while run_again:
            while True:
                try:
                    print('<-|',cat_list.head.data,'|->')
                    print("[1] Choose\n[2] Next\n[3] Previous\n[4] Exit")
                    choice=eval(input("Enter your choice: "))
                    break
                except:
                    print("Try again! ")


            if choice==1:
              product = tree.root.left.data[tree.root.left.data['category'] == cat_list.head.data]
              print(product)
              while True:
                  try:
                      id_search = int(input("Order using Product ID : "))
                      cat_product = product[product['Product ID'] == id_search]
                      price = int(cat_product['price'])
                      name = list(cat_product['Name'])
                      nstack.append(name.pop())
                      stack.append(price)
                      print("Product name: ",nstack)
                      print("Product price: ",stack)
                      break
                  except:
                      print("Invalid datatype, Kindly enter a valid datatype ")
              run_again=False
            elif choice==2:
              cat_list.next()
              

            elif choice==3:
              cat_list.prev()
            elif choice==4:
              print("Returned to Main Menu.")
              run_cat=False
              run_again=False
            else:
              print("Invalid choice! ")

      elif user_choice==3:
        run_cat=False
      else:
        print("Wrong choice! ")

cat_list = linkedlist()
cat_list.head = Node('Spicy')
second = Node('Sweet')
third = Node('Sour')
fourth = Node('Karwa')

cat_list.head.next = second
second.next = third
third.next = fourth
fourth.next = cat_list.head

cat_list.head.prev = fourth
second.prev = cat_list.head
third.prev = second
fourth.prev = third

mylist = linkedlist()
mylist.head = Node('Pakistani Cuisine')
second = Node('Italian Cuisine')
third = Node('Chinese Cuisine')
fourth = Node('Greek Cuisine')
fifth = Node('Japanese Cuisine')

mylist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = mylist.head

mylist.head.prev = fifth
second.prev = mylist.head
third.prev = second
fourth.prev = third
fifth.prev = fourth

c_q=[]
nstack=[]
stack=[]
print("\n~ R E S T A U R A N T  O R D E R I N G ~")
print("_______________________________________\n")

run=True
while run:
    while True:
        try:
            print('<-|',mylist.head.data,'|->')
            print("[1] Choose\n[2] Next\n[3] Previous\n[4] Confirm Order\n[5] Exit")
            choice=eval(input("Enter your choice: "))
            break

        except:
            print("Try again! ")
    if choice==1:
      mylist.select()
    elif choice==2:
      mylist.next()
    elif choice==3:
      mylist.prev()
    elif choice==4:
      mylist.confirm()

    elif choice==5:
        print("Exited successfully.")
        run=False
    else:
      print("Invalid choice! ")