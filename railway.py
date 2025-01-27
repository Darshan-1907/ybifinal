import pandas as pd
import os

# File paths for storing data
USER_FILE = "users.csv"
TRAIN_FILE = "trains.csv"
BOOKING_FILE = "bookings.csv"

# Initialize files if they don't exist
def initialize_files():
    if not os.path.exists(USER_FILE):
        pd.DataFrame(columns=["Username", "Password"]).to_csv(USER_FILE, index=False)
    if not os.path.exists(TRAIN_FILE):
        pd.DataFrame(columns=["TrainNo", "Name", "Source", "Destination", "Time"]).to_csv(TRAIN_FILE, index=False)
    if not os.path.exists(BOOKING_FILE):
        pd.DataFrame(columns=["Username", "TrainNo", "SeatNo"]).to_csv(BOOKING_FILE, index=False)

# User registration
def register():
    users = pd.read_csv(USER_FILE)
    username = input("Enter username: ")
    if username in users["Username"].values:
        print("Username already exists!")
        return
    password = input("Enter password: ")
    new_user = pd.DataFrame({"Username": [username], "Password": [password]})
    new_user.to_csv(USER_FILE, mode='a', header=False, index=False)
    print("Registration successful!")

# User login
def login():
    users = pd.read_csv(USER_FILE)
    username = input("Enter username: ")
    password = input("Enter password: ")
    if ((users["Username"] == username) & (users["Password"] == password)).any():
        print("Login successful!")
        return username
    else:
        print("Invalid credentials!")
        return None

# Add train (Admin function)
def add_train():
    trains = pd.read_csv(TRAIN_FILE)
    train_no = input("Enter train number: ")
    if train_no in trains["TrainNo"].values:
        print("Train already exists!")
        return
    name = input("Enter train name: ")
    source = input("Enter source station: ")
    destination = input("Enter destination station: ")
    time = input("Enter departure time: ")
    new_train = pd.DataFrame({"TrainNo": [train_no], "Name": [name], "Source": [source], "Destination": [destination], "Time": [time]})
    new_train.to_csv(TRAIN_FILE, mode='a', header=False, index=False)
    print("Train added successfully!")

# View train schedules
def view_trains():
    trains = pd.read_csv(TRAIN_FILE)
    if trains.empty:
        print("No trains available.")
    else:
        print("\nTrain Schedules:")
        print(trains.to_string(index=False))

# Book a ticket
def book_ticket(username):
    view_trains()
    train_no = input("Enter train number to book: ")
    seat_no = input("Enter seat number: ")
    new_booking = pd.DataFrame({"Username": [username], "TrainNo": [train_no], "SeatNo": [seat_no]})
    new_booking.to_csv(BOOKING_FILE, mode='a', header=False, index=False)
    print("Ticket booked successfully!")

# View bookings
def view_bookings(username):
    bookings = pd.read_csv(BOOKING_FILE)
    user_bookings = bookings[bookings["Username"] == username]
    if user_bookings.empty:
        print("No bookings found.")
    else:
        print("\nYour Bookings:")
        print(user_bookings.to_string(index=False))

# Main menu
def main():
    initialize_files()
    user = None
    while True:
        print("\nRailway Management System")
        print("1. Register")
        print("2. Login")
        print("3. Admin - Add Train")
        print("4. View Train Schedules")
        print("5. Book Ticket")
        print("6. View Bookings")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
        elif choice == "3":
            add_train()
        elif choice == "4":
            view_trains()
        elif choice == "5":
            if user:
                book_ticket(user)
            else:
                print("Please login first.")
        elif choice == "6":
            if user:
                view_bookings(user)
            else:
                print("Please login first.")
        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
