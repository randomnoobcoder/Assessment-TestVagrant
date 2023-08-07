import unittest
from recent_played_songs import RecentPlayedSongs


class TestRecentPlayedSongs(unittest.TestCase):

    def test_non_existent_user(self):
        recent_plays = RecentPlayedSongs(capacity_per_user=3)

        # The recent_plays is empty, and the user does not have any recently played songs
        self.assertEqual(recent_plays.get_recently_played_songs("UnknownUser"), [])

    def test_capacity_limit(self):
        recent_plays = RecentPlayedSongs(capacity_per_user=2)

        # Adding songs for user 'User1'
        recent_plays.add_song("User1", "S1")
        recent_plays.add_song("User1", "S2")
        self.assertEqual(recent_plays.get_recently_played_songs("User1"), ['S1', 'S2'])

        # Adding more songs than the capacity (2)
        recent_plays.add_song("User1", "S3")
        recent_plays.add_song("User1", "S4")
        self.assertEqual(recent_plays.get_recently_played_songs("User1"), ['S3', 'S4'])

        # Only the latest 2 songs should be in the list
        self.assertEqual(len(recent_plays.get_recently_played_songs("User1")), 2)

    def test_add_song_and_get_recently_played_songs(self):
        recent_plays = RecentPlayedSongs(capacity_per_user=3)

        # Adding songs for user 'User2'
        recent_plays.add_song("User2", "S1")
        recent_plays.add_song("User2", "S2")
        recent_plays.add_song("User2", "S3")
        self.assertEqual(recent_plays.get_recently_played_songs("User2"), ['S1', 'S2', 'S3'])

        recent_plays.add_song("User2", "S4")
        self.assertEqual(recent_plays.get_recently_played_songs("User2"), ['S2', 'S3', 'S4'])

        recent_plays.add_song("User2", "S2")
        self.assertEqual(recent_plays.get_recently_played_songs("User2"), ['S3', 'S4', 'S2'])

        recent_plays.add_song("User2", "S1")
        self.assertEqual(recent_plays.get_recently_played_songs("User2"), ['S4', 'S2', 'S1'])


if __name__ == "__main__":
    unittest.main()
