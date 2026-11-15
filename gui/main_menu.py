import customtkinter as ctk


class MainMenu(ctk.CTkToplevel):

    def __init__(self, parent, credentials):
        super().__init__(parent)
        self.parent = parent
        self.title("Main Menu")
        self.geometry("800x500")

        # Multi-line text area
        self.textbox = ctk.CTkTextbox(self, height=150)
        self.textbox.pack(padx=20, pady=(20, 10), fill="x")

        # Frame holding 2x buttons
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True)

        for i, label in enumerate(["Button 1", "Button 2", "Button 3", "Button 4"]):
            button = ctk.CTkButton(frame, text=label)
            button.grid(row=i // 2, column=i % 2, padx=20, pady=20)

        # Frame button buttons
        bot_frame = ctk.CTkFrame(self)
        bot_frame.pack(expand=True)
        for i, [label, command] in enumerate([["Test", self.on_test], ["Login", self.on_login]]):
            button = ctk.CTkButton(bot_frame, text=label, command=command)
            button.grid(row=i // 2, column=i % 2, padx=20, pady=20)


        '''
        # Test button
        self.button_test = ctk.CTkButton(self, text="Test", command=self.on_test)
        self.button_test.pack(pady=(0, 10))

        self.button_login = ctk.CTkButton(self, text="Login", command=self.on_login)
        self.button_login.pack(pady=(0, 20))
        '''

    def on_test(self):
        print(self.textbox.get("1.0", "end-1c"))

    def on_login(self):
        # Back to login
        self.parent.deiconify()
        self.destroy()