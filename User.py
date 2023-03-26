class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password