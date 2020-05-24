# Enable VT100 support on Windows
import os;
os.system("")

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

from lib import *
zui = zui.Zui();

r = zui.confirmation("Are you registered?")

if not r:
    zui.center("It seems like you're not registered. Shell we setup you with a account?");

    username = zui.input("Desired Username: ").strip()
    password = zui.input("Desired Password: ").strip()
    ret = reqsystem.addUser(username, password)
    if not ret:
            zui.center("Error occured.")

    else:
            zui.center(f"Welcome {username}! Please relog while selecting 'y' on registration.")
else:
        username = zui.input("Username: ").strip();
        password = zui.input("Password: ").strip();
        user = reqsystem.getUser(username, password)

        if not user:
                zui.center("Error occured.")
        else:
                if options.cg:
                    zui.center(f"Making guild {options.cg}..")
                    ret = reqsystem.createGuild(username, password, options.cg)

                    if not ret:
                            zui.center("Error occured.")
                    else:
                            zui.center("Guild has been made.")

                if options.ai:
                    zui.center(f"Joining guild {options.ai}")
                    ret = reqsystem.acceptInvite(username, password, options.ai)
                    if not ret:
                        zui.center("Error occured.")
                    else:
                        zui.center(f"You've joined {options.ai}.")

                if options.di:
                    ret = reqsystem.declineInvite(username, password, options.di)
                    if not ret:
                        zui.center("Error occured.")
                    else:
                        zui.center("Invite declined.")

                if options.iu:
                    zui.center(f"Inviting {options.iu}. ")
                    ret = reqsystem.inviteUser(username, password, options.iu)
                    if not ret:
                        zui.center("Error occured.")
                    else:
                        zui.center("User invited.")

                if options.lg:
                    zui.center(f"Leaving guild {options.lg}. ")
                    ret = reqsystem.leaveGuild(username, password, options.iu)
                    if not ret:
                        zui.center("Error occured.")
                    else:
                        zui.center("Guild left.")

                if options.dg:
                    zui.center(f"Deleting guild {options.dg}. ")
                    ret = reqsystem.deleteGuild(username, password, options.dg)
                    if not ret:
                        zui.center("Error occured.")
                    else:
                        zui.center("Guild deleted.")

                if options.du:
                    ok = zui.confirmation("Do you really want to do this? Your account will be removed and you will be removed from all guilds.")
                    if not ok:
                        zui.center("You can log back in without using this tag.")
                        exit()
                    else:
                        zui.center(f"Deleting your account... ")
                        ret = reqsystem.deleteUser(username, password)
                        if not ret:
                            zui.center("Error occured.")
                        else:
                            zui.center("Account deleted.")
                            exit()

                if "guild" not in user:
                    name = rtext.rainbow(f"{username}")
                else:
                    name = rtext.rainbow(f"[{user['guild']['name']}] {username}")

                if not user["invitations"]:
                    invitn = "You don't have any Guild Invitations."
                else:
                    invitn = f"You're invited to: {', '.join(user['invitations'])}.\nUse `main.py --acceptinvite name` to join a guild, and `main.py --declineguild name`"

                zui.center(invitn)

                zui.center(f'Welcome {name}. You\'re currently {rtext.rainbow(str(user["proc"]))}% xerty.')
