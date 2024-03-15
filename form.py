from tkinter import *
import requests  # HTTP Requests

#API Adrdes
API_URL = "http://127.0.0.1:5000"

def register_clicked():
    window_login.destroy()

    def register_user(username, password):
        if text_npass.get() == text_npassc.get() and text_npass.get() != "" and text_nusrnm.get() != "":
            response = requests.post(f"{API_URL}/register", json={"username": username, "password": password})
            if response.status_code == 201:
                lbl_register.configure(text="Register Success")
            else:
                lbl_register.configure(text="Registration Failed")
        elif text_npass.get() != "" and text_npassc.get() != "" and text_nusrnm.get() == "":
            lbl_register.configure(text="Please Enter Username")
        elif text_npass.get() != "" and text_nusrnm.get() == "":
            lbl_register.configure(text="Please Enter Username")
        elif text_nusrnm.get() != "" and text_npass.get() != "" and text_npassc.get() == "":
            lbl_register.configure(text="Please Confirm Password")
        elif text_npassc.get() != text_npass.get():
            lbl_register.configure(text="Passwords Do Not Match")
        elif text_nusrnm.get() != "":
            lbl_register.configure(text="Please Enter Password")

    # Register window
    global window_register
    window_register = Tk()
    window_register.geometry('400x300')
    window_register.title("Register")

    # Register form fields
    Label(window_register, text="Please Register").place(x=150, y=10)
    Label(window_register, text="New Username: ").place(x=150, y=40)
    Label(window_register, text="New Password: ").place(x=150, y=90)
    Label(window_register, text="Confirm Password: ").place(x=142, y=140)
    text_nusrnm = Entry(window_register, width=10)
    text_nusrnm.place(x=150, y=60)
    text_npass = Entry(window_register, width=10, show='*')
    text_npass.place(x=150, y=110)
    text_npassc = Entry(window_register, width=10, show='*')
    text_npassc.place(x=150, y=160)
    lbl_register = Label(window_register, text="")
    lbl_register.place(x=150, y=200)

    # Register button
    Button(window_register, text="Register", command=lambda: register_user(text_nusrnm.get(), text_npass.get())).place(x=157, y=230)
    Button(window_register, text="Login", command=lambda: [window_register.destroy(), login_window()]).place(x=165, y=260)

def login_window():
    global window_login
    window_login = Tk()
    window_login.geometry('400x300')
    window_login.title("Login")

    # Login form fields
    Label(window_login, text="Please Login").place(x=160, y=10)
    Label(window_login, text="Username: ").place(x=165, y=40)
    Label(window_login, text="Password: ").place(x=165, y=90)
    text_usrnm = Entry(window_login, width=10)
    text_usrnm.place(x=150, y=60)
    text_pass = Entry(window_login, width=10, show='*')
    text_pass.place(x=150, y=110)
    lbl_def = Label(window_login, text="")
    lbl_def.place(x=150, y=200)

    def login_clicked():
        if "'" in text_pass.get() and "'" in text_usrnm.get() and "%27" in text_pass and "%27" in text_pass:
            lbl_def.configure(text="Invalid Character")
        else:
            response = requests.post(f"{API_URL}/login", json={"username": text_usrnm.get(), "password": text_pass.get()})
            if response.ok:
                user_id = response.json().get("user_id")
                lbl_def.configure(text=f"Login successful. Your User ID is {user_id}")
            else:
                lbl_def.configure(text="Invalid username or password")

    # Login button
    Button(window_login, text="Login", command=login_clicked).place(x=125, y=140)
    Button(window_login, text="Register", command=register_clicked).place(x=195, y=140)

    window_login.mainloop()

login_window()
