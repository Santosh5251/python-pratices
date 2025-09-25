import os

FILENAME = "contacts.txt"

def create_contact(name, phone):
    with open(FILENAME, "a") as f:
        f.write(f"{name},{phone}\n")
    print("Contact created.")

def read_contacts():
    if not os.path.exists(FILENAME):
        print("No contacts found.")
        return
    with open(FILENAME, "r") as f:
        for line in f:
            name, phone = line.strip().split(",")
            print(f"Name: {name}, Phone: {phone}")

def update_contact(old_name, new_name, new_phone):
    if not os.path.exists(FILENAME):
        print("No contacts to update.")
        return
    lines = []
    with open(FILENAME, "r") as f:
        lines = f.readlines()
    with open(FILENAME, "w") as f:
        found = False
        for line in lines:
            name, phone = line.strip().split(",")
            if name == old_name:
                f.write(f"{new_name},{new_phone}\n")
                found = True
            else:
                f.write(line)
        if found:
            print("Contact updated.")
        else:
            print("Contact not found.")

def delete_contact(name):
    if not os.path.exists(FILENAME):
        print("No contacts to delete.")
        return
    lines = []
    with open(FILENAME, "r") as f:
        lines = f.readlines()
    with open(FILENAME, "w") as f:
        found = False
        for line in lines:
            contact_name, phone = line.strip().split(",")
            if contact_name != name:
                f.write(line)
            else:
                found = True
        if found:
            print("Contact deleted.")
        else:
            print("Contact not found.")

# Example usage
create_contact("santosh", "12345")
create_contact("Bob", "67890")
read_contacts()
update_contact("Madhav", "Amit", "54321")
delete_contact("Bob")
read_contacts()
