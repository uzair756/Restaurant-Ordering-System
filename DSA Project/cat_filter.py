import pandas as pd
import PySimpleGUI as sg
from lists import stack
from lists import nstack
pk = pd.read_csv("pak.csv")
jp = pd.read_csv("japan.csv")
italy = pd.read_csv("italy.csv")
grk = pd.read_csv("greek.csv")
china = pd.read_csv("china.csv")
account = pd.read_csv("accounts_info.csv")

# nstack=[]
# stack=[]



class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None


class linkedlist():

  def __init__(self):
    self.head = None
  def next(self):
    self.head = self.head.next
  def prev(self):
    self.head = self.head.prev
  



class T_Node():
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Trees():
    def __init__(self):
        self.root=None




class cat_select_front_end():
    def __init__(self,head,cat_head):
        self.head = head
        self.cat_head=cat_head
        tree=Trees()
        tree.root=T_Node(self.head)
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
        try:
            cat_product = tree.root.left.data[tree.root.left.data['category'] == self.cat_head.data]
            layoutorder=[[sg.Text(""),[sg.Text("______________________________________")],sg.Text(cat_product)],
            [sg.Text("______________________________________")],[sg.Text("Enter the Product ID:")],
            [sg.Text("     "),sg.Input("", size=(25, 3), key='search', justification="center")],
            [sg.Text("           "),sg.Button("Confirm", size=(15, 0))]]
            window = sg.Window('Filtered Category',layoutorder)
            event1, values = window.Read()
            if event1 == "Confirm":
                dict=window.read()[1]
                print(dict["search"])
                product = tree.root.left.data[tree.root.left.data['Product ID'] == int(dict['search'])]
                price = int(product['price'])
                name = list(product['Name'])
                
                nstack.append(name.pop())
                stack.append(price)
                print("Product name: ",nstack)
                print("Product price: ",stack)
                sg.popup("Item added \nCart Updated")
                

        except:
            sg.popup("Product Not Found!")
            
        window.Close()      
                


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
if __name__ == "__main__":
    cat_class=cat_select_front_end()