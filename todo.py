def main():      #Defines the main function where the core logic of the to-do list resides
    tasks = []    #Initializes an empty list called tasks to store task dictionaries. Each dictionary will represent a task with its name and completion status.

    while True:      #Starts an infinite loop to continuously show the menu until the user chooses to exit.
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
#Displays a menu with four options for the user.
        choice = input("Enter your choice: ")
#Asks the user to input their choice (1 to 4).
        if choice == '1':
            print()
            n_tasks = int(input("How may task you want to add: "))
#Prompts the user for the number of tasks to add and converts it to an integer.
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")
#Loops n_tasks times to take input for each task.
#Each task is stored as a dictionary with keys:
#"task": the task description
#"done": a boolean initially set to False
#Adds each task to the tasks list and confirms it was added.
        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")
#Lists all tasks in the tasks list.
#Uses enumerate() to get each task's index and details.
#Displays task number, name, and whether it's done or not.
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
#Asks the user for the task number to mark as done.
#Subtracts 1 because list indices start from 0, but the user sees tasks numbered from 1.
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            # Checks if the entered index is valid.
            # If valid, sets the "done" key of the task to True.
            else:
                print("Invalid task number.")
        # Displays an error message if the task number is out of range.
        elif choice == '4':
            print("Exiting the To-Do List.")
            break
#Breaks out of the while loop and ends the program.

        else:
            print("Invalid choice. Please try again.")
#Displays a message for invalid input and re-displays the menu.

if __name__ == "__main__":
    main()

"""
🔹 What is __name__ in Python?
Every Python file (module) has a special built-in variable called __name__.

When a Python file is:

run directly, Python sets __name__ to "__main__".

imported into another file, __name__ is set to the module's name (i.e., the file name without .py).

Example:
Suppose you have a file named todo.py:

Case 1: Run directly

bash
Copy
Edit
$ python todo.py
Then inside todo.py, __name__ == "__main__" will be True.

Case 2: Imported in another file

python
Copy
Edit
import todo
Then inside todo.py, __name__ == "todo" (i.e., the module name), not "__main__".

🔹 Why do we use if __name__ == "__main__":?
We use it to ensure that certain code runs only when the file is executed directly, not when it is imported as a module.

So:

python
Copy
Edit
if __name__ == "__main__":
    main()
This line checks: "Is this script being run directly?"

If yes, it calls the main() function to start the program.

If the script is imported in another file, the main() function won't run automatically.

🔹 Why is this useful?
It lets you write reusable code. Example:

python
Copy
Edit
# todo.py
def main():
    print("This is the main To-Do List app")

def helper():
    print("This is a helper function")
Now if you run todo.py directly, you want main() to execute.
But if someone imports todo.py to reuse helper(), you don’t want the whole app to run automatically.

By using:

python
Copy
Edit
if __name__ == "__main__":
    main()
You avoid that problem.

✅ Summary
Part	Meaning
__name__	A special variable that holds the name of the current module.
"__main__"	The value of __name__ when the script is run directly.
if __name__ == "__main__":	Ensures the code block runs only if the file is executed directly, not when imported.

Would you like a visual diagram or code example with two files to show this in action?
"""