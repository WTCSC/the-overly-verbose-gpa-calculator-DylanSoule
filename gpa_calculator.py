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
        for i in range(class_in_sem1):
            total += classes[0][i][1]
        if type == 'sem1' and class_in_sem1 != 0:
            return round(total/class_in_sem1,2)
    if type == 'sem2' or type == 'all':
        for i in range(class_in_sem2):
            total += classes[1][i][1]
        if type == 'sem2' and class_in_sem2 != 0:
            return round(total/class_in_sem2,2)
    if type == 'all' and (class_in_sem1 != 0 or class_in_sem2 != 0):
        return round(total/(class_in_sem1+class_in_sem2),2)
    return '0, as you have no classes in that part of the year'

def gpa_analysis(type, goal):
    gpa = calc_gpa(type)
    if goal < gpa:
        return("Congratulations, you have already met your GPA goal!")
    class_in_sem1 = len(classes[0])
    class_in_sem2 = len(classes[1])
    class_list1 = ['Class', 'Current Grade','','Improved Grade', 'Current GPA','', 'Improved GPA']
    class_list2 = ['Class', 'Current Grade','','Improved Grade', 'Current GPA','', 'Improved GPA']
    for i in range(class_in_sem1):
        class_list1.extend([classes[0][i][0], classes[0][i][1],'-->','4.0', gpa,'-->', round(((gpa*class_in_sem1)-classes[0][i][1]+4.0)/class_in_sem1,2)])
    for i in range(class_in_sem2):
        class_list2.extend([classes[0][i][0], classes[0][i][1],'-->', '4.0', gpa,'-->', round(((gpa*class_in_sem1)-classes[0][i][1]+4.0)/class_in_sem1,2)])
    if type == 'sem1' or type == 'all':
        print("Semester 1 GPA analysis:\n")
        change = (goal - gpa) * class_in_sem1
        print(f"Throughout all of your classes, you need to add {change} points to your classes")
        print("In addition, this is what gpa you will get if you change any one class to a 4.0:")
        for first, second, third, fourth, fifth, sixth, seventh in zip(
            class_list1[::7], class_list1[1::7], class_list1[2::7], class_list1[3::7], class_list1[4::7], class_list1[5::7], class_list1[6::7]
        ):
            print(f"{first: <15}{second: <20}{third: <10}{fourth: <20}{fifth: <20}{sixth: <10}{seventh}")
    if type == 'sem2' or type == 'all':
        print("Semester 2 GPA analysis:\n")
        change = (goal - gpa) * class_in_sem2
        print(f"Throughout all of your classes, you need to add {change} points to your classes")
        print("In addition, this is what gpa you will get if you change any one class to a 4.0:")
        for first, second, third, fourth, fifth, sixth, seventh in zip(
            class_list2[::7], class_list2[1::7], class_list2[2::7], class_list2[3::7], class_list2[4::7], class_list2[5::7], class_list2[6::7]
        ):
            print(f"{first: <15}{second: <20}{third: <10}{fourth: <20}{fifth: <20}{sixth: <10}{seventh}")
    

        

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
        done = input("\nWould you like to calculate another type(yes/no) ").lower()
        if done == 'yes':
            continue
        elif done == 'no':
            break
        else:
            while True:
                done = input("Please only enter yes or no").lower()
                if done == 'yes':
                    break
                elif done =='no':
                    break
            if done == 'yes':
                continue
        break
    
    want_to_analyze = input("\nWould you like to analyze for improvement(yes/no) ").lower()
    while True:
        if want_to_analyze != 'yes' and want_to_analyze != 'no':
            want_to_analyze = input("Error, make sure you only input 'yes' or 'no'").lower()
            continue
        else:
            break
    if want_to_analyze == 'yes':
        while True:
            type = input("\nHow would you like to analyze your gpa(Semester 1/Semester 2/Whole year) ").lower()
            goal_grade = validate_number(input("What is your goal GPA? "), True)
            if type == 'semester 1':
                print(gpa_analysis('sem1', goal_grade))
            elif type == 'semester 2':
                print(gpa_analysis('sem2', goal_grade))
            elif type == 'whole year':
                print(gpa_analysis('all', goal_grade))
            else:
                input("Wrong Input(Press enter to re-input) ")
                continue
            continuing = input("Would you like to analyze a different type(yes/no) ")
            while True:
                sdf
    classes = [[],[]]
