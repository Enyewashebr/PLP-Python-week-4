def read_and_write_file():
    try:
        # Ask user for filename
        filename = input("Enter the filename to read from: ")
        
        # Open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        
        output_filename = "output.txt"
        with open(output_filename, "w") as output_file:
            output_file.write(modified_content)

        print(f"Modified content has been saved to {output_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_write_file()
