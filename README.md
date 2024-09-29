<!DOCTYPE html>
<html>
<head>

</head>
<body>

<h1>To-Do List Chat Bot with Dynamic Categorization and Timestamps</h1>

<p>Welcome to the <strong>To-Do List Chat Bot with Dynamic Categorization and Timestamps</strong>! This application is an interactive command-line chat bot that helps you manage your tasks efficiently by automatically categorizing them and tracking when they are added, completed, and removed.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a>
        <ul>
            <li><a href="#adding-tasks">Adding Tasks</a></li>
            <li><a href="#viewing-tasks">Viewing Tasks</a></li>
            <li><a href="#completing-tasks">Completing Tasks</a></li>
            <li><a href="#removing-tasks">Removing Tasks</a></li>
            <li><a href="#help">Help</a></li>
            <li><a href="#exiting">Exiting</a></li>
        </ul>
    </li>
    <li><a href="#example-interaction">Example Interaction</a></li>
    <li><a href="#code-explanation">Code Explanation</a>
        <ul>
            <li><a href="#imports-and-setup">Imports and Setup</a></li>
            <li><a href="#data-structures">Data Structures</a></li>
            <li><a href="#core-functions">Core Functions</a>
                <ul>
                    <li><a href="#get_categoryword">get_category(word)</a></li>
                    <li><a href="#add_taskdescription">add_task(description)</a></li>
                    <li><a href="#remove_tasktask_identifier">remove_task(task_identifier)</a></li>
                    <li><a href="#view_tasks">view_tasks()</a></li>
                    <li><a href="#mark_task_completetask_identifier">mark_task_complete(task_identifier)</a></li>
                    <li><a href="#parse_commandcommand">parse_command(command)</a></li>
                    <li><a href="#print_help">print_help()</a></li>
                </ul>
            </li>
            <li><a href="#main-loop">Main Loop</a></li>
        </ul>
    </li>
    <li><a href="#dependencies">Dependencies</a></li>
    <li><a href="#license">License</a></li>
</ul>

<hr>

<h2 id="features">Features</h2>

<ul>
    <li><strong>Interactive Chat Bot Interface</strong>: Engage with the bot using natural language commands.</li>
    <li><strong>Dynamic Task Categorization</strong>: Automatically categorizes tasks using the WordNet lexical database.</li>
    <li><strong>Timestamps</strong>: Records and displays when tasks are added, completed, and removed.</li>
    <li><strong>Add Multiple Tasks</strong>: Add single or multiple tasks in one command.</li>
    <li><strong>Remove Tasks</strong>: Remove tasks by their name or index within their category.</li>
    <li><strong>Complete Tasks</strong>: Mark tasks as complete by name or index.</li>
    <li><strong>View Tasks</strong>: Display all tasks grouped by their categories, showing completion status and timestamps.</li>
    <li><strong>Help Command</strong>: Provides a list of available commands and usage instructions.</li>
    <li><strong>Persistent Categories</strong>: Categories are created dynamically and maintained as tasks are added or removed.</li>
</ul>

<hr>

<h2 id="installation">Installation</h2>

<ol>
    <li><strong>Clone the Repository</strong>:
        <pre><code>git clone https://github.com/yourusername/yourrepository.git</code></pre>
    </li>
    <li><strong>Navigate to the Project Directory</strong>:
        <pre><code>cd yourrepository</code></pre>
    </li>
    <li><strong>Install Dependencies</strong>:
        <p>Ensure you have <strong>Python 3</strong> installed. Install the required Python packages using pip:</p>
        <pre><code>pip install nltk</code></pre>
    </li>
    <li><strong>Download NLTK Data</strong>:
        <p>The script will attempt to download necessary NLTK data files (<code>wordnet</code> and <code>omw-1.4</code>) automatically. If you encounter issues, you can download them manually:</p>
        <pre><code>import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')</code></pre>
    </li>
</ol>

<hr>

<h2 id="usage">Usage</h2>

<p>Run the script using the following command:</p>

<pre><code>python todo_chatbot.py</code></pre>

<h3 id="adding-tasks">Adding Tasks</h3>

<ul>
    <li><strong>Add a Single Task</strong>:
        <pre><code>Add buy groceries</code></pre>
    </li>
    <li><strong>Add Multiple Tasks</strong>:
        <pre><code>Add apple, banana, and orange</code></pre>
        <p>The bot will automatically categorize each task and record the timestamp when each task is added.</p>
    </li>
