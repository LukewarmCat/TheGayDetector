from . import spinnerz;
import requests;

def getUser(username, password):
    if username and password:
            with spinnerz.Spinner("Sending request to server... "):
                r = requests.get(f"https://xerty.glitch.me/getUser/{username}/{password}").json()
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

def addUser(username, password):
        if username and password:
                with spinnerz.Spinner("Sending request to server... "):
                        r = requests.get(f"https://xerty.glitch.me/addUser/{username}/{password}").json()
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

def inviteUser(username, password, user):
        if username and password and user:
                with spinnerz.Spinner("Sending request to server... "):
                        r = requests.get(f"https://xerty.glitch.me/inviteUser/{username}/{password}/{user}").json()
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

def declineInvite(username, password, guild):
        if username and password and guild:
                with spinnerz.Spinner("Sending request to server... "):
                        r = requests.get(f"https://xerty.glitch.me/declineInvite/{username}/{password}/{guild}").json()
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

def acceptInvite(username, password, guild):
        if username and password and guild:
                with spinnerz.Spinner("Sending request to server... "):
                        r = requests.get(f"https://xerty.glitch.me/acceptInvite/{username}/{password}/{guild}").json()
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

def createGuild(username, password, guildName):
    if username and password and guildName:
            with spinnerz.Spinner("Sending request to server... "):
                r = requests.get(f"https://xerty.glitch.me/createGuild/{username}/{password}/{guildName}").json()
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

def deleteGuild(username, password, guildName):
    if username and password and guildName:
            with spinnerz.Spinner("Sending request to server... "):
                r = requests.get(f"https://xerty.glitch.me/deleteGuild/{username}/{password}/{guildName}").json()
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

def deleteUser(username, password):
    if username and password:
            with spinnerz.Spinner("Sending request to server... "):
                r = requests.get(f"https://xerty.glitch.me/deleteUser/{username}/{password}").json()
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

def leaveGuild(username, password, guildName):
    if username and password and guildName:
            with spinnerz.Spinner("Sending request to server... "):
                r = requests.get(f"https://xerty.glitch.me/leaveGuild/{username}/{password}/{guildName}").json()
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
