# Lukewarmcat's Module Importer
import importlib, time, sys, requests;
modules = ["spinnerz"]

for x in modules:
        vars()[x] = importlib.import_module(f'.{x}', package='lib')

def getUser(username, password):
        with spinnerz.Spinner("Sending request to serv'er... "):
                r = requests.get(f"https://gey.glitch.me/getUser/{username}/{password}").json()
        print("                                      ")
        if "error" in r:
                print("Error: " + r["error"])
                return False;
                exit()
        if "sucess" in r:
                return r["sucess"];
                exit()

def addUser(username, password):
        if username and password:
                with spinnerz.Spinner("Sending request to server... "):
                        r = requests.get(f"https://gey.glitch.me/addUser/{username}/{password}").json()
                print("                                      ")
                if "error" in r:
                        print("Error: " + r["error"])
                        return False;
                        exit()
                if "sucess" in r:
                        return r["sucess"];
                        exit()
        else:
                print("Error: Missing username or password")

if __name__ == "__main__":
        exit()
