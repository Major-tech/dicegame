class Session:
    """Holds user sessions in memory"""
    def __init__(self):
        self.logged_in = False
        self.username = None


    def login(self,username: str):
        self.logged_in = True
        self.username = username


    def logout(self):
        self.logged_in = False
        self.username = None
