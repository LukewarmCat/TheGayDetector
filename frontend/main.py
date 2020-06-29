# Tkinter
from ttkthemes import themed_tk as tk;
from tkinter import ttk
import tkinter as tko;
import tkinter.messagebox as messagebox

# Discord RPC
from pypresence import Presence
import time, atexit;

# Libaries (request)
from lib import *

activity = {
    "state": "Logged Out",
    "details": "Not logged in.",
    "large_text": "https://github.com/LukewarmCat/xerty",
    "large_image": "large"
}

RPC = Presence("716003185503764511")

rpcOff = None;
try:
    RPC.connect()
except (FileNotFoundError, ConnectionRefusedError):
    rpcOff = True;

if not rpcOff:
    RPC.update(**activity)

    def set_details(detail):
        activity["details"] = detail
        RPC.update(**activity)

    def set_state(state):
        activity["state"] = state
        RPC.update(**activity)

window = tk.ThemedTk(background=True, toplevel=True)
window.get_themes()

window.set_theme("equilux")

window.title("Main Menu")

def registerw():
    rw = tko.Toplevel(window)
    rw.title("Register Menu")

    ttk.Label(rw, text="Username:").grid(column=1, row=1)
    usernameo = ttk.Entry(rw, width=10)
    usernameo.grid(column=2, row=1)

    ttk.Label(rw, text="Password:").grid(column=1, row=2)
    passwordo = ttk.Entry(rw, width=10)
    passwordo.grid(column=2, row=2)

    def submitr():
            username = usernameo.get()
            password = passwordo.get()

            ret = request.addUser(username, password)
            if not ret:
                messagebox.showerror("Error", "Error occured.")
            else:
                messagebox.showinfo("Information", "User added.")

    ttk.Button(rw, text="Submit", command=submitr).grid(column=1, row=3)

