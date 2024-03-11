import PySimpleGUI as sg
layout=[#[sg.Image(source="logo.png")],
        [sg.Text("                     "),sg.Text("Account")],
        [sg.Button("Login"),sg.Button("Register"),sg.Button("Dont Login")]


]
Window=sg.Window("User Selection",layout)
Window.read()