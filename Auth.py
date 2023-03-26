class Auth:
    def __init__(self):
        self.users = []

    def registerUser(self, name, email, password):
        user = User(len(self.users) + 1, name, email, password)
        self.users.append(user)

    def getUserByEmail(self, email):
        for user in self.users:
            if user.getEmail() == email:
                return user
        return None

    def loginUser(self, email, password):
        user = self.getUserByEmail(email)
        if user and user.getPassword() == password:
            return user
        return None