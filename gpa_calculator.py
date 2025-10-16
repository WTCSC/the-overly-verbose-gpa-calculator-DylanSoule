classes=[[],[]]

def validate_number(number, isgrade):
    while True:
        try:
            number = float(number)
        except:
            # Hella Verbose stuff
            number = input("Error, please only input a number ")
            continue
        break
    if not isgrade:
        return int(number)
    else:
        while number < 0 or number > 4:
            # GET HELLA VERBOSE
            number = validate_number(input("Make sure your grade is between 0.00 and 4.00 "), True)
    return number

def calc_gpa(type):
    total = 0
    class_in_sem1 = len(classes[0])
    class_in_sem2 = len(classes[1])

    if type == 'sem1' or type == 'all':
        for i in range(class_in_sem1-1):
            total += classes[0][i][1]
        if type == 'sem2' and class_in_sem1 != 0:
            return total/class_in_sem1
    if type == 'sem2' or type == 'all':
        for i in range(class_in_sem2-1):
            total += classes[1][i][1]
        if type == 'sem2' and class_in_sem2 != 0:
            return total/class_in_sem2
    if type == 'all' and class_in_sem1 != 0 and class_in_sem2 != 0:
        return total/(class_in_sem1+class_in_sem2)
    return '0, as you have no classes in that part of the year'

while True:
    # Verbose Stuff
    class_num_sem1 = validate_number(input("\nHow many classes did you have in semester one?(Number Only) "),False)

    for i in range(int(class_num_sem1)):
        classes[0].append([input(f"\nWhat is your class is your period number {i+1} in semester one? ")])
        classes[0][i].append(validate_number(input("What is your grade in that class?(0.00-4.00) "),True))

    # More Verbose stuff
    
    class_num_sem2 = validate_number(input("\nHow many classes did you have in semester two?(Number Only) "),False)

    for i in range(class_num_sem2):
        classes[1].append([input(f"\nWhat is your class number {i+1} for semester two? ")])
        classes[1][i].append(validate_number(input("What is your GPA in that class?(0.00 - 4.00) "),True))
    
    # Limgarium Verbiosa

    while True:
        type = input("\nHow would you like to view your gpa(Semester 1/Semester 2/Whole year) ").lower()
        if type == 'semester 1':
            print(f"\nYour GPA for Semester 1 is {calc_gpa('sem1')}")
        elif type == 'semester 2':
            print(f"\nYour GPA for Semester 2 is {calc_gpa('sem2')}")
        elif type == 'whole year':
            print(f"\nYour GPA for the whole year is {calc_gpa('all')}")
        else:
            input("Wrong Input(Press enter to re-input) ")
            continue
        if input("\nWould you like to calculate another type(yes/no) ").lower() == 'yes':
            continue
        else:
            break
    