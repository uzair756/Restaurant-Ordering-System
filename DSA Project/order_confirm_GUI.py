import PySimpleGUI as sg
from signup_gui import register
from login_GUI import login
from lists import stack
from lists import nstack
dict={}



sg.theme('DarkAmber')
font_big = ("Arial", 15)
font_small = ("Arial", 12)
def order_confirmation():
    deq=[]
    bill=0
    for i in range(len(stack)):
        dict={}

        dict[nstack.pop()] = stack.pop()
        deq.append(dict)
    print(deq)
    dupdeq=deq.copy()


    for i in range(len(dupdeq)):
        d=dupdeq.pop()
        layout = [[sg.Text("Name"),sg.Text("Price")]
            
        ]
        layout.append([sg.Text(list(d.keys()).pop()),sg.Text(list(d.values()).pop())])
        layout.append([sg.Text("Do you want to confirm this item:")])
        layout.append([sg.Radio('Confirm',1, key='Confirm')])
        layout.append([sg.Radio('Discard',1, key='Discard')])
        layout.append([sg.Button('Done')])
        window = sg.Window('Checkbox Example', layout)
        event, values = window.read()
        if event == 'Done':
            x=window.read()
            print(x)
            a=x[-1]
            if a['Confirm']==True:
                b=deq.pop(i-1)
                deq.insert(0,b)
                amount=list(b.values()).pop()
                print(amount)
                bill=bill+amount
            elif a['Confirm']==False:
                deq.pop(i-1)
        window.Close()
    layout2 = [[sg.Text("The Total amount to be paid is:RS"),sg.Text(bill)],[sg.Text("Login/ Register for special discount")]
    ,[sg.Button("Login"),sg.Button("Register"),sg.Button("Dont Login")]]
    window=sg.Window('bill',layout2)
    event, values = window.read()
    if event == "Login":
        login(bill)
        
    elif event == "Register":
        register(bill)
    elif event == "Dont Login":
        sg.popup(["No discount for you, Pay the actual amount KHALAS!"],["The amount to be paid is: ",bill])
    window.Close()
    print(deq)

    print(deq)
    print(bill)
    while True:
        window.read()
        break




