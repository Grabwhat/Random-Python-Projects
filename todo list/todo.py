def showtask(todos):
    if not todos:
        print("You have nothing to do.\n")
    else:
        print("Your Todo List:\n")
        for i, todo in enumerate(todos):
            print(f"{i + 1}. {todo}")

def addtask(thelist, task):
    thelist.append(task)
    print("Task Added\n")

def deletetask(thelist, task):
    thelist.pop(thelist.index(task))
    print("Task Deleted")

def main():
    todo = []
    while True:
        print("\nWelcome to Your Todo List!\n" \
        "1. Your List\n" \
        "2. Add a task\n" \
        "3. Delete task")

        what = input("\nWhat do you want to do? ")

        if what == "1":
            showtask(todo)
        elif what == "2":
            task = input("What is your task? ")
            addtask(todo, task)
        elif what == "3":
            showtask(todo)
            deltask = input("Which task do you want to delete? ")
            if deltask in todo:
                deletetask(todo, deltask)
            else:
                print("Error: Task does not exist")

main()