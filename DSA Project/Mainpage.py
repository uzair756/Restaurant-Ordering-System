import PySimpleGUI as sg
from Pakistan import Pakistani
from order_confirm_GUI import order_confirmation
sg.theme('BlueMono')
c_q=[]
nstack=[]
stack=[]
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

def front_end():
        combo= sg.Combo(values=[mylist.head.data,mylist.head.next.data, 
                mylist.head.next.next.data,mylist.head.next.next.next.data, 
                mylist.head.next.next.next.next.data], default_value=mylist.head.data,key="cuisine")
        layout=[
                [sg.Text("                         "),sg.Image(source="logo.png")],
                [sg.Text("")],
                [sg.Text("                         "),sg.Button("<=", button_color="green"),combo,sg.Button("=>", button_color="green")],
                [sg.Text("                                                     "),sg.Button("Select", button_color="green")],
                [sg.Text("                                     "),sg.Button("Confirm", button_color="green"),sg.Button("Exit", button_color="green")],
                [sg.Text("")],
                [sg.Text("")]]
        window=sg.Window("Cusine Selection",layout,size=(500,500))
        while True:
                event, values = window.Read()
                if event in (None, 'Exit'):
                        sg.popup("       Exited\nHave a nice day")
                        break
                elif event == "Select":
                        llist=Pakistani(mylist.head.data)
                elif event == "Confirm":
                        order_confirmation()
                elif event == '=>':
                        mylist.next()
                        combo.update(values=[mylist.head.prev.data,mylist.head.data, 
                mylist.head.next.next.data,mylist.head.next.next.next.data, 
                mylist.head.next.next.next.next.data], value=mylist.head.data)
                elif event == '<=':
                        mylist.prev()
                        combo.update(values=[mylist.head.next.data, 
                mylist.head.next.next.data,mylist.head.next.next.next.data, 
                mylist.head.next.next.next.next.data,mylist.head.data,], value=mylist.head.data)
        window.Close()

front_end()