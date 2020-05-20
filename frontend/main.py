import random, shelve, rtext, confirmz, reqsystem;

r = confirmz.q("Registred?");

if not r:
        print("(Please note everything's being sent over plaintext.)\n")
        print("It seems like you're not registered. Shall we setup you with a account?")

        username = input("Desired Username: ").strip();
        password = input("Desired Password: ").strip();

        returne = reqsystem.addUser(username, password)
        if not returne:
                print("Error occured.")
        else:
                print(f"Welcome {username}! Please relog while selecting 'y' on registration.")
else:
        username = input("Username: ").strip();
        password = input("Password: ").strip();
        returne = reqsystem.getUser(username, password)

        if not returne:
                print("Error occured.")
        else:
                print(f"Welcome {rtext.rainbow(username)}. You're currently {rtext.rainbow(str(returne))}% gay.")
