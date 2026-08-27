# A student needs to manage a list of assignments. Write a Python script that:
# Creates a list of assignments,
# Adds a new assignment to the list, 
# Removes an assignment that is completed,
# Prints the updated list of assignments 

def main():
    # 1. Create a list of initial assignments
    assignments = ["Math Homework", "History Essay", "Physics Lab Report"]
    print(f"Initial assignments: {assignments}")

    # 2. Add a new assignment to the list
    new_assignment = "Computer Science Project"
    assignments.append(new_assignment)
    print(f"\nAdded: '{new_assignment}'")

    # 3. Remove a completed assignment
    completed_assignment = "History Essay"
    if completed_assignment in assignments:
        assignments.remove(completed_assignment)
        print(f"Removed completed task: '{completed_assignment}'")

    # 4. Print the updated list of assignments
    print("\n--- Updated Assignment List ---")
    for index, task in enumerate(assignments, 1):
        print(f"{index}. {task}")


if __name__ == "__main__":
    main()
