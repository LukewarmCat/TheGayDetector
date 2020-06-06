import tkinter as tk
import tkinter.messagebox as messagebox
from lib import *
import time, atexit;
from pypresence import Presence

defaultButton = {"relief": "ridge", "borderwidth": 0, "highlightbackground": "lime", "highlightthickness": 2}
defaultListbox = {"borderwidth": 0}

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
except ConnectionRefusedError:
    rpcOff = True;

if not rpcOff:
    RPC.update(**activity)

    def set_details(detail):
        activity["details"] = detail
        RPC.update(**activity)

    def set_state(state):
        activity["state"] = state
        RPC.update(**activity)

window = tk.Tk()

window.title("Main Menu")

def registerw():
    rw = tk.Toplevel(window)
    rw.title("Register Menu")

    tk.Label(rw, text="Username:").grid(column=1, row=1)
    usernameo = tk.Entry(rw, width=10)
    usernameo.grid(column=2, row=1)

    tk.Label(rw, text="Password:").grid(column=1, row=2)
    passwordo = tk.Entry(rw, width=10)
    passwordo.grid(column=2, row=2)

    def submitr():
            username = usernameo.get()
            password = passwordo.get()

            ret = request.addUser(username, password)
            if not ret:
                messagebox.showerror("Error", "Error occured.")
            else:
                messagebox.showinfo("Information", "User added.")

    tk.Button(rw, text="Submit", command=submitr, **defaultButton).grid(column=1, row=3)

