classes=[]

def validate_number(number):
    while True:
        try:
            number = int(number)
        except:
            print("Error, please only input the number")
            continue
        break
    return number

def get_classes(class_num_sem1, class_num_sem2):
    for i in range(class_num_sem1):
        classes.append[input(f"")]

while True:
    # Verbose Stuff
    class_num_sem1 = validate_number(input("How many classes did you have in semester one?(Number Only) "))
    class_num_sem2 = validate_number(input("How many classes did you have in semester one?(Number Only) "))
    # More Verbose stuff
    get_classes()