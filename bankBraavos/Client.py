class Client:

    def __init__(self, name, lastName, document):
        self.name = name
        self.lastName = lastName
        self.document = document

    def seeInformation(self):
        return print(f'Client:\nname: {self.name}\nlast name: {self.lastName}\ndocument: {self.document}')
