try:
    with open("data.txt", "r") as file:
        content = file.read()
        file.close() #closing the file
except FileNotFoundError:
    print("Error: File not found.")
else:
    print("File content:\n", content)