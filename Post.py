class Post:
    def __init__(self, id, author, title, body):
        self.id = id
        self.author = author
        self.title = title
        self.body = body

    def getId(self):
        return self.id

    def getAuthor(self):
        return self.author

    def getTitle(self):
        return self.title

    def getBody(self):
        return self.body

    def setAuthor(self, author):
        self.author = author

    def setTitle(self, title):
        self.title = title

    def setBody(self, body):
        self.body = body