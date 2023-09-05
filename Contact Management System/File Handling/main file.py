import file1
import file2
 
contacts = dict()


while True:
    file1.show_menu()
    choice = input("Enter your choice:")
    if choice == '1':
        file1.add_contact()
    elif choice == '2':
        file1.view_contact()
    elif choice == '3':
        file1.search_contact()
    elif choice == '4':
        file2.edit_contact()  
    elif choice == '5':
        file2.delete_contact()
    elif choice == '6':
        print("Exiting Contact")
        break
    else:
        print("invalid contact.please select a valid option")
        
    