</ul>

<h3 id="viewing-tasks">Viewing Tasks</h3>

<ul>
    <li>Display all tasks grouped by their categories, along with their addition and completion timestamps:
        <pre><code>View tasks</code></pre>
    </li>
    <li>or
        <pre><code>Show my tasks</code></pre>
    </li>
</ul>

<h3 id="completing-tasks">Completing Tasks</h3>

<ul>
    <li><strong>Complete a Single Task by Name</strong>:
        <pre><code>Complete buy groceries</code></pre>
    </li>
    <li><strong>Complete Multiple Tasks</strong>:
        <pre><code>Complete apple, banana</code></pre>
    </li>
    <li><strong>Complete a Task by Index</strong> (index refers to the position within its category):
        <pre><code>Complete 0</code></pre>
    </li>
</ul>

<h3 id="removing-tasks">Removing Tasks</h3>

<ul>
    <li><strong>Remove a Single Task by Name</strong>:
        <pre><code>Remove buy groceries</code></pre>
    </li>
    <li><strong>Remove Multiple Tasks</strong>:
        <pre><code>Remove apple, banana</code></pre>
    </li>
    <li><strong>Remove a Task by Index</strong>:
        <pre><code>Remove 0</code></pre>
    </li>
</ul>

<h3 id="help">Help</h3>

<ul>
    <li>Display the help message with all available commands:
        <pre><code>Help</code></pre>
    </li>
</ul>

<h3 id="exiting">Exiting</h3>

<ul>
    <li>Exit the chat bot:
        <pre><code>Exit</code></pre>
    </li>
    <li>or
        <pre><code>Quit</code></pre>
    </li>
</ul>

<hr>

<h2 id="example-interaction">Example Interaction</h2>

<pre><code>Hello! I'm your To-Do List Assistant with dynamic categorization and timestamps. How can I help you today?
Type 'help' to see what I can do.

You: Add apple, banana, and cow
Task added under 'Edible_fruit': apple (Added on 2023-10-01 12:00:00)
Task added under 'Edible_fruit': banana (Added on 2023-10-01 12:00:00)
Task added under 'Bovine': cow (Added on 2023-10-01 12:00:00)

You: View tasks
Here are your tasks:

Category: Edible_fruit
  0. [❌] apple
     Added on: 2023-10-01 12:00:00
  1. [❌] banana
     Added on: 2023-10-01 12:00:00

Category: Bovine
  0. [❌] cow
     Added on: 2023-10-01 12:00:00

You: Complete banana
Great job! You've completed: banana in 'Edible_fruit'
Completed on: 2023-10-01 12:05:00

You: View tasks
Here are your tasks:

Category: Edible_fruit
  0. [❌] apple
     Added on: 2023-10-01 12:00:00
  1. [✔️] banana
     Added on: 2023-10-01 12:00:00
     Completed on: 2023-10-01 12:05:00

Category: Bovine
  0. [❌] cow
     Added on: 2023-10-01 12:00:00

You: Remove cow
Task removed from 'Bovine': cow
Added on: 2023-10-01 12:00:00
Removed on: 2023-10-01 12:10:00

You: Bye
Goodbye! Have a productive day!
</code></pre>

<hr>

<h2 id="code-explanation">Code Explanation</h2>

<h3 id="imports-and-setup">Imports and Setup</h3>

<pre><code>import re
from datetime import datetime
from nltk.corpus import wordnet as wn
import nltk

# Ensure the necessary NLTK data files are downloaded
try:
    wn.synsets('test')
except LookupError:
    nltk.download('wordnet')
    nltk.download('omw-1.4')
</code></pre>

<ul>
    <li><strong>re</strong>: For regular expression operations used in command parsing.</li>
    <li><strong>datetime</strong>: To handle date and time operations.</li>
    <li><strong>nltk.corpus.wordnet</strong>: Used for natural language processing and categorization.</li>
    <li><strong>nltk</strong>: Provides functionalities for downloading necessary datasets.</li>
</ul>

<p>The script checks if the required NLTK data is available; if not, it downloads it.</p>

<h3 id="data-structures">Data Structures</h3>

