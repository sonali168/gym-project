class Super:

    def create_member():
        global data
        global customer
        customer_data = {}
        customer = []

        Name = input('Name :')
        # if name.isalpha():

        Age = input('Age :')

        Gender = input('Gender(male, female, transgender) :')
        if Gender.lower() not in ['male', 'female', 'transgender']:
            print("invalid Gender")
            Gender = input('Gender(male, female, transgender) :')

        Mobile_number = input('Mobile number :')
        if len(Mobile_number) < 10 or len(Mobile_number) > 10:
            print("Please enter valid number")
            Mobile_number = input('Mobile number :')

        Email_id = input('Email_id')

        BMI = input('BMI :')

        Membership_duration = input('Membership duration in months (1,3,6 or 12) :')
        if Membership_duration not in ['1', '3', '6', '12']:
            print(" Please choose mention months option")
            Membership_duration = input('Membership duration in months (1,3,6 or 12) :')

        customer_data['Name'] = Name
        customer_data['Gender'] = Gender
        customer_data['Age'] = Age
        customer_data['Mobile_number'] = Mobile_number
        customer_data['Email_id'] = Email_id
        customer_data['BMI'] = BMI
        customer.append(customer_data)
        # customer += 1

    def view_member():  # final

        global data
        global customer
        global customer_data
        # customer = []
        # data = {}

        Mobile_number = input('Mobile number :')
        if len(Mobile_number) < 10 or len(Mobile_number) > 10:
            print("Please enter valid number")
            Mobile_number = input('Mobile number :')

        # if data['Mobile_number'] == Mobile_number:
        ls = list(customer_data.values())
        # print(ls)
        if Mobile_number in ls:  # in customer_data.values():
            # if Mobile_number in iter(customer:
            print(customer_data)
        else:
            print("No such member exist")

    def delete_member():
        global cutomer
        global data

        Mobile_number = input('Mobile number :')
        if len(Mobile_number) < 10 or len(Mobile_number) > 10:
            print("Please enter valid number")
            Mobile_number = input('Mobile number :')

        if data['Mobile_number'] == Mobile_number:
            if 'Mobile_number' in customer:
                data.pop('item')
                customer.append(data)



    def view_regimen():
        regimen_data = {}

        # BMI = int(18.5,25,30,31)

        # if BMI < 18.5:
        data1 = [('BMI <', 18.5), ('Mon', 'Chest'), ('Tue', 'Biceps'), ('Wed', 'Rest'), ('Thu', 'Back'),
                 ('Fri', 'Triceps'), ('Sat', 'rest'), ('Sun', 'Rest')]
        regimen_data.update(data1)

        # if BMI < 25:
        data2 = [('BMI <', 25), ('Mon', 'Chest'), ('Tue', 'Biceps'), ('Wed', 'Cardio/Abs'), ('Thu', 'Back'),
                 ('Fri', 'Triceps'), ('Sat', 'Legs'), ('Sun', 'Rest')]
        regimen_data.update(data2)

        # if BMI < 30:
        data3 = [('BMI <', 30), ('Mon', 'Chest'), ('Tue', 'Biceps'), ('Wed', 'Cardio/Abs'), ('Thu', 'Back'),
                 ('Fri', 'Triceps'), ('Sat', 'Legs'), ('Sun', 'Rest')]
        regimen_data.update(data3)

        # if BMI > 30:
        data4 = [('BMI >', 31), ('Mon', 'Chest'), ('Tue', 'Biceps'), ('Wed', 'Cardio'), ('Thu', 'Back'),
                 ('Fri', 'Triceps'), ('Sat', 'Cardio'), ('Sun', 'Cardio')]
        regimen_data.update(data4)


    def delete_regimen():

        regimen_data = {}
        enter = input('BMI')

        if enter in regimen_data:
            regimen_data.pop(enter)
        else:
            print("Check BMI")