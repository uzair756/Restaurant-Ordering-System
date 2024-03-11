import pandas as pd
import PySimpleGUI as sg
from categories import cat_frontend
from lists import stack
from lists import nstack
pk = pd.read_csv("pak.csv")
jp = pd.read_csv("japan.csv")
italy = pd.read_csv("italy.csv")
grk = pd.read_csv("greek.csv")
china = pd.read_csv("china.csv")
account = pd.read_csv("accounts_info.csv")

# sg.theme('DarkAmber')
# nstack=[]
# stack=[]


class T_Node():
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Trees():
    def __init__(self):
        self.root=None
class Pakistani():

  def __init__(self,head):
    self.head = head
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
    flag=True
    while flag:
        layout =  [
                  [sg.Text("______________________________________")],
                  [sg.Text("                "),sg.Text(tree.root.left.data[['Name','price']])],
                  [sg.Text("______________________________________")],[sg.Text('Please select an option:')],
                  [sg.Button('Order'), sg.Button('Filter by Category'), sg.Button('Return')],
                  [sg.Text('', key='output')]]
                  
        window = sg.Window('Front-end').Layout(layout)
        event, values = window.Read()
        window.Close()
        if event in (None, 'Return'):
            flag=False
        elif event == 'Order':
            try:
                layoutorder=[[sg.Text(""),[sg.Text("______________________________________")],sg.Text(tree.root.left.data)],
                [sg.Text("______________________________________")],[sg.Text("Enter the Product ID:")],
                [sg.Text("     "),sg.Input("", size=(25, 3), key='search', justification="center")],
                [sg.Text("           "),sg.Button("Confirm", size=(15, 0))]]
                window = sg.Window('Menu').Layout(layoutorder)
                event1, values = window.Read()
                if event1 == "Confirm":
                    dict=window.read()[1]
                    print(dict["search"])
                    product = tree.root.left.data[tree.root.left.data['Product ID'] == int(dict['search'])]
                    print(product)
                    price = int(product['price'])
                    name = list(product['Name'])
                    nstack.append(name.pop())
                    stack.append(price)
                    print("Product name: ",nstack)
                    print("Product price: ",stack)
                    sg.popup("Item added \nCart Updated")

            except:
                sg.popup("Product Not Found!")         
            
        elif event == 'Filter by Category':
            cat_frontend(self.head)
                    
        window.Close()
if __name__=="__main__":
    llist=Pakistani()
