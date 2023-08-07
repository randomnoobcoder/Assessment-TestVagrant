class RecentPlayedSongs:
    def __init__(self, capacity_per_user):
        self.capacity_per_user = capacity_per_user
        self.recently_played = {}

    def add_song(self, user, song):
        if user not in self.recently_played:
            self.recently_played[user] = []

        # Check if the list is at its maximum capacity
        if len(self.recently_played[user]) >= self.capacity_per_user:
            # Remove the least recently played song (first element in the list)
            self.recently_played[user].pop(0)

        # Add the newly played song to the end of the list
        self.recently_played[user].append(song)

    def get_recently_played_songs(self, user):
        return self.recently_played.get(user, [])

