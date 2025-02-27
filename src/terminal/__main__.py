import apps.notepad
from terminal_os.clear import clear


clear()
while True:
   
    
    terminal_option = input(">>> ")
    
    if terminal_option == "notepad":
        apps.notepad.notepad()
    elif terminal_option == "info":
        print("Welcome in the Windows 12 Terminal")