def loginw():
    rl = tk.Toplevel(window)
    rl.title("Login Menu")

    tk.Label(rl, text="Username:").grid(column=1, row=1)
    usernameo = tk.Entry(rl, width=10)
    usernameo.grid(column=2, row=1)

    tk.Label(rl, text="Password:").grid(column=1, row=2)
    passwordo = tk.Entry(rl, width=10)
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

                    ls = tk.Toplevel(window)
                    tk.Button(ls, text="Delete Your Account", command=submitss, **defaultButton).grid(column=1, row=1)
                    tk.Button(ls, text="Reroll Xerty", command=rxg, **defaultButton).grid(column=1, row=2)

                def ulg():
                    ret = request.getUserRanking(username, password)
                    if not ret:
                        messagebox.showerror("Error", "Error occured.")
                    else:
                        ul = tk.Toplevel(window)
                        listbox = tk.Listbox(ul, **defaultListbox)

                        for i in range(len(ret)):
                            if i < 10:
                                listbox.insert(i, f"#{i+1} | {ret[i][1]} [{ret[i][0]}]")
                        listbox.pack()
                def submitg():
                    if "guild" in user:
                        lg = tk.Toplevel(window)
                        tk.Label(lg, text=f"You're in {user['guild']['name']}").grid(column=1, row=1)
                        tk.Label(lg, text=f"Members: {', '.join(user['guild']['accounts'])}").grid(column=1, row=4);
                        tk.Label(lg, text=f"{user['guild']['name']} has a total of {user['guild']['totalxerty']}% xerty.").grid(column=1, row=3)


                        def glg():
                            ret = request.getGuildRanking(username, password)
                            if not ret:
                                messagebox.showerror("Error", "Error occured.")
                            else:
                                gl = tk.Toplevel(window)
                                listbox = tk.Listbox(gl, **defaultListbox)
                                for i in range(len(ret)):
                                    if i < 10:
                                        listbox.insert(i, f"#{i+1} | {ret[i][1]} [{ret[i][0]}]")
                                listbox.pack()

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
                            ivug = tk.Toplevel(window);
                            ivsub = tk.Entry(ivug, width=10)
                            ivsub.grid(column=1, row=1)
                            def ivugt():
                                ret = request.inviteUser(username, password, ivsub.get())
                                if not ret:
                                    messagebox.showerror("Error", "Error occured.")
                                else:
                                    messagebox.showinfo("Information", "User invited.")

                            tk.Button(ivug, text="Submit", command=ivugt, **defaultButton).grid(column=2, row=1)


                        if user['guild']['owner'] == username:
                            tk.Label(lg, text=f"You're a owner.").grid(column=1, row=2)
                            tk.Button(lg, text="Disband Guild", command=dvg, **defaultButton).grid(column=1, row=5)
                            tk.Button(lg, text="Invite User", command=ivg, **defaultButton).grid(column=1, row=6)
                        else:
                            tk.Label(lg, text=f"You're in user.").grid(column=1, row=2)
                            tk.Button(lg, text="Leave Guild", command=lvg, **defaultButton).grid(column=1, row=5)

                        tk.Button(lg, text="Guild Leaderboards", command=glg, **defaultButton).grid(column=1, row=7)
                    else:
                        ln = tk.Toplevel(window)
                        tk.Label(ln, text="You don't seem to be in a guild. Would you like to create one?").grid(column=1, row=1)
                        def lny():
                            lnyg = tk.Toplevel(window);
                            guildName = tk.Entry(lnyg, width=10)
                            guildName.grid(column=1, row=1)
                            def lnygt():
                                ret = request.createGuild(username, password, guildName.get())
                                if not ret:
                                    messagebox.showerror("Error", "Error occured.")
                                else:
                                    messagebox.showinfo("Information", "Guild Made")

                            tk.Button(lnyg, text="Submit", command=lnygt, **defaultButton).grid(column=2, row=1)
                        tk.Button(ln, text="Yes", command=lny, **defaultButton).grid(column=1, row=2)
                        tk.Button(ln, text="No (Close this window)", **defaultButton).grid(column=2, row=2)
                def ai():
                    aiug = tk.Toplevel(window);
                    aisub = tk.Entry(aiug, width=10)
                    aisub.grid(column=1, row=1)
                    def aigt():
                        ret = request.acceptInvite(username, password, aisub.get())
                        if not ret:
                            messagebox.showerror("Error", "Error occured.")
                        else:
                            messagebox.showinfo("Information", "Invite Accepted. Welcome!")
                    tk.Button(aiug, text="Submit", command=aigt, **defaultButton).grid(column=2, row=1)

                def di():
                    diug = tk.Toplevel(window);
                    disub = tk.Entry(diug, width=10)
                    disub.grid(column=1, row=1)
                    def dugt():
                        ret = request.declineInvite(username, password, disub.get())
                        if not ret:
                            messagebox.showerror("Error", "Error occured.")
                        else:
                            messagebox.showinfo("Information", "Invite declined.")

                    tk.Button(diug, text="Submit", command=dugt, **defaultButton).grid(column=2, row=1)

                lo = tk.Toplevel(window)

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

                tk.Label(lo, text=f"Welcome {username}.").grid(column=1, row=1)
                tk.Label(lo, text=f"You're currently {user['proc']}% xerty.").grid(column=1, row=4)

                tk.Button(lo, text="Settings", command=submits, **defaultButton).grid(column=10, row=1)
                tk.Button(lo, text="Guilds", command=submitg, **defaultButton).grid(column=10, row=4)
                tk.Button(lo, text="User Leaderboards", command=ulg, **defaultButton).grid(column=1, row=6)

                invitationl = tk.Label(lo, text=f"You don't have any invitations.")
                invitationl.grid(column=1, row=5)

                if user["invitations"]:
                    invitationl["text"] = f"You're invitated to {','.join(user['invitations'])}"
                    tk.Button(lo, text="Decline Invite", command=di, **defaultButton).grid(column=1, row=7)
                    tk.Button(lo, text="Accept Invite", command=ai, **defaultButton).grid(column=1, row=8)

    tk.Button(rl, text="Submit", command=submitl, **defaultButton).grid(column=1, row=3)

tk.Button(window, text="Login", command=loginw, **defaultButton).grid(column=2, row=1)
tk.Button(window, text="Register", command=registerw, **defaultButton).grid(column=1, row=1)

window.tk_setPalette(foreground="lime", background="black")
window.mainloop()
