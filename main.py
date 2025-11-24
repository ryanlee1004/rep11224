
# ===== Global Variables =====
current_data = None      # Holds the mark table currently loaded in memory (list of lists)
current_filename = None  # The filename currently being used (string)

# ===== File Utility Functions (implemented in this branch) =====

def save_current_file():
    global current_data, current_filename
    if current_data is None or current_filename is None:
        print("No data or filename to save.")
        return
    with open(current_filename, "w") as f:
        for row in current_data:
            line = ",".join(str(x) for x in row)
            f.write(line + "\n")

def create_new_file():
    global current_data, current_filename

    print("\n=== Create New File ===")

    # 1. get number of students
    while True:
        count = input("Enter number of students (5 to 15): ").strip()
        if count.isdigit():
            count = int(count)
            if 5 <= count <= 15:
                break
        print("Invalid input. Please enter a number between 5 and 15.")

    # 2. get student names
    students = []
    for i in range(count):
        while True:
            name = input(f"Enter name for student {i+1}: ").strip()
            if name != "":
                students.append(name)
                break
            print("Name cannot be empty.")

    # 3. build initial data structure
    current_data = [[""]]  # header row

    for name in students:
        current_data.append([name])

    # 4. get filename
    filename = input("Enter filename to save (without extension): ").strip()
    if not filename.endswith(".csv"):
        filename += ".csv"

    current_filename = filename

    # 5. save file
    save_current_file()
    print(f"File '{current_filename}' created and saved successfully.")

def load_file():
    global current_data, current_filename

    print("\n=== Load File ===")
    filename = input("Enter filename to load (including .csv): ").strip()
    current_filename = filename

    loaded = []

    with open(filename, "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split(",")

        row = []
        for item in parts:
            if item == "A":
                row.append("A")
            elif item.replace(".", "", 1).isdigit():
                if "." in item:
                    row.append(float(item))
                else:
                    row.append(int(item))
            else:
                row.append(item)

        loaded.append(row)

    current_data = loaded
    print(f"File '{current_filename}' loaded successfully.")

# ===== Placeholder Functions for Other Features =====

def enter_weekly_marks():
    print("Enter Weekly Marks: not implemented in this branch yet.")

def view_class_marks():
    print("View Class Marks: not implemented in this branch yet.")

def edit_marks():
    print("Edit Marks: not implemented in this branch yet.")

# ===== Main Menu Loop =====

def main():
    while True:
        print("\n===== Math Tutor Mark Management Program =====")
        print("1. Create New File")
        print("2. Load File")
        print("3. Enter Weekly Marks")
        print("4. View Class Marks")
        print("5. Edit Marks")
        print("6. Exit")

        choice = input("Select a menu option: ").strip()

        if choice == "1":
            create_new_file()
        elif choice == "2":
            load_file()
        elif choice == "3":
            enter_weekly_marks()
        elif choice == "4":
            view_class_marks()
        elif choice == "5":
            edit_marks()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please choose between 1 and 6.")

# Program Start
main()
