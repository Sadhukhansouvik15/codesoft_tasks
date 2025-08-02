def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    if not name:
        print("Name is required to add a contact.")
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contacts(contacts):
    query = input("Enter name or phone number to search: ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if results:
        print("\nSearch Results:")
        for i, c in enumerate(results, start=1):
            display_contact_details(i, c)
    else:
        print("No contacts matched your search.")

def display_contact_details(index, contact):
    print(f"{index}. Name: {contact['name']}")
    print(f"   Phone: {contact['phone']}")
    print(f"   Email: {contact['email']}")
    print(f"   Address: {contact['address']}")

def update_contact(contacts):
    if not contacts:
        print("No contacts available to update.")
        return
    view_contacts(contacts)
    try:
        choice = int(input("Enter the number of the contact to update: "))
        if 1 <= choice <= len(contacts):
            contact = contacts[choice - 1]
            print("Leave field empty to keep current value.")
            new_name = input(f"Name [{contact['name']}]: ").strip()
            new_phone = input(f"Phone [{contact['phone']}]: ").strip()
            new_email = input(f"Email [{contact['email']}]: ").strip()
            new_address = input(f"Address [{contact['address']}]: ").strip()

            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address

            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact(contacts):
    if not contacts:
        print("No contacts available to delete.")
        return
    view_contacts(contacts)
    try:
        choice = int(input("Enter the number of the contact to delete: "))
        if 1 <= choice <= len(contacts):
            removed = contacts.pop(choice - 1)
            print(f"Contact '{removed['name']}' deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    contacts = []
    print("Welcome to the Contact Book!")

    while True:
        display_menu()
        option = input("Select an option (1-6): ").strip()

        if option == '1':
            add_contact(contacts)
        elif option == '2':
            view_contacts(contacts)
        elif option == '3':
            search_contacts(contacts)
        elif option == '4':
            update_contact(contacts)
        elif option == '5':
            delete_contact(contacts)
        elif option == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