<pre><code># Dictionary to store tasks categorized
categories = {}
</code></pre>

<ul>
    <li><strong>categories</strong>: A dictionary where each key is a category name, and the value is a list of tasks under that category.</li>
    <li>Each task is a dictionary with the following keys:
        <ul>
            <li><code>'description'</code></li>
            <li><code>'completed'</code></li>
            <li><code>'date_added'</code></li>
            <li><code>'date_completed'</code> (added when the task is completed)</li>
            <li><code>'date_removed'</code> (added when the task is removed)</li>
        </ul>
    </li>
</ul>

<h3 id="core-functions">Core Functions</h3>

<h4 id="get_categoryword"><code>get_category(word)</code></h4>

<p>Determines the category of a word using WordNet hypernyms.</p>

<pre><code>def get_category(word):
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
</code></pre>

<ul>
    <li>Fetches the first synset (meaning) of the word.</li>
    <li>Obtains hypernyms (broader categories).</li>
    <li>Returns the first hypernym as the category, capitalized.</li>
    <li>Returns <code>'Uncategorized'</code> if no synsets or hypernyms are found.</li>
</ul>

<h4 id="add_taskdescription"><code>add_task(description)</code></h4>

<p>Adds new tasks to the to-do list, categorizing them dynamically and recording the addition timestamp.</p>

<pre><code>def add_task(description):
    task_list = [task.strip() for task in description.split(',') if task.strip()]
    for task_name in task_list:
        category = get_category(task_name.lower())
        task = {
            'description': task_name,
            'completed': False,
            'date_added': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'date_removed': None
        }
        categories.setdefault(category, []).append(task)
        print(f"Task added under '{category}': {task_name} (Added on {task['date_added']})")
</code></pre>

<ul>
    <li>Splits the input description into individual tasks.</li>
    <li>For each task:
        <ul>
            <li>Determines its category.</li>
            <li>Creates a task dictionary with the description, completion status, and addition timestamp.</li>
            <li>Adds the task to the appropriate category in the <code>categories</code> dictionary.</li>
        </ul>
    </li>
    <li>Prints a confirmation message with the category and timestamp.</li>
</ul>

<h4 id="remove_tasktask_identifier"><code>remove_task(task_identifier)</code></h4>

<p>Removes tasks from the to-do list by their number or description, records the removal timestamp, and displays the addition and removal times.</p>

