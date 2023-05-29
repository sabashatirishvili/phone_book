import re, os

phone_dir = {}

def is_valid(num):
    """
    ფუნქცია, რომელიც იყენებს რეგულარულ გამოსახულებას იმისათვის, რომ სწორი ტელეფონის ნომერი 
    მიიღოს პროგრამამ.
    """
    regex = r"^(?:\+\d{1,3}\s?)?(?:\d{9,})$"
    return True if re.match(regex, num) else False
    

def add_number(name, num):
    if is_valid(num):
        phone_dir[name] = num
    else:
        return

def remove_number(name):
    if phone_dir and name in phone_dir:
        del phone_dir[name]

def display_numbers():
    if phone_dir:
        for name, number in phone_dir.items():
            print(f"{name}: {number}")
    else:
        print("ნომრების სია ცარიელია.")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    menu = {
        "1": display_numbers,
        "2": add_number,
        "3": remove_number
    }
    while True:
        print("1. არსებული ნომრების დაბეჭვდა")
        print("2. ნომრის ჩამატება")
        print("3. ნომრის ამოშლა")
        print("0. პროგრამიდან გასვლა")
        choice = input("აირჩიეთ მოქმედება")
        if choice == "0":
          break;
        if choice in menu:
            if choice == "2":
                name = input("შეიყვანეთ სახელი:")
                num = input("შეიყვანეთ ნომერი:")
                add_number(name, num)
            elif choice == "3":
                name = input("შეიყვანეთ ამოსაშლელი კონტაქტის სახელი:")
                remove_number(name)
            elif choice == "1":
                display_numbers()
        
        input("ტერმინალის გასანახლებლად დააჭირეთ Enter-ს..")
        clear_terminal()

if __name__ == "__main__":
    main()