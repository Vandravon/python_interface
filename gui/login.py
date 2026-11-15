import customtkinter as ctk

from core.credentials import Credentials
from gui.main_menu import MainMenu


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("My Application")
        self.geometry("800x500")
        self.menu = None

        # Login
        self.label_login = ctk.CTkLabel(self, text="Login")
        self.label_login.pack(pady=(10, 0))
        self.entry_login = ctk.CTkEntry(self, placeholder_text="Your login")
        self.entry_login.pack(pady=5)

        # Password
        self.label_password = ctk.CTkLabel(self, text="Password")
        self.label_password.pack(pady=(10, 0))
        self.entry_password = ctk.CTkEntry(
            self, placeholder_text="Your password", show="•"
        )
        self.entry_password.pack(pady=5)

        # Connect button
        self.button_connect = ctk.CTkButton(
            self, text="Connect", command=self.on_connect
        )
        self.button_connect.pack(pady=20)

    def on_connect(self):
        credentials = Credentials(
            login=self.entry_login.get(),
            password=self.entry_password.get(),
        )

        # Hide the window
        self.withdraw()

        # Open main menu window, keep a reference so it is not garbage collected
        self.menu = MainMenu(self, credentials)
        self.menu.focus()
