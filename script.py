# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is the first line of my file.\n")
        file.write("This is the second line of my file.\n")
        file.write("This is the third line of my file.\n")
    print("New file 'my_file.txt' created successfully.")
except FileNotFoundError:
    print("File 'my_file.txt' could not be created.")
except PermissionError:
    print("You do not have permission to create the file 'my_file.txt'.")
except Exception as e:
    print("An unexpected error occurred while creating the file 'my_file.txt'.", e)
finally:
    print("File creation process completed.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of 'my_file.txt':")
        print(contents)
except FileNotFoundError:
    print("File 'my_file.txt' could not be found.")
except PermissionError:
    print("You do not have permission to read the file 'my_file.txt'.")
except Exception as e:
    print("An unexpected error occurred while reading the file 'my_file.txt'.", e)
finally:
    print("File reading process completed.")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is the fourth line of my file.\n")
        file.write("This is the fifth line of my file.\n")
        file.write("This is the sixth line of my file.\n")
    print("Three lines appended to 'my_file.txt' successfully.")
except FileNotFoundError:
    print("File 'my_file.txt' could not be found.")
except PermissionError:
    print("You do not have permission to append to the file 'my_file.txt'.")
except Exception as e:
    print("An unexpected error occurred while appending to the file 'my_file.txt'.", e)
finally:
    print("File appending process completed.")