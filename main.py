from datetime import datetime


menu = ["Add Reminder", "View Reminders","Delete Reminder", "Exit"]
reminder_list = []
id = int(0)

def view_reminders():
    if not reminder_list:
        print("Reminders List is empty")
    else:
        print("%-5s %-20s %-30s %-15s %-20s" % ("ID", "Title", "Description", "Due Date", "Created At"))
        for reminder in reminder_list:
            print("%-5s %-20s %-30s %-15s %-20s" %(reminder.get('ID'),reminder.get('title'),reminder.get('Description'),reminder.get('Due Date'),reminder.get('Created at')))

def update_id(id):
    id = id + 1
    return id

def add_reminder():
    title = input("Enter Title:")
    desc = input("Description: ")
    due_date = input("Enter Due Date (YYYY-MM-DD): ")
    now = datetime.now()
    creation_date = now.strftime("%Y-%m-%d %H:%M")
    #user_input = title + ' | ' + desc +'\n' + "Due Date: " + due_date + '\nAdded: ' + creation_date
    id_temp = update_id(id)
    user_input = {
        'ID' : id_temp,
        "title" : title,
        "Description" : desc,
        "Due Date" : due_date,
        "Created at" : creation_date
    }
    reminder_list.append(user_input) 
    print("Reminder Added")

def delete_reminder():
    if not reminder_list:
        print("Reminders List is empty")
    else:
        view_reminders()
        del_reminder = input("Enter reminder ID: ")
        removed = reminder_list.pop(int(del_reminder))  
        print(f"'{removed}' has been deleted!")

def edit_reminder():
    if not reminder_list:
        print("Reminders List is empty")
    else:
        view_reminders()
        select_reminder = int(input("Enter reminder ID: "))
        keys = list(reminder_list[select_reminder-1].keys())
        for index, key in enumerate(keys, start=1):
            print(f"{index}. {key}")
        user_choice = input("Enter your Field no. to Edit: ")
        x = input("Enter: ")
        print(reminder_list[select_reminder-1][int(user_choice)-1])
        
            


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
            case '5':
                edit_reminder()
            case _:
                print("Invalid option, try again.") 


if __name__ == "__main__":
    main()

#lalala adive