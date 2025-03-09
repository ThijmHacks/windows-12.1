import apps.notepad as im_notepad
import apps.matrix as im_matrix

from terminal_os.clear import clear


clear()
while True:
   
    
    terminal_option = input(">>> ")
    
    if terminal_option == "notepad":
        im_notepad.notepad()
    elif terminal_option == "info":
        print("Welcome in the Windows 12 Terminal")
    elif terminal_option == "matrix":
        try:
            im_matrix.main()
        except KeyboardInterrupt:
            print("\nMatrix effect stopped. Goodbye!")  # Graceful exit message
