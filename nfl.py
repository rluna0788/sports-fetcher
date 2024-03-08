from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://site.api.espn.com"
SCOREBOARD_ENDPOINT = "/apis/site/v2/sports/basketball/nba/scoreboard"
ALL_TEAMS_ENDPOINT = "/apis/site/v2/sports/basketball/nba/teams"
SINGLE_TEAM_ENDPOINT = "/apis/site/v2/sports/basketball/nba/teams/"  # append team abbreviation

# printer = PrettyPrinter()


def get_scoreboard_data():
    data_obj = []
    home_team = ""
    away_team = ""
    home_team_score = ""
    away_team_score = ""

    events = get(BASE_URL + SCOREBOARD_ENDPOINT).json()["events"]

    for event in events:
        games = event['competitions']

        for game in games:
            clock = game['status']['displayClock']
            period = game['status']['period']
            for team in game['competitors']:
                if team['homeAway'] == "home":
                    home_team = team['team']['abbreviation']
                    home_team_score = team['score']

                elif team['homeAway'] == "away":
                    away_team = team['team']['abbreviation']
                    away_team_score = team['score']

            data_obj.append({"Match Up": home_team + " vs " + away_team,
                             "Score": home_team_score + " - " + away_team_score,
                             "Current Clock": clock,
                             "Period": period
                             })
        # print("--------------------------------------------")
        # print(f"{home_team['abbreviation']} vs {away_team['abbreviation']}")
        # print(f"{home_team_score} - {away_team_score}")
        # print(f"Time Clock: {clock} - Period: {period}")
    return data_obj

def get_teams():
    sports = get(BASE_URL + ALL_TEAMS_ENDPOINT).json()["sports"]

    for leagues in sports:
        for league in leagues["leagues"]:
            for team in league["teams"]:
                team_abbreviation = team["team"]["abbreviation"]
                team_stats = get_team_stats(team_abbreviation)
                print(f"{team_stats['team_name']} - {team_stats['division_standing']}")


def get_team_stats(team):
    team_stats = get(BASE_URL + SINGLE_TEAM_ENDPOINT + team).json()
    team_name = team_stats["team"]["displayName"]
    division_standing = team_stats["team"]["standingSummary"]
    team_data = {
        "team_name": team_name,
        "division_standing": division_standing
    }
    return team_data



