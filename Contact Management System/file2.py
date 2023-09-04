contacts = dict()
def search_contact():
    name = input("Enter name to search:")
    if name in contacts:
        details = contacts[name]
        print(f"Name:{name}")
    else:
        print("Contact not found")


def delete_contact():
    name = input("Enter name to delete:")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found")