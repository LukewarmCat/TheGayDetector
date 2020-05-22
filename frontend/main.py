from optparse import OptionParser

parser = OptionParser()
parser.add_option("-a", "--acceptinvite", dest="ai",
                  help="Accept a invite.")

parser.add_option("-d", "--declineinvite", dest="di",
                  help="Decline a guild invitation.")

parser.add_option("-c", "--createguild", dest="cg",
                  help="Create a guild.")

parser.add_option("-i", "--inviteuser", dest="iu",
                  help="Invite a user to your guild.")

parser.add_option("-l", "--leaveguild", dest="lg",
                  help="Leave a guild.")

parser.add_option("-x", "--deleteguild", dest="dg",
                  help="Delete your guild.")

parser.add_option("-m", "--deleteuser", dest="du", action="store_true",
                  help="Delete your account.")

(options, args) = parser.parse_args()

import random, sys;
from lib import *;

r = confirmz.q("Registred?");

if not r:
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

                if options.di:
                    ret = reqsystem.declineInvite(username, password, options.di)
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

                if options.lg:
                    print(f"Leaving guild {options.lg}. ")
                    ret = reqsystem.leaveGuild(username, password, options.iu)
                    if not ret:
                        print("Error occured.")
                    else:
                        print("Guild left.")

                if options.dg:
                    print(f"Deleting guild {options.dg}. ")
                    ret = reqsystem.deleteGuild(username, password, options.dg)
                    if not ret:
                        print("Error occured.")
                    else:
                        print("Guild deleted.")

                if options.du:
                    ok = confirmz.q("Do you really want to do this? Your account will be removed and you will be removed from all guilds.")
                    if not ok:
                        print("You can log back in without using this tag.")
                        exit()
                    else:
                        print(f"Deleting your account... ")
                        ret = reqsystem.deleteUser(username, password)
                        if not ret:
                            print("Error occured.")
                        else:
                            print("Account deleted.")
                            exit()

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
