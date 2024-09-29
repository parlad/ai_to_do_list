# To-Do List Chat Bot with Dynamic Categorization

import re
from nltk.corpus import wordnet as wn
import nltk

# Ensure the necessary NLTK data files are downloaded
try:
    wn.synsets('test')
except LookupError:
    nltk.download('wordnet')
    nltk.download('omw-1.4')

# Dictionary to store tasks categorized
categories = {}

def get_category(word):
    """
    Determines the category of a word using WordNet hypernyms.
    """
    synsets = wn.synsets(word)
    if not synsets:
        return 'Uncategorized'
    # Get the first synset
    synset = synsets[0]
    # Get hypernyms (broader categories)
    hypernyms = synset.hypernyms()
    if hypernyms:
        # Return the first hypernym's lemma name as category
        category = hypernyms[0].lemma_names()[0]
        return category.capitalize()
    else:
        return 'Uncategorized'

def add_task(description):
    """
    Adds new tasks to the to-do list, categorizing them dynamically.
    """
    task_list = [task.strip() for task in description.split(',') if task.strip()]
    for task_name in task_list:
        category = get_category(task_name.lower())
        task = {'description': task_name, 'completed': False}
        categories.setdefault(category, []).append(task)
        print(f"Task added under '{category}': {task_name}")

def remove_task(task_identifier):
    """
    Removes tasks from the to-do list by their number or description.
    """
    found = False
    for category, tasks in categories.items():
        # Try to interpret task_identifier as an index
        try:
            task_number = int(task_identifier)
            if 0 <= task_number < len(tasks):
                removed_task = tasks.pop(task_number)
                print(f"Task removed from '{category}': {removed_task['description']}")
                found = True
                break
        except ValueError:
            # Treat task_identifier as a description
            for i, task in enumerate(tasks):
                if task['description'].lower() == task_identifier.lower():
                    removed_task = tasks.pop(i)
                    print(f"Task removed from '{category}': {removed_task['description']}")
                    found = True
                    break
        if found:
            # Clean up category if empty
            if not tasks:
                del categories[category]
            break
    if not found:
        print(f"No task found with description or number: {task_identifier}")

def view_tasks():
    """
    Displays all tasks in the to-do list with their categories and status.
    """
    if not categories:
        print("You have no tasks at the moment.")
    else:
        print("Here are your tasks:")
        for category, tasks in categories.items():
            print(f"\nCategory: {category}")
            for idx, task in enumerate(tasks):
                status = '✔️' if task['completed'] else '❌'
                print(f"  {idx}. [{status}] {task['description']}")

def mark_task_complete(task_identifier):
    """
    Marks specific tasks as completed.
    """
    found = False
    for category, tasks in categories.items():
        # Try to interpret task_identifier as an index
        try:
            task_number = int(task_identifier)
            if 0 <= task_number < len(tasks):
                tasks[task_number]['completed'] = True
                print(f"Great job! You've completed: {tasks[task_number]['description']} in '{category}'")
                found = True
                break
        except ValueError:
            # Treat task_identifier as a description
            for task in tasks:
                if task['description'].lower() == task_identifier.lower():
                    task['completed'] = True
                    print(f"Great job! You've completed: {task['description']} in '{category}'")
                    found = True
                    break
        if found:
            break
    if not found:
        print(f"No task found with description or number: {task_identifier}")

def parse_command(command):
    """
    Parses the user's command and calls the appropriate function.
    """
    command = command.strip()

    # Add task(s)
    add_match = re.match(r'add (.+)', command, re.IGNORECASE)
    if add_match:
        tasks_string = add_match.group(1)
        # Replace ' and ' with ','
        tasks_string = tasks_string.replace(' and ', ',')
        add_task(tasks_string)
        return

    # Remove task(s)
    remove_match = re.match(r'remove (.+)', command, re.IGNORECASE)
    if remove_match:
        tasks_string = remove_match.group(1)
        # Replace ' and ' with ','
        tasks_string = tasks_string.replace(' and ', ',')
        task_list = [task.strip() for task in tasks_string.split(',')]
        for task_identifier in task_list:
            if task_identifier:
                remove_task(task_identifier)
        return

    # View tasks
    if re.search(r'\b(view|show|list)\b', command, re.IGNORECASE):
        view_tasks()
        return

    # Mark task(s) as complete
    complete_match = re.match(r'(complete|done|finish) (.+)', command, re.IGNORECASE)
    if complete_match:
        tasks_string = complete_match.group(2)
        # Replace ' and ' with ','
        tasks_string = tasks_string.replace(' and ', ',')
        task_list = [task.strip() for task in tasks_string.split(',')]
        for task_identifier in task_list:
            if task_identifier:
                mark_task_complete(task_identifier)
        return

    # Help command
    if re.match(r'help', command, re.IGNORECASE):
        print_help()
        return

    print("Sorry, I didn't understand that command. Type 'help' to see what I can do.")

def print_help():
    """
    Prints the list of available commands.
    """
    print("""
I can help you manage your to-do list with dynamic categorization. Here are some things you can say:

- Add a task: "Add buy groceries"
- Add multiple tasks: "Add apples, bananas, and oranges"
- Remove a task: "Remove buy groceries" or "Remove 0"
- Remove multiple tasks: "Remove apples, bananas, and oranges"
- View tasks: "View tasks", "Show my tasks", "List"
- Mark task as complete: "Complete buy groceries" or "Complete 0"
- Mark multiple tasks as complete: "Complete apples, bananas"
- Help: "Help", "What can you do?"
- Exit: "Exit", "Quit", "Bye"
""")

# Chat bot loop
if __name__ == "__main__":
    print("Hello! I'm your To-Do List Assistant with dynamic categorization. How can I help you today?")
    print("Type 'help' to see what I can do.\n")
    while True:
        command = input("You: ")
        if command.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye! Have a productive day!")
            break
        parse_command(command)
