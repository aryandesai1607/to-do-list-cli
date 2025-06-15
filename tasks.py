def show_menu():
    print("\n1. view tasks")
    print("2. add tasks")
    print("3. remove tasks")
    print("4. exit")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return[]


def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

     
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1: 
            print("\nYour Tasks: ")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == 2:
            task = input("Enter a task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == 3:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            task_no = int(input("Enter the task number you want to remove: ")) - 1
            if 0 <= task_no <= len(tasks):
                tasks.pop(task_no)
                save_tasks(tasks)
        elif choice == 4:
            break
        else:
            print("INVALID CHOICE")





main()