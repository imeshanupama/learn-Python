# --------- LOGIN SYSTEM WITH LOOP ---------

def print_line():
    print("=" * 40)

def login():
    users = {
        "imesh": "123456",
        "admin": "admin123"
    }

    while True:
        print_line()
        print("🔐  PYTHON LOGIN SYSTEM")
        print_line()

        username = input("👤 Username: ")
        password = input("🔑 Password: ")

        print_line()

        if username in users and users[username] == password:
            print("✅ Login successful!")
            print(f"🎉 Welcome, {username}!")
            print_line()
            break   # EXIT LOOP when login is correct
        else:
            print("❌ Login failed!")
            print("⚠️  Try again...\n")

# run program
login()