<pre><code>def remove_task(task_identifier):
    found = False
    for category, tasks in categories.items():
        # Try to interpret task_identifier as an index
        try:
            task_number = int(task_identifier)
            if 0 <= task_number < len(tasks):
                tasks[task_number]['date_removed'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                removed_task = tasks.pop(task_number)
                print(f"Task removed from '{category}': {removed_task['description']}")
                print(f"Added on: {removed_task['date_added']}")
                print(f"Removed on: {removed_task['date_removed']}")
                found = True
                break
        except ValueError:
            # Treat task_identifier as a description
            for i, task in enumerate(tasks):
                if task['description'].lower() == task_identifier.lower():
                    task['date_removed'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    removed_task = tasks.pop(i)
                    print(f"Task removed from '{category}': {removed_task['description']}")
                    print(f"Added on: {removed_task['date_added']}")
                    print(f"Removed on: {removed_task['date_removed']}")
                    found = True
                    break
        if found:
            # Clean up category if empty
            if not tasks:
                del categories[category]
            break
    if not found:
        print(f"No task found with description or number: {task_identifier}")
</code></pre>

<ul>
    <li>Iterates over categories and tasks.</li>
    <li>Attempts to match the task identifier as an index or description.</li>
    <li>Records the current date and time as the removal timestamp.</li>
    <li>Removes the task if found and updates the categories.</li>
    <li>Prints the task description along with addition and removal timestamps.</li>
    <li>Notifies the user if the task is not found.</li>
</ul>

<h4 id="view_tasks"><code>view_tasks()</code></h4>

<p>Displays all tasks grouped by their categories, including their addition and completion timestamps.</p>

<pre><code>def view_tasks():
    if not categories:
        print("You have no tasks at the moment.")
    else:
        print("Here are your tasks:")
        for category, tasks in categories.items():
            print(f"\nCategory: {category}")
            for idx, task in enumerate(tasks):
                status = '✔️' if task['completed'] else '❌'
                print(f"  {idx}. [{status}] {task['description']}")
                print(f"     Added on: {task['date_added']}")
                if task['completed']:
                    print(f"     Completed on: {task['date_completed']}")
</code></pre>

<ul>
    <li>Checks if there are tasks to display.</li>
    <li>Iterates over each category and its tasks.</li>
    <li>Prints out the category name and tasks with their completion status and timestamps.</li>
</ul>

<h4 id="mark_task_completetask_identifier"><code>mark_task_complete(task_identifier)</code></h4>

<p>Marks specific tasks as completed and records the completion timestamp.</p>

<pre><code>def mark_task_complete(task_identifier):
    found = False
    for category, tasks in categories.items():
        # Try to interpret task_identifier as an index
        try:
            task_number = int(task_identifier)
            if 0 <= task_number < len(tasks):
                tasks[task_number]['completed'] = True
                tasks[task_number]['date_completed'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"Great job! You've completed: {tasks[task_number]['description']} in '{category}'")
                print(f"Completed on: {tasks[task_number]['date_completed']}")
                found = True
                break
        except ValueError:
            # Treat task_identifier as a description
            for task in tasks:
                if task['description'].lower() == task_identifier.lower():
                    task['completed'] = True
                    task['date_completed'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    print(f"Great job! You've completed: {task['description']} in '{category}'")
                    print(f"Completed on: {task['date_completed']}")
                    found = True
                    break
        if found:
            break
    if not found:
        print(f"No task found with description or number: {task_identifier}")
</code></pre>

<ul>
    <li>Similar logic to <code>remove_task</code>.</li>
    <li>Marks the task's <code>'completed'</code> status as <code>True</code> and records the completion timestamp.</li>
    <li>Prints a confirmation message with the completion timestamp.</li>
    <li>Notifies the user if the task is not found.</li>
</ul>

<h4 id="parse_commandcommand"><code>parse_command(command)</code></h4>

<p>Parses the user's command and calls the appropriate function.</p>

<pre><code>def parse_command(command):
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
</code></pre>

<ul>
    <li>Strips and processes the command.</li>
    <li>Uses regular expressions to match command patterns.</li>
    <li>Calls the corresponding function based on the command.</li>
    <li>Supports adding, removing, viewing, completing tasks, and showing help.</li>
    <li>Processes multiple tasks in add, remove, and complete commands.</li>
</ul>

<h4 id="print_help">print_help()</h4>

<p>Prints the list of available commands.</p>

<pre><code>def print_help():
    print("""
I can help you manage your to-do list with dynamic categorization and timestamps. Here are some things you can say:

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
</code></pre>

<ul>
    <li>Provides usage instructions and examples.</li>
</ul>

<h3 id="main-loop">Main Loop</h3>

<pre><code>if __name__ == "__main__":
    print("Hello! I'm your To-Do List Assistant with dynamic categorization and timestamps. How can I help you today?")
    print("Type 'help' to see what I can do.\n")
    while True:
        command = input("You: ")
        if command.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye! Have a productive day!")
            break
        parse_command(command)
</code></pre>

<ul>
    <li>Starts the chat bot.</li>
    <li>Continuously prompts the user for input.</li>
    <li>Exits when the user types an exit command.</li>
    <li>Calls <code>parse_command</code> to handle user input.</li>
</ul>

<hr>

<h2 id="dependencies">Dependencies</h2>

<ul>
    <li><strong>Python 3</strong>: Ensure you have Python version 3.x installed.</li>
    <li><strong>NLTK (Natural Language Toolkit)</strong>: Used for natural language processing and categorization.
        <pre><code>pip install nltk</code></pre>
    </li>
    <li><strong>NLTK Data</strong>: The script will attempt to download necessary NLTK data files (<code>wordnet</code> and <code>omw-1.4</code>) automatically. If you encounter issues, download them manually:
        <pre><code>import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')</code></pre>
    </li>
</ul>

<hr>

<h2 id="license">License</h2>

<p>This project is open-source and available under the <a href="LICENSE">MIT License</a>.</p>

<hr>

<p><strong>Enjoy managing your tasks with the To-Do List Chat Bot with Dynamic Categorization and Timestamps!</strong></p>

<p>If you have any questions or suggestions, feel free to contribute or open an issue on GitHub.</p>

</body>
</html>
