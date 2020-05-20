import requests, spinnerz, time, sys;

def getUser(username, password):
        with spinnerz.Spinner("Sending request to server... "):
                r = requests.get(f"https://gayaccounts.glitch.me/getUser/{username}/{password}").json()
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
                        r = requests.get(f"https://gayaccounts.glitch.me/addUser/{username}/{password}").json()
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
