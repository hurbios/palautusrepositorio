import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_funktio_loytaa_pelaajan(self):
        found_player = self.stats.search("Semenko")
        self.assertEqual(str(found_player), 'Semenko EDM 4 + 12 = 16')
        found_player = self.stats.search("asdf")
        self.assertEqual(found_player, None)

    def test_team_funktio_loytaa_tiimin(self):
        found_team = self.stats.team("EDM")
        self.assertEqual(len(found_team), 3)

    def test_top_funktio_palauttaa_karkipelaajat(self):
        top_players = self.stats.top(1, SortBy.POINTS)
        self.assertEqual(len(top_players), 2)
        self.assertEqual(str(top_players[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(str(top_players[1]), "Lemieux PIT 45 + 54 = 99")

        top_players = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(len(top_players), 2)
        self.assertEqual(str(top_players[0]), "Lemieux PIT 45 + 54 = 99")
        self.assertEqual(str(top_players[1]), "Yzerman DET 42 + 56 = 98")

        top_players = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 2)
        self.assertEqual(str(top_players[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(str(top_players[1]), "Yzerman DET 42 + 56 = 98")
