"""import json
import os
import streamlit as st

DATA_FILE = "bank_data.json"

# ---------- Save data to JSON ----------
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\nData saved to {DATA_FILE} successfully!")


# ---------- Load existing data (if available) ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Warning: JSON file was empty or corrupted. Starting fresh.")
                return {}
    else:
        return {}


# ---------- Create account ----------
def create_account(data):
    name = input("Enter account holder name: ").strip()
    if name in data:
        print(f"Account for '{name}' already exists!")
        return data

    pin = input("Enter 4-digit PIN: ").strip()
    balance = float(input("Enter initial balance: "))

    data[name] = {
        "account_holder": name,
        "pin": pin,
        "balance": balance
    }

    print(f"\nAccount for {name} added successfully!")
    return data


# ---------- Read / Display accounts ----------
def display_accounts(data):
    if not data:
        print("\nNo accounts found.")
        return

    print("\n--- All Bank Accounts ---")
    for account in data.values():
        print(f"Name: {account['account_holder']}, PIN: {account['pin']}, Balance: {account['balance']}")


# ---------- Update account ----------
def update_account(data):
    name = input("Enter the account holder name to update: ").strip()
    if name not in data:
        print(f"Account for '{name}' does not exist!")
        return data

    print("\nWhat would you like to update?")
    print("1. PIN")
    print("2. Balance")

    choice = input("Enter your choice (1/2): ").strip()

    if choice == '1':
        new_pin = input("Enter new 4-digit PIN: ").strip()
        data[name]['pin'] = new_pin
        print(f"\nPIN updated for {name}")

    elif choice == '2':
        new_balance = float(input("Enter new balance: "))
        data[name]['balance'] = new_balance
        print(f"\nBalance updated for {name}")

    else:
        print("Invalid choice.")

    return data


# ---------- Delete account ----------
def delete_account(data):
    name = input("Enter the account holder name to delete: ").strip()
    if name in data:
        confirm = input(f"Are you sure you want to delete account '{name}'? (y/n): ").lower()
        if confirm == 'y':
            del data[name]
            print(f"\nAccount '{name}' deleted successfully!")
        else:
            print("Delete cancelled.")
    else:
        print(f"Account for '{name}' does not exist!")

    return data


# ---------- Main program ----------
def main():
    print("Welcome to the Bank Account Manager")
    data = load_data()

    while True:
        print("\n--- Menu ---")
        print("1. Create Account")
        print("2. Display All Accounts")
        print("3. Update Account")
        print("4. Delete Account")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            data = create_account(data)
        elif choice == '2':
            display_accounts(data)
        elif choice == '3':
            data = update_account(data)
        elif choice == '4':
            data = delete_account(data)
        elif choice == '5':
            save_data(data)
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")


if __name__ == "__main__":
    main()


#streamlit UI

st.title("Bank Account Manager")
st.write("Manage bank accounts with Create, Read, Update, and Delete operations.")
if st.button("Run Bank Account Manager"):
    main()
    st.success("Bank Account Manager operations completed. Check console for details.")
    choice=st.selectbox("Choose an operation",["Create Account","Display All Accounts","Update Account","Delete Account"])
    if choice=="Create Account":
        name=st.text_input("Enter account holder name")
        pin=st.text_input("Enter 4-digit PIN")
        balance=st.number_input("Enter initial balance",min_value=0.0)
    elif choice=="Display All Accounts":
        display_accounts(load_data())
    elif choice=="Update Account":
        name=st.text_input("Enter the account holder name to update")
        update_choice=st.selectbox("What would you like to update?",["PIN","Balance"])
        if update_choice=="PIN":
            new_pin=st.text_input("Enter new 4-digit PIN")
        elif update_choice=="Balance":
            new_balance=st.number_input("Enter new balance",min_value=0.0)
    elif choice=="Delete Account":
        name=st.text_input("Enter the account holder name to delete")
        if st.button("Delete Account"):
            data=load_data()
            if name in data:
                confirm=st.radio(f"Are you sure you want to delete account '{name}'?",["No","Yes"])
                if confirm=="Yes":
                    del data[name]
                    save_data(data)
                    st.success(f"Account '{name}' deleted successfully!")
                else:
                    st.info("Delete cancelled.")
            else:
                st.error(f"Account for '{name}' does not exist!")
    save_data(load_data())"""

import json
import os
import streamlit as st

DATA_FILE = "bank_data.json"

# ---------- Save data to JSON ----------
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- Load existing data (if available) ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                st.warning("Warning: JSON file was empty or corrupted. Starting fresh.")
                return {}
    else:
        return {}

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Bank Account Manager", page_icon="🏦")
st.title("🏦 Bank Account Manager")
st.write("Easily **Create**, **View**, **Update**, and **Delete** bank accounts using this simple CRUD app.")

# Load existing data
data = load_data()

# ---------- Menu ----------
menu = st.sidebar.radio("Select an Operation", ["Create Account", "Display All Accounts", "Update Account", "Delete Account"])

# ---------- CREATE ----------
if menu == "Create Account":
    st.subheader("➕ Create a New Account")
    name = st.text_input("Enter account holder name")
    pin = st.text_input("Enter 4-digit PIN", type="password", max_chars=4)
    balance = st.number_input("Enter initial balance", min_value=0.0)

    if st.button("Create Account"):
        if not name or not pin:
            st.error("Please fill all fields!")
        elif name in data:
            st.warning(f"Account for '{name}' already exists!")
        else:
            data[name] = {
                "account_holder": name,
                "pin": pin,
                "balance": balance
            }
            save_data(data)
            st.success(f"Account for '{name}' created successfully!")

# ---------- DISPLAY ----------
elif menu == "Display All Accounts":
    st.subheader("📋 All Bank Accounts")

    if not data:
        st.info("No accounts found.")
    else:
        for account in data.values():
            with st.expander(f"Account: {account['account_holder']}"):
                st.write(f"**PIN:** {account['pin']}")
                st.write(f"**Balance:** ₹{account['balance']}")

# ---------- UPDATE ----------
elif menu == "Update Account":
    st.subheader("✏️ Update Account Details")

    if not data:
        st.info("No accounts available to update.")
    else:
        selected_name = st.selectbox("Select account to update", list(data.keys()))
        update_choice = st.radio("What would you like to update?", ["PIN", "Balance"])

        if update_choice == "PIN":
            new_pin = st.text_input("Enter new 4-digit PIN", type="password", max_chars=4)
            if st.button("Update PIN"):
                if new_pin:
                    data[selected_name]['pin'] = new_pin
                    save_data(data)
                    st.success(f"PIN updated for '{selected_name}' successfully!")
                else:
                    st.error("Please enter a valid PIN.")
        else:
            new_balance = st.number_input("Enter new balance", min_value=0.0)
            if st.button("Update Balance"):
                data[selected_name]['balance'] = new_balance
                save_data(data)
                st.success(f"Balance updated for '{selected_name}' successfully!")

# ---------- DELETE ----------
elif menu == "Delete Account":
    st.subheader("🗑️ Delete Account")

    if not data:
        st.info("No accounts available to delete.")
    else:
        selected_name = st.selectbox("Select account to delete", list(data.keys()))
        confirm = st.checkbox(f"Yes, delete account '{selected_name}'")

        if st.button("Delete Account"):
            if confirm:
                del data[selected_name]
                save_data(data)
                st.success(f"Account '{selected_name}' deleted successfully!")
            else:
                st.warning("Please confirm deletion before proceeding.")

    