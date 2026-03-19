import os

DEFAULT_CONTACTS_FILE = "contacts.txt"


def load_contacts(file_path=DEFAULT_CONTACTS_FILE):
    """Load contacts from a file into a dictionary.

    The contact file format is one contact per line:
        name:phone
    """

    contacts = {}
    if not os.path.exists(file_path):
        return contacts

    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if not line or ":" not in line:
                    continue
                name, phone = line.split(":", 1)
                contacts[name.strip()] = phone.strip()
    except Exception as e:
        print(f"Failed to load contacts from '{file_path}': {e}")

    return contacts


def save_contacts(contacts, file_path=DEFAULT_CONTACTS_FILE):
    """Save contacts to a file, overwriting any existing content."""

    try:
        with open(file_path, "w") as file:
            for name, phone in contacts.items():
                file.write(f"{name}:{phone}\n")
        print(f"Contacts saved to '{file_path}'.")
    except Exception as e:
        print(f"Failed to save contacts to '{file_path}': {e}")


def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")


def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")


def main():
    contacts = load_contacts()

    print("Welcome to Contact Book!")
    if contacts:
        print(f"Loaded {len(contacts)} contact(s) from '{DEFAULT_CONTACTS_FILE}'.")

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Save Contacts")
        print("5. Load Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            name = input("Enter contact name: ").strip()
            phone = input("Enter contact phone number: ").strip()
            add_contact(contacts, name, phone)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            name = input("Enter contact name to delete: ").strip()
            delete_contact(contacts, name)
        elif choice == "4":
            save_contacts(contacts)
        elif choice == "5":
            confirm = input("This will replace current in-memory contacts. Continue? (y/N): ").strip().lower()
            if confirm == "y":
                contacts = load_contacts()
                print(f"Loaded {len(contacts)} contact(s) from '{DEFAULT_CONTACTS_FILE}'.")
            else:
                print("Load canceled.")
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
