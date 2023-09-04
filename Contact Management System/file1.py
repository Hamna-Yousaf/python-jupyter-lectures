
contacts = dict()
def show_menu():
    print("Contact Management System")
    print("1.Add Contact")
    print("2.View Contact")
    print("3.Search Contact")
    print("4.Edit Contact")
    print("5.Delete Contact")
    print("6.Exit")


def add_contact():
    name = input("Enter name:")
    Phone = input("Enter phone:")
    contacts[name] = Phone
    print("Contacts added successfully!")



def view_contact():
    if contacts:
      print("Contacts:")
      for name in contacts.items():
          print(f"Name:{name}")
    else:
        print("No contacts found")

def search_contact():
    name = input("Enter name to search:")
    if name in contacts:
        details = contacts[name]
        print(f"Name:{name}")
    else:
        print("Contact not found")