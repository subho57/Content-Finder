#   Copyright @subho57
#   GitHub  :   https://github.com/subho57
#   LinkedIn:   https://www.linkedin.com/in/subho57/
import os

# function to render pdf files
def search_in_pdf(file,key):
    import PyPDF2
    pdfReader = PyPDF2.PdfFileReader(open(file, 'rb'))
    for i in range(pdfReader.numPages):
        if key in str((pdfReader.getPage(i)).extractText()).lower():
            ch=input(f"\nSearch keyword FOUND in {file} !!\nDo you want to open it (Y/n)? ")
            if ch.lower() == 'y':
                print(f"Opening {file}...\n")
                print(os.system(f'"{file}"'))
            return True
    print(f"Search keyword NOT FOUND in {file}!!")
    return False

# function to render other plain text format files
def search_in_other(file,key):
    with open(file, "r") as fp:
        fileContent=fp.read()
    if key in fileContent.lower():
        ch=input(f"\nSearch keyword FOUND in {file} !!\nDo you want to open it (Y/n)? ")
        if ch.lower() == 'y':
            print(f"Opening {file}...\n")
            print(os.system(f'"{file}"'))
        return True
    else:
        print(f"Search keyword NOT FOUND in {file}!!")
        return False

# driver program
print("##############################################")
print("#                                            #")
print("#\t\tContent Finder\t\t     #")
print("#\t\t v1.0.2-beta \t\t     #")
print("#\t      brought to you by\t\t     #")
print("#\t\t  @subho57\t\t     #")
print("#                                            #")
print("##############################################\n")
print("************Supported File Types**************\n")
print("PDF, TXT, HTML, CSS, JAVASCRIPT, JSON, XML, PY")
print("\tC, CPP, JAVA, H, HAS, PYPY")
print("______________________________________________\n")
direc=os.listdir()
key=input("Enter the keyword you want to search for: ")
ext=input("Enter the file extenion you want to search in: ")
for file in direc:
    if file.endswith(ext):
        print(f"\nSearching in {file}...")
        flag=False
        if ext=='pdf':
            flag=search_in_pdf(file,key.lower())
        elif ext=='txt' or ext=='html' or ext=='c' or ext=='py' or ext=='java' or ext=='json' or ext=='cpp':
            flag=search_in_other(file,key.lower())
        if flag:
            ch=input("\nDo you want to continue (Y/n)? ")
            if ch.lower() == 'n':
                print("Exiting Program...")
                exit(0)
