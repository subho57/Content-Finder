import os
print("##############################################")
print("#\t\tContent Finder\t\t     #")
print("#\t\t  v0.1-alpha\t\t     #")
print("##############################################")
direc=os.listdir()
key=input("Enter the keyword you want to search for: ")
ext=input("Enter the file extenion you want to search in: ")
for file in direc:
    if file.endswith(ext):
        print(f"\nSearching in {file}...")
        with open(file, "r") as f:
            fileContent=f.read()
        if key.lower() in fileContent.lower():
            ch=input(f"\nSearch keyword found in {file} !!\nDo you want to open it (Y/n)? ")
            if ch.lower() == 'y':
                print(f"Opening {file}...\n")
                print(fileContent)
            ch=input("\nDo you want to continue (Y/n)? ")
            if ch.lower() == 'n':
                print("Exiting Program...")
                exit(0)
        else:
            print(f"Search keyword NOT found in {file}!!")