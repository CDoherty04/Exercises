import PySimpleGUI as SimpGUI

label1 = SimpGUI.Text("Enter Feet: ")
input1 = SimpGUI.Input()

label2 = SimpGUI.Text("Enter Inches: ")
input2 = SimpGUI.Input()

convert_button = SimpGUI.Button("Convert")

window = SimpGUI.Window("Convertor",
                        layout=[[label1, input1],
                                [label2, input2],
                                [convert_button]])

window.read()
window.close()
