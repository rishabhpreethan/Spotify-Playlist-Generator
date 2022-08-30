class Playlist:

    def _init_(self, name, id):

        self.name = name
        self.id = id

    def _str_(self):
        return f"Playlist: {self.name}"