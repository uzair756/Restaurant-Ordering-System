import PySimpleGUI as sg
import pandas as pd
account = pd.read_csv("accounts_info.csv")

def register(bill):
    flag=True
    layout = [

                [sg.Text("")],
            #[sg.Image(source='logo.png')],
            [sg.Text("")],
            [sg.Text("", key="Notify")],
            [sg.Text("            "), sg.Text("Name"), sg.Text("               "), sg.Text("               "), sg.Text("Age")],
            [sg.Input("", size=(25, 3), justification='centre', key="name"), sg.Input("", size=(25, 3), key="age", justification='centre')],
            [sg.Text("            "), sg.Text("Phone"), sg.Text("          "), sg.Text("          "),
            sg.Text("      "), sg.Text("City")],
            [sg.Input("", size=(25, 3), justification='centre', key="phon"),
            sg.Input("", size=(25, 3), justification='centre', key="city")],
            [sg.Text("                                       "), sg.Text("Email")],
            [sg.Input("", size=(52, 3), key="Email", justification="center")],

            [sg.Text("                                     "), sg.Text("Password")],
            [sg.Input("", size=(52, 3), key="Password", justification="center", password_char="*")],
            [sg.Text("")],
            [sg.Text("         "),sg.Button('Sign Up', size=(30, 2))],
            [sg.Text("                              "),sg.Button('Return', size=(10, 2))],

        ]
    Window= sg.Window("Sign up", layout)
    event, values = Window.read()
    if event == "Sign Up":
        x=Window.read()
        a=x[-1]
        Name=a["name"]
        Age=a["age"]
        Email=a['Email']
        Phone_no=a['phon']
        City=a['city']
        Password=a['Password']
        account_dict = {'Name': Name , 'Age': Age , 'Email': Email,
        "Phone number": Phone_no, "City": City , 'Password' : Password} 
        account.loc[len(account)] = account_dict
        account.to_csv("accounts_info.csv", index=False)
        sg.popup("Account Created!")
        Window.Close()
        flag=True
    elif event == "Return":
        flag=False
        Window.Close()

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
if __name__ == "__main__":
    register()