import requests
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url, timeout=30).json()
        return response

class PlayerStats:
    def __init__(self, response):
        self.players = []

        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)

    def top_scorers_by_nationality(self, nationality):
        return sorted(filter(lambda x : x.nationality == nationality, self.players), key=(lambda x: x.points), reverse=True)
    
    def nationalities(self):
        nationalities = set()
        for player_dict in self.players:
            nationalities.add(player_dict.nationality)
        return list(nationalities)


def main():
    season = Prompt.ask("Select season", choices=["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"])
    player_reader = PlayerReader(f"https://studies.cs.helsinki.fi/nhlstats/{season}/players")
    stats = PlayerStats(player_reader.get_players())

    console = Console()

    
    nationality = Prompt.ask("Select nationality", choices=stats.nationalities())
    print(f"Players from {nationality}:")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("name", width=25)
    table.add_column("team", style="green")
    table.add_column("goals", justify="right", style="dim")
    table.add_column("assists", justify="right", style="dim")
    table.add_column("points", justify="right", style="red")
    for player in stats.top_scorers_by_nationality(nationality):
        table.add_row(
            str(player.name), str(player.team), str(player.goals), str(player.assists), str(player.points)
        )

    console.print(table)

if __name__ == "__main__":
    main()
