fron super_user import Super
from Member_user import Member


def super_options():
    print("1.Create member")
    print("2.View member")
    print("3.Delete member")
    print("4.update member")
    print("5.Create regimen")
    print("6.View regimen")
    print("7.Delete regimen")
    print("8.Update regimen")
    print("0.Exit")


def member_options():
    print("1.My regimen")
    print("2.My profile")
    print("0.Exit")


print("-----Welcome To Fitfactory-----")
print("Please kindly enter given options super user or member user")

user_options = input()
while user_options not in ['super user', 'member user']:
    print("Please kindly enter given options super user or member user")
    user_options = input()

if user_options == 'super user':
    super_user_password = input("super_user_password : ")
    set_password = "superfit"
    while super_user_password != set_password:
        print("Please enter correct password")
        super_user_password = input("super_user_password : ")

    print("You have following authorities.")
    option1 = super_options()

    choice = int(input("Kindly enter options between 1,2,3,4,5,6,7,8:"))
    while choice < 0 or choice > 8:
        print("Kindly enter options between 1,2,3,4,5,6,7,8")
        choice = int(input("Kindly enter options between 1,2,3,4,5,6,7,8:"))


else:
    user_options == 'member user'
    member_user_password = input("member_user_password : ")
    set_password = "memberfit"
    while member_user_password != set_password:
        print("Please enter correct password")
        member_user_password = input("member_user_password : ")

    print("You have following authorities.")
    options2 = member_options()

    choice = int(input("Kindly enter options between 1,2:"))
    while choice < 1 or choice > 2:
        print("Kindly enter options between 1,2")
        choice = int(input("Kindly enter options between 1,2:"))

obj1 = Super()

while choice != 0:

    if choice == 1:
        obj1.create_member()
        super_options()

        choice = int(input("Kindly enter options between 1,2,3,4,5,6,7,8:"))
        while choice < 0 or choice > 8:
            print("Kindly enter options between 1,2,3,4,5,6,7,8")
            choice = int(input("Kindly enter options between 1,2,3,4,5,6,7,8:"))

    elif choice == 2:
        obj1.view_member()
        super_options()

        choice = int(input("Kindly enter options between 1,2,3,4,5,6,7,8:"))
        while choice < 0 or choice > 8:
            print("Kindly enter options between 1,2,3,4,5,6,7,8")
            choice = int(input("Kindly enter options between 1,2,3,4,5,6,7,8:"))

    elif choice == 3:
        obj1.view_member()
        super_options()

        choice = int(input("Kindly enter options between 1,2,3,4,5,6,7,8:"))
        while choice < 0 or choice > 8:
            print("Kindly enter options between 1,2,3,4,5,6,7,8")
            choice = int(input("Kindly enter options between 1,2,3,4,5,6,7,8:"))

    elif choice == 4:
        obj1.delete_member()
        super_options()

        choice = int(input("Kindly enter options between 1,2,3,4,5,6,7,8:"))
        while choice < 0 or choice > 8:
            print("Kindly enter options between 1,2,3,4,5,6,7,8")
            choice = int(input("Kindly enter options between 1,2,3,4,5,6,7,8:"))

    elif choice == 4:
        obj1.update_member()
        super_options()

        choice = int(input("Kindly enter options between 1,2,3,4,5,6,7,8:"))
        while choice < 0 or choice > 8:
            print("Kindly enter options between 1,2,3,4,5,6,7,8")
            choice = int(input("Kindly enter options between 1,2,3,4,5,6,7,8:"))

    elif choice == 0:
        print("End")

obj2 = Member()

while choice != 0:

    if choice == 1:
        obj1.my_regimen()
        member_options()

        choice = int(input("Kindly enter options between 1,2,0 :"))
        while choice < 0 or choice > 8:
            print("Kindly enter options between 1,2,0 :")
            choice = int(input("Kindly enter options between 1,2,0:"))

    elif choice == 2:
        obj1.view_member()
        super_options()

        choice = int(input("Kindly enter options between 1,2,0 :"))
        while choice < 0 or choice > 8:
            print("Kindly enter options between 1,2,0 :")
            choice = int(input("Kindly enter options between 1,2,0 :"))

    elif choice == 0:
        print("End")