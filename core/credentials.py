class Credentials:
    """Holds the user's login and password for the current session."""

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password
