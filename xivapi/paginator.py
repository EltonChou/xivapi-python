from .core import Core


class Paginator:

    def __init__(self, client):
        self.client = client

    def roll(self, m):
        return self.get