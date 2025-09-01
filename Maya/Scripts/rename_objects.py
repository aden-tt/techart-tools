# Bulk Naming Script
# This script allows users to select multiple objects and rename them with a prefix and a specified number of digits (e.g., object_0001)

import maya.cmds as cmds

# popup window
def create_ui():
    window = cmds.window(title="Bulk Naming Tool", width=260)
    main_layout = cmds.columnLayout(adj=True, cw=200, cat=["both", 10], rs=3, p=window)

    cmds.text(label='Prefix', p=main_layout)
    cmds.textField("prefixField", p=main_layout)
    cmds.text(label='# of Digits', p=main_layout)
    cmds.intField("digitsField", value=4, p=main_layout)
    cmds.button(label='Rename Objects', command=renameObjects, p=main_layout)
    
    cmds.showWindow(window)

# renames each selected object with prefix and number
def renameObjects(*args):
    # Query the UI fields each time the button is pressed
    prefix = cmds.textField("prefixField", query=True, text=True)
    digits = cmds.intField("digitsField", query=True, value=True)
    
    # Store currently selected objects
    unnamed = cmds.ls(selection=True)    
    counter = 1 

    # Iterate over each object and rename using prefix and counter
    for u in unnamed:
        newName = prefix + "_" + str(counter).zfill(digits)
        counter = counter + 1
        cmds.rename(u, newName) 
        
        
create_ui() # display ui 