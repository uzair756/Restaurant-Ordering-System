import PySimpleGUI as sg
import pandas as pd
from signup_gui import register
account = pd.read_csv("accounts_info.csv")
def login(bill):
    flag=True
    layout = [
            [sg.Text("")],
            [sg.Text("")],
            #[sg.Image(source="logo.png")],
            [sg.Text("")],
            [sg.Text("", key="Notify")],
            [sg.Text("              "),sg.Text("               "), sg.Text('Email')],
            [sg.Input("", key="Email", size=(50, 3), justification='center')],
            [sg.Text("")],
            [sg.Text("             "),sg.Text("             "),sg.Text('Password')],
            [sg.Input("", key="Password", size=(50, 3),
                    justification='center', password_char="*")],
            [sg.Text("")],
            [sg.Text("            "),sg.Button('Login', size=(30, 2))],
            [sg.Text("              "),sg.Text("              "),sg.Button('Return', size=(10, 2))],
        ]

    Window= sg.Window("Login", layout)
    event, values = Window.read()
    if event == "Return":
        Window.Close()
        flag=False
    elif event =="Login":
        x=Window.read()
        a=x[-1]
        Email=a["Email"]
        Password=a["Password"]
        Emailcheck = account[account['Email'] == Email]        #At this time it is randomnly checking the pass and email of random rows
        passcheck = Emailcheck[Emailcheck['Password'] == Password]
        if Emailcheck.empty | passcheck.empty:
            print("Account not found / Incorrect Email OR Password !")
            layout2 = [[sg.Text("Login/ Register for special discount")]
            ,[sg.Button("Login"),sg.Button("Register"),sg.Button("Dont Login")]]
            window=sg.Window('bill',layout2)
            event, values = window.read()
            if event == "Login":
                login()
            elif event == "Register":
                register()
            elif event == "Dont Login":
                Window.Close()
        elif not( passcheck.empty & Emailcheck.empty):
            sg.popup("Logged In!")
            Window.Close()    
            flag=True                    
    while True:
        print(Window.read())
        break
    if flag!=False:
        bill2=bill*0.10
        disbill=bill-bill2
        layout3 = [[sg.Text("The Total amount to be paid is:RS"),sg.Text(disbill)]]
        window=sg.Window("Discount",layout3)
        event, values = window.read()
    else:
        sg.popup(["No discount for you, Pay the actual amount KHALAS!"],["The amount to be paid is: ",bill])

if __name__=="__main__":
    login()

