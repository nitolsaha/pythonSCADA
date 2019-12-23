from employee_management import *
from menu import *
from order_process import *
from tkinter import *

global Elabel1
global Elabel2
global main_admin


if __name__ == '__main__':
    employee_management = Employee_Management()
    menu=Menu_Management()
    bill_count= Bill_Process()




root= Tk()


main_admin_pass= employee_management.all_emp_admin_pass()
print(main_admin_pass)

main_emp= employee_management.all_emp_emp_list()
print(main_emp)

main_emp_pass= employee_management.all_emp_emp_pass()
print(main_emp_pass)

main_admin= employee_management.all_emp_admin_list()
print(main_admin)



root.title("Resturant Management System")
root.geometry('400x300')

Label1= Label(root, text= "User Name")
Label2= Label(root, text= "Password")

Elabel1= Entry(root)
Elabel2= Entry(root, show= '*')



def check_login():
    print("check login started")
    if Elabel1 in main_admin:
        index_admin= main_admin.index(Elabel1)
        if main_admin_pass[index_admin]==Elabel2:
            print("Choose the any option (select 1 or 2) :\n")
            '''
            admin_option=int(input("1. Add Employee\n2. Update Menu\n3. Show Menu\n4.Order Process\nChoose your option :"))
            if admin_option==1:
                employee_management.add_employee()
            elif admin_option==2:
                menu.add_menu()
            elif admin_option==3:
                menu.all_menu()
            elif admin_option==4:
                menu.all_menu()
                bill_count.order()
                v=input("Do you want to process another order? : y/n\nChoose your option :")
            '''





Button1= Button(root,text='Login', command= check_login)

Label1.grid(row=1, sticky= E)
Label2.grid(row=2, sticky= E)
Elabel1.grid(row=1, column=1)
Elabel2.grid(row=2, column=1)
Button1.grid(row=3)
root.mainloop()




