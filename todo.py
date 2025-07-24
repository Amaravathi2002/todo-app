from pymongo import MongoClient

# Replace with your actual MongoDB connection URI
client = MongoClient("mongodb+srv://<Amaravathi_2002>:<Amara_2002>@cluster0.mongodb.net/?retryWrites=true&w=majority")

# Choose database and collection
db = client["todo_database"]
collection = db["todos"]

# Menu
def show_menu():
    print("\n--- ToDo List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

# Add Task
def add_task():
    task = input("Enter task: ")
    collection.insert_one({"task": task})
    print("Task added!")

# View Tasks
def view_tasks():
    tasks = collection.find()
    print("\n--- Your Tasks ---")
    for t in tasks:
        print(f"{t['_id']} - {t['task']}")

# Delete Task
def delete_task():
    view_tasks()
    task_id = input("Enter ID of task to delete: ")
    from bson.objectid import ObjectId
    collection.delete_one({"_id": ObjectId(task_id)})
    print("Task deleted!")

# Main Loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
