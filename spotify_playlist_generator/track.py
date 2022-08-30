class Track:

    def _init_(self, name, id, artist):

        self.name = name
        self.id = id
        self.artist = artist

    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"

    def _str_(self):
        return self.name + " by " + self.artist