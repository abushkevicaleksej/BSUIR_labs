class ClientManager:
    def __init__(self):
        self.__clients = []

    def add_client(self, client):
        self.__clients.append(client)

    def get_clients(self):
        return self.__clients
