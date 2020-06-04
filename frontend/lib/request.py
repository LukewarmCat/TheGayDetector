import requests;
def test(r, x, q):
    l = True;
    for b in r:
        if not b:
            l = False;
    if not l:
        print(f"Error: Missing {' or '.join(x)}.")
    else:
        postMap = {};
        for i in range(len(x)):
            postMap[x[i]] = r[i]
<<<<<<< HEAD
        m = requests.post(f"https://xerty.lukewarmcat.codes/{q}", data=postMap).json()
=======
        m = requests.post(f"http://xerty.lukewarmcat.codes/{q}", data=postMap).json()
>>>>>>> 2d996b5fe6b858034f3893b01c7d84069b1e34aa

        if "error" in m:
            print(f"Error: {m['error']}")
            return False;
        if "sucess" in m:
            return m["sucess"];


def getUser(username, password):
    return test([username, password], ["username", "password"], "getUser")

def addUser(username, password):
    return test([username, password], ["username", "password"], "addUser")

def inviteUser(username, password, user):
    return test([username, password, user], ["username", "password", "user"], "inviteUser")

def declineInvite(username, password, guild):
    return test([username, password, guild], ["username", "password", "guild"], "declineInvite")

def acceptInvite(username, password, guild):
    return test([username, password, guild], ["username", "password", "guild"], "acceptInvite")

def createGuild(username, password, guildName):
    return test([username, password, guildName], ["username", "password", "guildName"], "createGuild")

def deleteGuild(username, password, guildName):
    return test([username, password, guildName], ["username", "password", "guildName"], "deleteGuild")

def deleteUser(username, password):
    return test([username, password], ["username", "password"], "deleteUser")

def leaveGuild(username, password, guildName):
    return test([username, password, guildName], ["username", "password", "guildName"], "leaveGuild")

def getGuildRanking(username, password):
    return test([username, password], ["username", "password"], "getGuildRanking")

def getUserRanking(username, password):
    return test([username, password], ["username", "password"], "getUserRanking")

def rerollXerty(username, password):
    return test([username, password], ["username", "password"], "rerollXerty")

if __name__ == "__main__":
        exit()
