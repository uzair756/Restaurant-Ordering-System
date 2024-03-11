import PySimpleGUI as sg
from cat_filter import cat_select_front_end
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
# cat_list.category()


def cat_frontend(head):
    main=head
    combo=sg.Combo(values=[cat_list.head.data,cat_list.head.next.data, 
            cat_list.head.next.next.data,cat_list.head.next.next.next.data],
            default_value=cat_list.head.data, key='cuisine')
    layout=[
            [sg.Text("")],
            # [sg.Image(source="#")],
            [sg.Text("")],
            [sg.Text('')],
            [sg.Button("<="),combo,sg.Button("=>")],
            [sg.Text("")],
            [sg.Text(""),sg.Button("Exit"),sg.Button("Confirm")],
            [sg.Text("")]]
    window=sg.Window("Category Selection",layout)
    while True:
                event, values = window.Read()
                if event in (None, 'Exit'):
                        break
                elif event == "Confirm":
                    # print("jn")
                    cat_class = cat_select_front_end(main,cat_list.head)
                elif event == '=>':
                        cat_list.next()
                        combo.update(values=[cat_list.head.prev.data,cat_list.head.data, 
                cat_list.head.next.next.data,cat_list.head.next.next.next.data], value=cat_list.head.data)
                elif event == '<=':
                        cat_list.prev()
                        combo.update(values=[cat_list.head.next.data, 
                cat_list.head.next.next.data,cat_list.head.next.next.next.data, 
                cat_list.head.data,], value=cat_list.head.data)
                
    window.Close()

if __name__=="__main__":
    cat_frontend()
