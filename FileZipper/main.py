import PySimpleGUI as SimpGUI


c_label = SimpGUI.Text("Select files to compress: ")
c_input = SimpGUI.Input()
c_button = SimpGUI.FilesBrowse("Choose")

d_label = SimpGUI.Text("Select destination folder: ")
d_input = SimpGUI.Input()
d_button = SimpGUI.FolderBrowse("Choose")

run_button = SimpGUI.Button("Compress")


window = SimpGUI.Window("File Zipper", layout=[[c_label, c_input, c_button], [d_label, d_input, d_button], [run_button]])
window.read()
window.close()
