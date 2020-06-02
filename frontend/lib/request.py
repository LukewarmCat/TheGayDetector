import requests;
def test(r, x, q):
    l = True;
    for b in r:
        if not b:
            l = False;
    if not l:
        print(f"Error: Missing {' or '.join(x)}.")
    else:
        m = requests.get(f"http://xerty.glitch.me/{q}/{'/'.join(r)}").json()
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

if __name__ == "__main__":
        exit()
