from optparse import OptionParser

parser = OptionParser()
parser.add_option("-a", "--acceptinvite", dest="ai",
                  help="Accept a invite.")
parser.add_option("-d", "--declineguild", dest="dg",
                  help="Decline a guild invitation.")
parser.add_option("-c", "--createguild", dest="cg",
                  help="Create a guild.")
parser.add_option("-i", "--inviteuser", dest="iu",
                  help="Invite a user to your guild.")

(options, args) = parser.parse_args()

import random, sys;
from lib import *;

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
        user = reqsystem.getUser(username, password)

        if not user:
                print("Error occured.")
        else:
                if options.cg:
                    print(f"Making guild {options.cg}..")
                    ret = reqsystem.createGuild(username, password, options.cg)

                    if not ret:
                            print("Error occured.")
                    else:
                            print("Guild has been made.")

                if options.ai:
                    print(f"Joining guild {options.ai}")
                    ret = reqsystem.acceptInvite(username, password, options.ai)
                    if not ret:
                        print("Error occured.")
                    else:
                        print(f"You've joined {options.ai}.")
                if options.dg:
                    ret = reqsystem.declineInvite(username, password, options.dg)
                    if not ret:
                        print("Error occured.")
                    else:
                        print("Invite declined.")

                if options.iu:
                    print(f"Inviting {options.iu}. ")
                    ret = reqsystem.inviteUser(username, password, options.iu)
                    if not ret:
                        print("Error occured.")
                    else:
                        print("User invited.")

                if "guild" not in user:
                    displayname = rtext.rainbow(f"{username}")
                else:
                    displayname = rtext.rainbow(f"[{user['guild']['name']}] {username}")

                if not user["invitations"]:
                    uinvite = "You don't have any Guild Invitations."
                else:
                    uinvite = f"You're invited to: {', '.join(user['invitations'])}.\nUse `main.py --acceptinvite name` to join a guild, and `main.py --declineguild name`"

                print(uinvite)

                proc = rtext.rainbow(str(user["proc"]))
                print(f"Welcome {displayname}. You're currently {proc}% xerty.")
