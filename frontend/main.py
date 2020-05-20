# Lukewarmcat's Module Importer
import importlib, pkgutil, random, shelve;
modules = [name for _, name, _ in pkgutil.iter_modules(['lib'])]

for x in modules:
        vars()[x] = importlib.import_module(f'.{x}', package='lib')

r = confirmz.q("Registred?");

if not r:
        print("(Please note everything's being sent over plaintext.)\n")
        print("It seems like you're not registered. Shall we setup you with a account?")

        username = input("Desired Username: ").strip();
        password = input("Desired Password: ").strip();

        ret = reqsystem.addUser(username, password)
        if not ret:
                print("Error occured.")
        else:
                print(f"Welcome {username}! Please relog while selecting 'y' on registration.")
else:
        username = input("Username: ").strip();
        password = input("Password: ").strip();
        ret = reqsystem.getUser(username, password)

        if not ret:
                print("Error occured.")
        else:
                print(f"Welcome {rtext.rainbow(username)}. You're currently {rtext.rainbow(str(ret))}% gay.")
