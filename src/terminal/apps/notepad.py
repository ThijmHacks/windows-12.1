def notepad():
    while True:
        # Ask user for a command
        user_input = input("Type 'write' to add text or 'read [filename]' to read the file: ")
        
        # Check if user wants to add text to a file
        if user_input.lower() == "write":
            filename = input("Enter the filename (with .txt extension): ")
            print(f"Now writing to {filename}. Type 'exit' to stop.")
            with open(filename, 'a') as file:
                while True:
                    line = input(">>>  ")
                    if line.lower() == 'exit':
                        break
                    file.write(line + '\n')
            
        # Check if user wants to read a file
        elif user_input.lower().startswith("read"):
            parts = user_input.split()
            if len(parts) == 2:
                filename = parts[1]
                try:
                    with open(filename, 'r') as file:
                        print(f"Contents of {filename}:")
                        print(file.read())
                except FileNotFoundError:
                    print(f"Error: The file {filename} does not exist.")
            else:
                print("Please specify a valid filename to read.")
        
        # Exit the loop if user types 'exit'
        elif user_input.lower() == "exit":
            print("Exiting notepad.")
            break
        else:
            print("Invalid command. Try again.")
