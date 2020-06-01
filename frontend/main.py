import tkinter as tk
import tkinter.messagebox as messagebox
from lib import *

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

    tk.Button(rw, text="Submit", command=submitr).grid(column=1, row=3)

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

                    ls = tk.Toplevel(window)
                    tk.Button(ls, text="Delete Your Account", command=submitss).grid(column=1, row=1)

                def submitg():
                    if "guild" in user:
                        lg = tk.Toplevel(window)
                        tk.Label(lg, text=f"You're in {user['guild']['name']}").grid(column=1, row=1)
                        tk.Label(lg, text=f"Members: {', '.join(user['guild']['accounts'])}").grid(column=1, row=2)

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

                            tk.Button(ivug, text="Submit", command=ivugt).grid(column=2, row=1)


                        if user['guild']['owner'] == username:
                            tk.Label(lg, text=f"You're a owner.").grid(column=1, row=3)
                            tk.Button(lg, text="Disband Guild", command=dvg).grid(column=1, row=4)
                            tk.Button(lg, text="Invite User", command=ivg).grid(column=1, row=5)

                        else:
                            tk.Label(lg, text=f"You're in user.").grid(column=1, row=3)
                            tk.Button(lg, text="Leave Guild", command=lvg).grid(column=1, row=4)

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

                            tk.Button(lnyg, text="Submit", command=lnygt).grid(column=2, row=1)
                        tk.Button(ln, text="Yes", command=lny).grid(column=1, row=2)
                        tk.Button(ln, text="No (Close this window)").grid(column=2, row=2)

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
                    tk.Button(aiug, text="Submit", command=aigt).grid(column=2, row=1)

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

                    tk.Button(diug, text="Submit", command=dugt).grid(column=2, row=1)

                lo = tk.Toplevel(window)

                lo.title("Welcome!")
                invitationl = tk.Label(lo, text=f"You don't have any invitations.")
                invitationl.grid(column=1, row=5)
                tk.Label(lo, text=f"Welcome {username}.").grid(column=1, row=1)
                tk.Button(lo, text="Settings", command=submits).grid(column=10, row=1)
                tk.Label(lo, text=f"You're currently {user['proc']}% xerty.").grid(column=1, row=4)
                tk.Button(lo, text="Guilds", command=submitg).grid(column=10, row=4)

                if user["invitations"]:
                    invitationl["text"] = f"You're invitated to {','.join(user['invitations'])}"
                    tk.Button(lo, text="Decline Invite", command=di).grid(column=1, row=6)
                    tk.Button(lo, text="Accept Invite", command=ai).grid(column=1, row=7)
    tk.Button(rl, text="Submit", command=submitl).grid(column=1, row=3)

tk.Button(window, text="Login", command=loginw).grid(column=2, row=1)
tk.Button(window, text="Register", command=registerw).grid(column=1, row=1)

window.mainloop()
