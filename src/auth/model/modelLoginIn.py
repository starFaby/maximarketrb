class ModelLoginIn():
    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password

    # get y set id
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id

    # get y set username
    def getUsername(self):
        return self.username
    
    def setUsername(self, username):
        self.username = username

    # get y set password
    def getPassword(self):
        return self.password
    
    def setPassword(self, password):
        self.password = password



    def LoginInJason(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
            }