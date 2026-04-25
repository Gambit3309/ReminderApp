from datetime import datetime


menu = ["Add Reminder", "View Reminders","Delete Reminder", "Exit"]
reminder_list = []

def view_reminders():
    if not reminder_list:
        print("Reminders List is empty")
    else:
        for index, reminder in enumerate(reminder_list, start=1):
            print(f'{index}. {reminder}')

def add_reminder():
    title = input("Enter Title:")
    desc = input("Description: ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")
    now = datetime.now()
    creation_date = now.strftime("%Y-%m-%d %H:%M")
    user_input = title + ' | ' + desc +'\n' + "Due Date: " + due_date + '\nAdded: ' + creation_date
    reminder_list.append(user_input) 
    print("Reminder Added")

def delete_reminder():
    if not reminder_list:
        print("Reminders List is empty")
    else:
        view_reminders()
        del_reminder = input("Enter reminder number: ")
        removed = reminder_list.pop(int(del_reminder)-1)  
        print(f"'{removed}' has been deleted!")

def main():
    while True:
        print()
        print("My Custom Reminder App")
        for index, item in enumerate(menu, start = 1):
            print(f'{index}. {item}')

        user_choice = input("Enter your choice: ")

        match user_choice:
            case "1":
                add_reminder()
            case "2":
                view_reminders()
            case "3":
                delete_reminder()
            case "4":
                print("Goodbye!")
                break
            case _:
                print("Invalid option, try again.") 


if __name__ == "__main__":
    main()

#lalala adive