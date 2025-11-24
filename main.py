
# ===== Global Variables =====
current_data = None      # Holds the mark table currently loaded in memory (list of lists)
current_filename = None  # The filename currently being used (string)

# ===== Utility Functions =====

def save_current_file():
    global current_data, current_filename
    if current_data is None or current_filename is None:
        print("No data or filename to save.")
        return
    with open(current_filename, "w") as f:
        for row in current_data:
            line = ",".join(str(x) for x in row)
            f.write(line + "\n")

# ===== Helper Functions for Statistics =====

def extract_numeric(values):
    nums = []
    for v in values:
        if v != "A":
            nums.append(v)
    return nums

def mean(values):
    if len(values) == 0:
        return "N/A"
    return sum(values) / len(values)

def median(values):
    if len(values) == 0:
        return "N/A"
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n % 2 == 1:
        return sorted_vals[n // 2]
    else:
        return (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2

def stdev(values):
    if len(values) == 0:
        return "N/A"
    m = mean(values)
    var_sum = 0
    for v in values:
        var_sum += (v - m) ** 2
    variance = var_sum / len(values)
    return variance ** 0.5

def rank_students(data):
    # data[1:] = students
    means = []
    for row in data[1:]:
        numeric = extract_numeric(row[1:])
        m = mean(numeric)
        means.append(m)

    # sort unique means descending
    unique_means = sorted(list(set(means)), reverse=True)

    # assign rank based on mean
    ranks = []
    for m in means:
        rank = unique_means.index(m) + 1
        ranks.append(rank)

    return ranks

# ===== File and Mark Functions (placeholders for other branches) =====

def create_new_file():
    print("Create New File: not implemented in this branch yet.")

def load_file():
    print("Load File: not implemented in this branch yet.")

def enter_weekly_marks():
    print("Enter Weekly Marks: not implemented in this branch yet.")

def edit_marks():
    print("Edit Marks: not implemented in this branch yet.")

# ===== View Class Marks (implemented in this branch) =====

def view_class_marks():
    global current_data

    if current_data is None:
        print("No file loaded.")
        return

    print("\n=== Class Marks ===")

    header = current_data[0]
    student_rows = current_data[1:]

    # ----- Student Statistics -----
    print("\n--- Student Statistics ---")

    ranks = rank_students(current_data)

    for i, row in enumerate(student_rows):
        name = row[0]
        scores = row[1:]

        nums = extract_numeric(scores)
        m = mean(nums)
        med = median(nums)
        sd = stdev(nums)

        print(f"\n{name}:")
        print(f"  Scores: {scores}")
        print(f"  Mean: {m}")
        print(f"  Median: {med}")
        print(f"  Std Dev: {sd}")
        print(f"  Rank: {ranks[i]}")

    # ----- Test Statistics -----
    print("\n--- Test Statistics ---")

    num_tests = len(header) - 1

    for t in range(num_tests):
        test_name = header[t + 1]

        col_values = []
        for row in student_rows:
            v = row[t + 1]
            if v != "A":
                col_values.append(v)

        m = mean(col_values)
        med = median(col_values)
        sd = stdev(col_values)

        print(f"\n{test_name}:")
        print(f"  Mean: {m}")
        print(f"  Median: {med}")
        print(f"  Std Dev: {sd}")

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