def loginw():
    rl = tko.Toplevel(window)
    rl.title("Login Menu")

    ttk.Label(rl, text="Username:").grid(column=1, row=1)
    usernameo = ttk.Entry(rl, width=10)
    usernameo.grid(column=2, row=1)

    ttk.Label(rl, text="Password:").grid(column=1, row=2)
    passwordo = ttk.Entry(rl, width=10)
    passwordo.grid(column=2, row=2)

    def submitl():
            username = usernameo.get()
            password = passwordo.get()

            user = request.getUser(username, password)
            if not user:
                messagebox.showerror("Error", "Error occured.")
            else:
                def submits():
                    def submitss():
                        ret = request.deleteUser(username, password)
                        if not ret:
                            messagebox.showerror("Error", "Error occured.")
                        else:
                            messagebox.showinfo("Information", "Account deleted.")

                    def rxg():
                        ret = request.rerollXerty(username, password)
                        if not ret:
                            messagebox.showerror("Error", "Error occured.")
                        else:
                            messagebox.showinfo("Information", "Xerty Rerolled.")

                    ls = tko.Toplevel(window)
                    ttk.Button(ls, text="Delete Your Account", command=submitss).grid(column=1, row=1)
                    ttk.Button(ls, text="Reroll Xerty", command=rxg).grid(column=1, row=2)

                def ulg():
                    ret = request.getUserRanking(username, password)
                    if not ret:
                        messagebox.showerror("Error", "Error occured.")
                    else:
                        ul = tko.Toplevel(window)
                        for i in range(len(ret)):
                            if i < 10:
                                ttk.Label(ul, text=f"#{i+1} | {ret[i][1]} [{ret[i][0]}]").grid(column=1, row=i)
                def submitg():
                    if "guild" in user:
                        lg = tko.Toplevel(window)
                        ttk.Label(lg, text=f"You're in {user['guild']['name']}").grid(column=1, row=1)
                        ttk.Label(lg, text=f"Members: {', '.join(user['guild']['accounts'])}").grid(column=1, row=4);
                        ttk.Label(lg, text=f"{user['guild']['name']} has a total of {user['guild']['totalxerty']}% xerty.").grid(column=1, row=3)


                        def glg():
                            ret = request.getGuildRanking(username, password)
                            if not ret:
                                messagebox.showerror("Error", "Error occured.")
                            else:
                                gl = tko.Toplevel(window)
                                for i in range(len(ret)):
                                    if i < 10:
                                        ttk.Label(gl, text=f"#{i+1} | {ret[i][1]} [{ret[i][0]}]").grid(column=1, row=i)

                        def dvg():
                            ret = request.deleteGuild(username, password, user['guild']['name'])
                            if not ret:
                                messagebox.showerror("Error", "Error occured.")
                            else:
                                messagebox.showinfo("Information", "Guild Disbanded.")

                        def lvg():
                            ret = request.leaveGuild(username, password, user['guild']['name'])
                            if not ret:
                                messagebox.showerror("Error", "Error occured.")
                            else:
                                messagebox.showinfo("Information", "Guild Left.")

                        def ivg():
                            ivug = tko.Toplevel(window);
                            ivsub = ttk.Entry(ivug, width=10)
                            ivsub.grid(column=1, row=1)
                            def ivugt():
                                ret = request.inviteUser(username, password, ivsub.get())
                                if not ret:
                                    messagebox.showerror("Error", "Error occured.")
                                else:
                                    messagebox.showinfo("Information", "User invited.")

                            ttk.Button(ivug, text="Submit", command=ivugt).grid(column=2, row=1)


                        if user['guild']['owner'] == username:
                            ttk.Label(lg, text=f"You're a owner.").grid(column=1, row=2)
                            ttk.Button(lg, text="Disband Guild", command=dvg).grid(column=1, row=5)
                            ttk.Button(lg, text="Invite User", command=ivg).grid(column=1, row=6)
                        else:
                            ttk.Label(lg, text=f"You're in user.").grid(column=1, row=2)
                            ttk.Button(lg, text="Leave Guild", command=lvg).grid(column=1, row=5)

                        ttk.Button(lg, text="Guild Leaderboards", command=glg).grid(column=1, row=7)
                    else:
                        ln = tko.Toplevel(window)
                        ttk.Label(ln, text="You don't seem to be in a guild. Would you like to create one?").grid(column=1, row=1)
                        def lny():
                            lnyg = tko.Toplevel(window);
                            guildName = ttk.Entry(lnyg, width=10)
                            guildName.grid(column=1, row=1)
                            def lnygt():
                                ret = request.createGuild(username, password, guildName.get())
                                if not ret:
                                    messagebox.showerror("Error", "Error occured.")
                                else:
                                    messagebox.showinfo("Information", "Guild Made")

                            ttk.Button(lnyg, text="Submit", command=lnygt).grid(column=2, row=1)
                        ttk.Button(ln, text="Yes", command=lny).grid(column=1, row=2)
                        ttk.Button(ln, text="No (Close this window)").grid(column=2, row=2)
                def ai():
                    aiug = tko.Toplevel(window);
                    aisub = ttk.Entry(aiug, width=10)
                    aisub.grid(column=1, row=1)
                    def aigt():
                        ret = request.acceptInvite(username, password, aisub.get())
                        if not ret:
                            messagebox.showerror("Error", "Error occured.")
                        else:
                            messagebox.showinfo("Information", "Invite Accepted. Welcome!")
                    ttk.Button(aiug, text="Submit", command=aigt).grid(column=2, row=1)

                def di():
                    diug = tko.Toplevel(window);
                    disub = ttk.Entry(diug, width=10)
                    disub.grid(column=1, row=1)
                    def dugt():
                        ret = request.declineInvite(username, password, disub.get())
                        if not ret:
                            messagebox.showerror("Error", "Error occured.")
                        else:
                            messagebox.showinfo("Information", "Invite declined.")

                    ttk.Button(diug, text="Submit", command=dugt).grid(column=2, row=1)

                lo = tko.Toplevel(window)

                def closed():
                        if not rpcOff:
                            set_state("Logged Out")
                            set_details("Not logged in.")
                        lo.destroy();

                lo.protocol("WM_DELETE_WINDOW", closed)
                lo.title("Welcome!")
                if not rpcOff:
                    if "guild" in user:
                        set_details(f"[{user['guild']['tag']}] {username}")
                    else:
                        set_details(username)

                    set_state("In Game")

                ttk.Label(lo, text=f"Welcome {username}.").grid(column=1, row=1)
                ttk.Label(lo, text=f"You're currently {user['proc']}% xerty.").grid(column=1, row=4)

                ttk.Button(lo, text="Settings", command=submits).grid(column=10, row=1)
                ttk.Button(lo, text="Guilds", command=submitg).grid(column=10, row=4)
                ttk.Button(lo, text="User Leaderboards", command=ulg).grid(column=1, row=6)

                invitationl = ttk.Label(lo, text=f"You don't have any invitations.")
                invitationl.grid(column=1, row=5)

                if user["invitations"]:
                    invitationl["text"] = f"You're invitated to {','.join(user['invitations'])}"
                    ttk.Button(lo, text="Decline Invite", command=di).grid(column=1, row=7)
                    ttk.Button(lo, text="Accept Invite", command=ai).grid(column=1, row=8)

    ttk.Button(rl, text="Submit", command=submitl).grid(column=1, row=3)

ttk.Button(window, text="Login", command=loginw).grid(column=2, row=1)
ttk.Button(window, text="Register", command=registerw).grid(column=1, row=1)

window.mainloop()
