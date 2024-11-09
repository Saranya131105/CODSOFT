contacts = {}
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!\n")
def view_contacts():
    if contacts:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No contacts found.\n")
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() == name.lower() or search_term == details["phone"]:
            print(f"\nContact found:\nName: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Updating contact details:")
        contacts[name]["phone"] = input("Enter new phone number: ")
        contacts[name]["email"] = input("Enter new email: ")
        contacts[name]["address"] = input("Enter new address: ")
        print("Contact updated successfully!\n")
    else:
        print("Contact not found.\n")
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")
def main():
    print("Welcome to the Contact Book!")
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()