# Project 1: To-Do List - DecodeLabs
# By: Yasra Shabir

my_tasks = []

def add_task(task):
    my_tasks.append(task)
    print(f"✅ Task added: '{task}'")

def view_tasks():
    if len(my_tasks) == 0:
        print("📋 No tasks yet!")
    else:
        print("\n📋 Your To-Do List:")
        for index, task in enumerate(my_tasks, start=1):
            print(f"  {index}. {task}")
        print()

def main():
    print("🚀 Welcome to DecodeLabs To-Do List!\n")
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("\nEnter choice (1/2/3): ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()