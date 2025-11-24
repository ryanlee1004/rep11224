# ===== Global Variables =====
current_data = None      # Holds the mark table currently loaded in memory (list of lists)
current_filename = None  # The filename currently being used (string)

# ===== File Save Utility (used by this branch) =====

def save_current_file():
    global current_data, current_filename
    if current_data is None or current_filename is None:
        print("No data or filename to save.")
        return
    with open(current_filename, "w") as f:
        for row in current_data:
            line = ",".join(str(x) for x in row)
            f.write(line + "\n")

# ===== Placeholder Functions for File Creation/Loading/Viewing =====

def create_new_file():
    print("Create New File: not implemented in this branch yet.")

def load_file():
    print("Load File: not implemented in this branch yet.")

def view_class_marks():
    print("View Class Marks: not implemented in this branch yet.")

# ===== Enter and Edit Marks (implemented in this branch) =====

def enter_weekly_marks():
    global current_data, current_filename

    if current_data is None or current_filename is None:
        print("No file loaded. Please create or load a file first.")
        return

    print("\n=== Enter Weekly Marks ===")

    header = current_data[0]
    current_tests = len(header) - 1
    new_test_number = current_tests + 1
    test_name = "Test" + str(new_test_number)

    header.append(test_name)

    for i in range(1, len(current_data)):
        name = current_data[i][0]
        while True:
            entry = input(
                f"Enter mark for {name} in {test_name} "
                "(0-10 in steps of 0.5, 'A' for approved absence, or 0 for unapproved absence): "
            ).strip().upper()

            if entry == "A":
                current_data[i].append("A")
                break

            try:
                value = float(entry)
            except ValueError:
                print("Invalid input. Please enter a number or 'A'.")
                continue

            if not (0 <= value <= 10):
                print("Mark must be between 0 and 10.")
                continue

            if value * 2 != int(value * 2):
                print("Mark must be in steps of 0.5 (e.g. 7, 7.5).")
                continue

            if value == int(value):
                value = int(value)

            current_data[i].append(value)
            break

    save_current_file()
    print(f"Marks for {test_name} added and file saved as '{current_filename}'.")

def edit_marks():
    global current_data, current_filename

    if current_data is None:
        print("No file loaded.")
        return

    print("\n=== Edit Marks ===")

    header = current_data[0]
    student_rows = current_data[1:]

    print("\nSelect a student to edit:")
    for i, row in enumerate(student_rows):
        print(f"{i+1}. {row[0]}")

    while True:
        choice = input("Enter student number: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(student_rows):
                break
        print("Invalid choice.")

    student_index = choice
    student_name = student_rows[student_index - 1][0]

    num_tests = len(header) - 1

    if num_tests == 0:
        print("No tests available to edit.")
        return

    print("\nSelect test to edit:")
    for i in range(1, len(header)):
        print(f"{i}. {header[i]}")

    while True:
        t_choice = input("Enter test number: ").strip()
        if t_choice.isdigit():
            t_choice = int(t_choice)
            if 1 <= t_choice <= num_tests:
                break
        print("Invalid choice.")

    test_index = t_choice
    test_name = header[test_index]

    while True:
        entry = input(
            f"Enter new mark for {student_name} in {test_name} "
            "(0-10 in steps of 0.5, 'A', or 0): "
        ).strip().upper()

        if entry == "A":
            new_value = "A"
            break

        try:
            value = float(entry)
        except ValueError:
            print("Invalid input.")
            continue

        if not (0 <= value <= 10):
            print("Mark must be between 0 and 10.")
            continue

        if value * 2 != int(value * 2):
            print("Mark must be in 0.5 steps.")
            continue

        if value == int(value):
            value = int(value)

        new_value = value
        break

    current_data[student_index][test_index] = new_value

    save_current_file()

    print(f"Updated {student_name}'s mark for {test_name} to {new_value}.")

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
