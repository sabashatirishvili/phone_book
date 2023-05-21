def addNumber(num, name, dict):
    dict[num] = name

def deleteNumber(number, dict):
    dict.pop(number, None)

def display_numbers(dict):
    returnValue = ""
    for i,item in enumerate(dict):
        str = (f"\n {i}: {item}")
        returnValue += str
    
    return returnValue

def main():
    phonebook = {
        
    }

    addNumber(555555555, "fjajjaga", phonebook)
    print(display_numbers(phonebook))



if __name__ == "__main__":
    main()