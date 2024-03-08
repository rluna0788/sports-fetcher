from requests import get

BASE_URL = "https://site.api.espn.com"
SCOREBOARD_ENDPOINT = "/apis/site/v2/sports/{sport}/{league}/scoreboard"
ALL_TEAMS_ENDPOINT = "/apis/site/v2/sports/{sport}/{league}/teams"
SINGLE_TEAM_ENDPOINT = "/apis/site/v2/sports/{sport}/{league}/teams/"  # append team abbreviation


def get_scoreboard_data(sport, league):
    data_obj = []
    home_team_score = ""
    away_team_score = ""

    events = get(BASE_URL + SCOREBOARD_ENDPOINT.replace("{sport}", sport).replace("{league}", league)).json()["events"]

    for event in events:
        games = event['competitions']
        clock = event['status']['displayClock']
        period = event['status']['period']
        status = event['status']['type']['name']
        match_up = event['name']
        game_date = event['date']
        winner = get_winner(games)

        for game in games:
            for team in game['competitors']:
                if team['homeAway'] == "home":
                    home_team_score = team['score']

                elif team['homeAway'] == "away":
                    away_team_score = team['score']

            data_obj.append({"Match Up": match_up,
                             "Game Date": game_date,
                             "Winner": winner,
                             "Score": home_team_score + " - " + away_team_score,
                             "Current Clock": clock,
                             "Period": period,
                             "Status": status
                             })
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


def get_winner(game_data):
    winner = None

    for game in game_data:
        for team in game['competitors']:
            if "winner" in team:
                if team['winner']:
                    winner = team['team']['displayName']
            else:
                winner = "TBD"

    return winner
