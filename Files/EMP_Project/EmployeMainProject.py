from EmployeMenu import menu
from EmployeeAdd import addemployee
from EmployeDelete import deleteemploye
from EmployeSearch import searchemploye
from EmployeUpdate import updateemploye
from EmployeView import viewemploye,viewallemployes

while(True):
    try:
        menu()
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                addemployee()
            case 2:
                deleteemploye()
            case 3:
                updateemploye()
            case 4:
                viewemploye()
            case 5:
                viewallemployes()
            case 6:
                searchemploye()
            case 7:
                print("Thxx for using this project")
                break
            case _:
                print("\tUr Selection of operation is wrong -- try again")
    except ValueError:
        print("\tDont Enter Alnums, Strs, and Symbols for ur choice - try again.")